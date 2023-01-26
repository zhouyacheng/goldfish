import pathlib
import re

import kubernetes.client
import yaml
from kubernetes.client.rest import ApiException


class KubernetesYamlClient(object):
    UPPER_FOLLOWED_BY_LOWER_RE = re.compile("(.)([A-Z][a-z]+)")
    LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE = re.compile("([a-z0-9])([A-Z])")

    def __init__(self, client, payload, **kwargs):
        self.client = client
        self.body = None
        self.payload = payload
        self.api = None
        self.kwargs = kwargs
        self._parse()

    def _parse(self):
        if isinstance(self.payload, str):
            self.body = yaml.safe_load(self.payload)
        if isinstance(self.payload, pathlib.Path):
            self.body = yaml.safe_load(self.payload.read_text())
        if isinstance(self.payload, dict):
            self.body = self.payload
        if self.body is None:
            raise Exception("yaml不能为空")

        group, _, version = self.body["apiVersion"].partition("/")
        if version == "":
            version = group
            group = "core"
        group = "".join(group.rsplit(".k8s.io", 1))
        group = "".join(word.capitalize() for word in group.split("."))
        fcn_to_call = "{0}{1}Api".format(group, version.capitalize())
        self.api = getattr(kubernetes.client, fcn_to_call)(self.client)
        kind = self.body["kind"]
        kind = self.UPPER_FOLLOWED_BY_LOWER_RE.sub(r"\1_\2", kind)
        self.kind = self.LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE.sub(r"\1_\2", kind).lower()
        namespace = self.body["metadata"]["namespace"]
        self.kwargs["namespace"] = namespace

    def call(self, method, **kwargs):
        if hasattr(self.api, "{0}_namespaced_{1}".format(method, self.kind)):
            resp = getattr(self.api, "{0}_namespaced_{1}".format(method, self.kind))(
                **kwargs
            )
        else:
            kwargs.pop("namespace", None)
            resp = getattr(self.api, "{0}_{1}".format(method, self.kind))(**kwargs)
        return resp

    def create(self):
        return self.call("create", body=self.body, **self.kwargs)

    def replace(self):
        name = self.body["metadata"]["name"]
        return self.call("replace", name=name, body=self.body, **self.kwargs)

    def patch(self):
        name = self.body["metadata"]["name"]
        return self.call("patch", name=name, body=self.body, **self.kwargs)

    def get(self):
        try:
            name = self.body["metadata"]["name"]
            namespace = self.body["metadata"]["namespace"]
            return self.call("read", name=name, namespace=namespace)
        except ApiException as e:
            if e.status == 404:
                return

    def delete(self):
        try:
            name = self.body["metadata"]["name"]
            return self.call("delete", name=name, **self.kwargs)
        except ApiException as e:
            if e.status == 404:
                return

    def ensure(self, force=False):
        if self.get() is None:
            return self.create()
        try:
            if force:
                self.delete()
                return self.create()
            return self.replace()
        except ApiException as e:
            raise e
