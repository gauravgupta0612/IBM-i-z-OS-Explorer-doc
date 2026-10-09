# Releases & changelog process

Every version is published as a **GitHub Release** of
[IBM-i-z-OS-Explorer](https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer/releases), with the `.vsix` attached and its section of the changelog as release notes. This site's [Changelog](../changelog.md) page picks up the same information automatically.

## How it fits together

```text
 CHANGELOG.md  ──►  git tag v1.2.3  ──►  GitHub Actions (main repo)
 (main repo)                               ├─ builds ibmi-zos-explorer-1.2.3.vsix
                                           └─ creates Release "v1.2.3"
                                                 notes = "## [1.2.3]" section of CHANGELOG.md
                                                 asset = the .vsix

 Documentation site (this repo) ── GitHub Actions, every hour + on every push
       └─ downloads CHANGELOG.md + the list of releases
       └─ regenerates changelog.md with release and download links
       └─ publishes to GitHub Pages
```

## Release a new version (step by step)

1. **Change the code** in the `ibmi-zos-explorer` folder and test it with F5.
2. **Raise the version** in `package.json`, following [semantic versioning](https://semver.org):

    | Change | Example |
    |---|---|
    | Bug fixes only | `1.0.0` → `1.0.1` |
    | New features, nothing broken | `1.0.1` → `1.1.0` |
    | Breaking changes | `1.1.0` → `2.0.0` |

3. **Add a section at the top of `CHANGELOG.md`**, using exactly this heading format, because the release build looks for it:

    ```markdown
    ## [1.0.1] – 2026-10-20

    ### Fixed
    - Compile errors now show the right line for SQLRPGLE members.

    ### Added
    - "Refresh" button on My Spooled Files.
    ```

    Use the sections **Added**, **Changed**, **Fixed**, **Removed** and **Security** as needed.

4. **Update the documentation** in the `ibmi-zos-explorer-doc` folder if a feature changed. You don't need to edit `docs/changelog.md`; it is generated.
5. **Publish:** double-click **`publish.bat`** in the `ibmi-zos-explorer` folder. It:
    1. commits the source changes (as Gaurav Gupta);
    2. pushes the source;
    3. pushes the documentation;
    4. pushes the tag `v<version>`, which starts the release build.
6. About **2 minutes** later the release appears under **Releases**. The documentation's changelog page shows it **within the hour**. For an immediate update, open the doc repo → **Actions** → **Build & deploy docs** → **Run workflow**.

## Changelog rules

- Newest version at the **top**.
- One `## [x.y.z] – YYYY-MM-DD` heading per version.
- Write for users ("Compile now…") rather than for developers ("Refactored…").
- Never change the section of a version that is already released; add a new version instead.

## Re-run a failed release

On the main repo, open **Actions** → the failed **Build & Release** run → **Re-run all jobs**.
If the tag points to the wrong commit, delete the release and the tag on GitHub, fix the code, and run `publish.bat` again.
