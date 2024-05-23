"""Get link info for links to Docker Hub."""
from dataclasses import dataclass
from pathlib import Path
import requests


@dataclass
class DockerHubInfo:
    """Info required from Docker Hub to generate a link or badge."""
    tag: str
    """Image tag."""
    digest: str
    """Image digest."""


def digest(tag_data: dict) -> str:
    """Return a tag's digest if it exists."""
    return tag_data.get("images", [{}])[0].get("digest", "")


def get_latest_tags() -> dict[str, DockerHubInfo]:
    """Return a list of tags from Docker Hub.
    
    Returns
    -------
    latest_tag
    
    latest-lite_tag
    """
    url = "https://hub.docker.com/v2/repositories/fcpindi/c-pac/tags?page_size=100"
    response = requests.get(url)
    tags_data = {tag["name"]: tag for tag in response.json().get("results")}
    tags = {name: tag for name, tag in tags_data.items() if name.startswith("release-")}
    tag_keys = list(tags.keys())
    tag_keys.sort(reverse=True)
    latest, lite = next(tag for tag in tag_keys if tag[-1].isdigit()), next(tag for tag in tag_keys if tag.endswith("-lite"))
    return {"primary": DockerHubInfo(tag=latest, digest=digest(tags[latest])),
            "lite": DockerHubInfo(tag=lite, digest=digest(tags[lite])),
            **{tag: DockerHubInfo(tag=tag, digest=digest(tags_data[tag]))
               for tag in ["nightly", "nightly-lite"]}}


def create_badge(variant: str, docker_hub_info: DockerHubInfo) -> dict[str, str]:
    """Create a Docker Hub RST badge for the given tag and digest."""
    version = docker_hub_info.tag.split("-v", 1)[-1].split("-", 1)[0]
    if version.startswith("nightly"):
        repstr = f"|{variant}-badge|"
        return {repstr: f""".. {repstr} image:: https://img.shields.io/badge/development_version-C--PAC_{version}-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/{docker_hub_info.tag}/images/{docker_hub_info.digest.replace(':', '-')}
   """}
    repstr = f"|latest-{variant}-badge|"
    return {repstr: f""".. {repstr} image:: https://img.shields.io/badge/last_published_version-C--PAC_{version}-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/{docker_hub_info.tag}/images/{docker_hub_info.digest.replace(':', '-')}
"""}


def update_doc(doc_path: Path) -> None:
    r"""Update the badges in ``docs_path``."""
    badges = {}
    for tag in get_latest_tags().items():
        badges.update(create_badge(*tag))
    with doc_path.open("r", encoding="utf8") as _doc:
        lines = _doc.readlines()
    for i, line in enumerate(lines):
        if line.startswith(".. |"):
            for key, badge in badges.items():
                if line.startswith(f".. {key}"):
                    lines[i:i+2] = badge
    with doc_path.open("w", encoding="utf8") as _doc:
        _doc.write("".join(lines))

if __name__ == "__main__":
    update_doc(Path(__file__).parent / "user/versions.rst")
