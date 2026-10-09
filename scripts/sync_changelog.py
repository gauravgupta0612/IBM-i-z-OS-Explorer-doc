"""Builds docs/changelog.md from the main repository.

Sources (public, no token needed; GITHUB_TOKEN is used when present to avoid rate limits):
  * CHANGELOG.md on the main branch of gauravgupta0612/IBM-i-z-OS-Explorer
  * the GitHub Releases of that repository (download links, release dates)

If GitHub cannot be reached, the existing docs/changelog.md is kept as is.
"""
import json
import os
import re
import sys
import urllib.request

REPO = "gauravgupta0612/IBM-i-z-OS-Explorer"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/CHANGELOG.md"
API = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "changelog.md")


def get(url: str, accept: str = "*/*") -> bytes:
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "docs-changelog-sync"})
    token = os.environ.get("GITHUB_TOKEN")
    if token and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main() -> int:
    try:
        local = os.environ.get("CHANGELOG_PATH")  # preview with a local CHANGELOG.md
        changelog = open(local, encoding="utf-8").read() if local else get(RAW).decode("utf-8")
    except Exception as e:  # keep the committed copy
        print(f"WARNING: could not download CHANGELOG.md ({e}); keeping existing page")
        return 0

    releases = {}
    api_ok = True
    try:
        for rel in json.loads(get(API, "application/vnd.github+json")):
            if rel.get("draft"):
                continue
            vsix = next((a for a in rel.get("assets", []) if a["name"].endswith(".vsix")), None)
            releases[rel["tag_name"].lstrip("v")] = {
                "url": rel["html_url"],
                "date": (rel.get("published_at") or "")[:10],
                "vsix": vsix["browser_download_url"] if vsix else None,
                "vsix_name": vsix["name"] if vsix else None,
                "prerelease": rel.get("prerelease", False),
            }
    except Exception as e:
        api_ok = False
        print(f"WARNING: could not read releases ({e}); using standard release links")

    body = re.sub(r"^# Changelog\s*\n", "", changelog, count=1)
    # MkDocs (Python-Markdown) needs 4-space indentation for nested lists; GitHub accepts 2.
    body = re.sub(r"^((?:  )+)(?=[-*] |\d+\. )", lambda m: "    " * (len(m.group(1)) // 2), body, flags=re.M)

    def add_links(m: re.Match) -> str:
        heading, ver = m.group(0), m.group(1)
        rel = releases.get(ver)
        if not rel and not api_ok:  # API unreachable: link by naming convention
            base = f"https://github.com/{REPO}/releases"
            rel = {"url": f"{base}/tag/v{ver}", "vsix": f"{base}/download/v{ver}/ibmi-zos-explorer-{ver}.vsix",
                   "vsix_name": f"ibmi-zos-explorer-{ver}.vsix", "prerelease": False}
        if not rel:
            return heading + "\n\n*Not released on GitHub yet.*"
        parts = [f"[:material-tag: Release v{ver}]({rel['url']})"]
        if rel["vsix"]:
            parts.append(f"[:material-download: {rel['vsix_name']}]({rel['vsix']})")
        if rel["prerelease"]:
            parts.append("**pre-release**")
        return heading + "\n\n" + " · ".join(parts)

    body = re.sub(r"^## \[([^\]]+)\].*$", add_links, body, flags=re.M)

    page = (
        "# Changelog\n\n"
        "All notable changes to **IBM i & z/OS Explorer**. This page is generated automatically from "
        f"[CHANGELOG.md](https://github.com/{REPO}/blob/main/CHANGELOG.md) and the "
        f"[GitHub Releases](https://github.com/{REPO}/releases), so it always matches the published versions.\n\n"
        "!!! tip \"Which version do I have?\"\n"
        "    **Extensions** (Ctrl+Shift+X) → *IBM i & z/OS Explorer*: the version is shown next to the name.\n\n"
        + body.strip() + "\n"
    )
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"changelog.md updated ({len(releases)} release(s) found)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
