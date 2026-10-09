# Passwords & security

## Passwords

- Passwords are asked **once**, on the first connect, and stored with **VS Code SecretStorage**. That is the operating system keychain:
    - **Windows:** Credential Manager
    - **macOS:** Keychain
    - **Linux:** libsecret / GNOME Keyring
- They are **never** written to `settings.json`, the workspace or any project file.
- **Reset Stored Password** (right-click a connection) replaces it.
- **Remove Connection** deletes the stored password too.

!!! danger "Never type a password into another field"
    Only type passwords into the masked **password** prompt. If a password ends up in another field (for example the connection name), remove the connection, create it again, and change that password on the host.

## Sharing connections

**Export Connections…** writes host, port, user, filters, library list and favorites to a JSON file, but **never passwords**. When colleagues import the file, each one enters their own password on first connect. See [Productivity](../reference/productivity.md#export-and-import-connections).

## SSH keys (IBM i)

Choose **SSH private key file** in the wizard. Only the **path** of the key is stored; the key itself stays in its file.

## TLS (z/OS)

**Verify certificate** is the default. **Accept self-signed certificate** turns off certificate checking for that connection only. Use it only on networks you trust.

## Logging

**Output → IBM i & z/OS** lists every request (the method and path for z/OS, the command for IBM i) so you can see exactly what was sent. Passwords and authorization headers are **never** logged.

## What the extension can do on the host

The extension acts with **your** user profile's authority, nothing more. Destructive actions always ask for confirmation first:

- deleting data sets, members, files and objects;
- replacing a member when copying, and uploading a folder into a data set;
- purging jobs and ending jobs.
