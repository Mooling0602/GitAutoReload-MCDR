from dataclasses import dataclass
from pathlib import Path

from mcdreforged.api.all import Serializable


class GitRepoInfo(Serializable):
    plugin_id: str
    local_dir: str
    remote_url: str
    branch: str
    is_linked: bool
    do_packaging: bool


@dataclass
class PureGitRepo(Serializable):
    plugin_id: str
    local_dir: Path


class GitRepoList(Serializable):
    git_repos: list[GitRepoInfo]
