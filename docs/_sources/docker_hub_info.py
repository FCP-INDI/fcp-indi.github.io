"""Get link info for links to Docker Hub."""
from pathlib import Path
import requests


def digest(tag_data: dict) -> str:
    """Return a tag's digest if it exists."""
    return tag_data.get("images", [{}])[0].get("digest", "")


def get_latest_tags() -> tuple[str, str, str]:
    """Return a list of tags from Docker Hub.
    
    Returns
    -------
    latest_tag
    
    latest-lite_tag
    """
    url = "https://hub.docker.com/v2/repositories/fcpindi/c-pac/tags?page_size=100"
    response = requests.get(url)
    tags_data = response.json()
    tags = {tag["name"]: tag for tag in tags_data.get("results", []) if tag["name"].startswith("release-")}
    tag_keys = list(tags.keys())
    tag_keys.sort(reverse=True)
    latest, lite = next(tag for tag in tag_keys if tag[-1].isdigit()), next(tag for tag in tag_keys if tag.endswith("-lite"))
    return ("primary", latest, digest(tags[latest])), ("lite", lite, digest(tags[lite]))


def create_badge(variant: str, tag: str, digest: str) -> dict[str, str]:
    """Create a Docker Hub RST badge for the given tag and digest."""
    version = tag.split("-v", 1)[1].split("-", 1)[0]
    repstr = f"|latest-{variant}-badge|"
    return {repstr: f""".. {repstr} image:: https://img.shields.io/badge/last_published_version-C--PAC_{version}-green
   :target: https://hub.docker.com/layers/fcpindi/c-pac/{tag}/images/{digest.replace(':', '-')}
"""}


def update_doc(doc_path: Path) -> None:
    r"""Update the badges in ``docs_path``."""
    badges = {}
    for tag in get_latest_tags():
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
