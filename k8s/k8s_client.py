import pathlib
import re

import kubernetes.client
import yaml
from kubernetes.client.rest import ApiException
from kubernetes.client import CustomObjectsApi


class KubernetesYamlClient(object):
    UPPER_FOLLOWED_BY_LOWER_RE = re.compile("(.)([A-Z][a-z]+)")
    LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE = re.compile("([a-z0-9])([A-Z])")

    def __init__(self, client, payload,**kwargs):
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

        group, _, self.version = self.body["apiVersion"].partition("/")
        if self.version == "":
            self.version = group
            group = "core"
        group = "".join(group.rsplit(".k8s.io", 1))
        group = "".join(word.capitalize() for word in group.split("."))
        fcn_to_call = "{0}{1}Api".format(group, self.version.capitalize())
        try:
            self.api = getattr(kubernetes.client, fcn_to_call)(self.client)
        except Exception as e:
            print(str(e))
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

    def ensure(self, force=False ,method: str=""):
        if method.lower() == "delete":
            return self.delete()
        if self.get() is None:
            return self.create()
        try:
            if force:
                self.delete()
                return self.create()
            return self.replace()
        except ApiException as e:
            raise e

    def resource_ensure(self,method: str=""):
        if not method and method.lower() not in {"list","retrieve","get","update","replace","delete","destroy","post","create"}:
            raise Exception("method not allowed.")
        if method.lower() == "get" or method.lower() == "list" or method.lower() == "retrieve":
            return self.get()
        if method.lower() == "update" or method.lower() == "replace":
            return self.replace()
        if method.lower() == "delete" or method.lower() == "destroy":
            return self.delete()
        if method.lower() == "create" or method.lower() == "post":
            return self.create()

    def custom_resource_ensure(self,crd_instance, method: str = "",name: str=""):
        crd_template = yaml.safe_load(crd_instance.template)
        group = crd_template.get("spec").get("group")
        plural = crd_template.get("spec").get("names").get("plural")
        namespace = self.body["metadata"]["namespace"]
        print(group,plural,namespace,self.kind,name)
        # ret = CustomObjectsApi().create_namespaced_custom_object(group=group, version=self.version,namespace=namespace,
        #                                                       plural=plural, body=self.body)
        if method.lower() == "get" or method.lower() == "list" or method.lower() == "retrieve":
            return CustomObjectsApi().get_cluster_custom_object(group=group, version=self.version,
                                                                 plural=plural, name=name)
        if method.lower() == "update" or method.lower() == "replace":
            return CustomObjectsApi().replace_cluster_custom_object(group=group, version=self.version,
                                                                 plural=plural, name=name, body=self.body)
        if method.lower() == "delete" or method.lower() == "destroy":
            return CustomObjectsApi().delete_cluster_custom_object(group=group, version=self.version,
                                                                 plural=plural, name=name)
        if method.lower() == "create" or method.lower() == "post":
            return CustomObjectsApi().create_cluster_custom_object(group=group, version=self.version,
                                                                 plural=plural, body=self.body)

