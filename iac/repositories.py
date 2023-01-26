from packaging.version import Version
from urllib.parse import urlparse
from typing import List

from gitea import Configuration, RepositoryApi, ApiClient


class ReleaseTag(object):
    def __init__(self,version: Version,name:str,commit: str, archive_url:str):
        self.version = version
        self.name = name
        self.commit = commit
        self.archive_url = archive_url


class BaseRepositoryProvider(object):
    def __init__(self,token:str,url:str):
        self.token = token
        self.url = url

    def tags(self , lower: Version = None) -> List[ReleaseTag]:
        raise NotImplementedError

class GiteaRepositoryProvider(BaseRepositoryProvider):

    def __init__(self, token:str, url:str,):
        super(GiteaRepositoryProvider,self).__init__(token,url)
        self.token = token
        self.url = url
        self.configuration = Configuration()

        parsed_url = urlparse(url)
        _,owner,name = parsed_url.path.split("/")
        new_host = url.replace(parsed_url.path,"")
        print(owner,name,f"{new_host}/api/v1")
        self.owner = owner
        self.name = name
        self.configuration.host = f"{new_host}/api/v1"
        self.configuration.api_key = {"Authorization": self.token}
        self.configuration.api_key_prefix = {"Authorization": "token"}

    @property
    def repository_api(self) -> RepositoryApi:
        return RepositoryApi(ApiClient(self.configuration))

    def tags(self , lower: Version = None) -> List[ReleaseTag]:
        page = 0
        while True:
            page += 1
            tags = self.repository_api.repo_list_tags(owner=self.owner, repo=self.name,page=page)
            if not tags:
                raise ValueError("no more tags!!")
            sorted_tags = sorted(tags,key=lambda x:x.name,reverse=True)
            for tag in sorted_tags:
                version = Version(tag.name)
                if lower and version <= lower:
                    raise ValueError("no new tags!!")
                yield ReleaseTag(version=version,name=tag.name,commit=tag.id,archive_url=tag.tarball_url)