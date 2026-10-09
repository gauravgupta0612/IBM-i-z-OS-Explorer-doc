---
hide:
  - navigation
---

# IBM i & z/OS Explorer

**One Visual Studio Code extension for IBM i and z/OS.**
Browse, edit, compile and run on both platforms from a single **IBM i & z/OS** view in the VS Code sidebar.

[Download the latest release :material-download:](https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer/releases/latest){ .md-button .md-button--primary }
[Quick start :material-rocket-launch:](getting-started/quick-start.md){ .md-button }

---

<div class="grid cards" markdown>

-   :material-server-network: **z/OS (through z/OSMF)**

    ---

    - Data sets and PDS/PDSE members: open, edit and save back to the host
    - USS files
    - Submit JCL, follow jobs and read spool output
    - TSO and MVS console commands

    [:octicons-arrow-right-24: z/OS features](zos/datasets.md)

-   :material-server: **IBM i (through SSH)**

    ---

    - Libraries, source files and members: edit and save
    - Compile, with errors shown in the Problems panel
    - CL commands; SQL results in a sortable grid
    - IFS, spooled files, job logs, PASE terminal

    [:octicons-arrow-right-24: IBM i features](ibmi/libraries.md)

-   :material-shield-key: **Secure by design**

    ---

    - Passwords are kept only in the OS keychain (VS Code SecretStorage)
    - Nothing secret is written to settings or project files
    - Every request is logged, without passwords

    [:octicons-arrow-right-24: Security](connections/security.md)

-   :material-history: **Changelog with every release**

    ---

    Each GitHub release carries its changelog section, and this site's changelog page updates on its own.

    [:octicons-arrow-right-24: Changelog](changelog.md)

</div>

## How it connects

| | IBM i | z/OS |
|---|---|---|
| **Protocol** | SSH (port 22) + SFTP | HTTPS REST (z/OSMF) |
| **Server side** | `STRTCPSVR *SSHD` | z/OSMF started, with the REST files, jobs, TSO and console services |
| **Sign-in** | Password or SSH key file | RACF password or passphrase |
| **Data access** | QSYS2 SQL services, CL through PASE `system`, CPYTOSTMF/CPYFRMSTMF | z/OSMF REST APIs |

## Requirements

- Visual Studio Code **1.85** or later (Windows, macOS or Linux)
- An IBM i at **7.3** or later with SSH, and/or a z/OS system with **z/OSMF**
- Network access from your PC to the host (VPN if needed)

!!! tip "New here?"
    Follow the [Quick start](getting-started/quick-start.md). You will have your first connection in about two minutes.
