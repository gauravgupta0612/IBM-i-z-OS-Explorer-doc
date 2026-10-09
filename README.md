# IBM i & z/OS Explorer – Documentation

Source of the documentation site for the [IBM i & z/OS Explorer](https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer) VS Code extension.

**Read it online:** <https://gauravgupta0612.github.io/IBM-i-z-OS-Explorer-doc/>

## What's inside

| Path | Content |
|---|---|
| `docs/` | The pages (Markdown) |
| `docs/changelog.md` | **Generated.** Built from the extension's `CHANGELOG.md` and GitHub Releases by `scripts/sync_changelog.py` |
| `mkdocs.yml` | Site configuration and navigation |
| `.github/workflows/docs.yml` | Builds and publishes to GitHub Pages on every push, every hour and on demand |

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>.

## One-time GitHub setup

**Settings → Pages → Build and deployment → Source: GitHub Actions.**

Author: Gaurav Gupta · MIT License
