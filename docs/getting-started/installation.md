# Installation

## Install from a .vsix file

1. Download **`ibmi-zos-explorer-<version>.vsix`** from the
   [Releases page](https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer/releases/latest).
2. In VS Code, open **Extensions** (++ctrl+shift+x++).
3. Click the **`…`** menu at the top right of the Extensions view, then **Install from VSIX…**.
4. Select the downloaded file. If VS Code asks, reload the window.

=== "Command line"

    ```bash
    code --install-extension ibmi-zos-explorer-1.1.0.vsix
    ```

=== "Several PCs"

    Copy the `.vsix` to a shared folder and run the command line above on each PC, or install it from VS Code as shown in the steps above.

After installation, a new **IBM i & z/OS** icon appears in the activity bar on the left, and the status bar shows something like
`z/OS 0 · IBM i 0` (the number of connections defined).

## Update to a new version

Install the newer `.vsix` the same way. VS Code replaces the old version. Your connections, filters and stored passwords are kept.

To see what changed, open the [Changelog](../changelog.md). Every release on GitHub also shows the changes for that version.

## Uninstall

**Extensions** → *IBM i & z/OS Explorer* → **Uninstall**.
Stored passwords stay in the OS keychain until you remove the connections. Remove the connections first if you want them gone.

## Requirements

| Item | Minimum |
|---|---|
| VS Code | 1.85 |
| Operating system | Windows 10/11, macOS 12+, Linux (x64/arm64) |
| IBM i | 7.3 or later, SSH server running |
| z/OS | 2.3 or later with z/OSMF |
