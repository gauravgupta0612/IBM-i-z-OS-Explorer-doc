# IBM i connection

## What you need

| Item | Value / where to get it |
|---|---|
| **Host** | IP address or DNS name of the IBM i, e.g. `myibmi.company.com` |
| **Port** | `22` (SSH). Ask your administrator if they changed it. |
| **User** | Your IBM i user profile, e.g. `GGUPTA` |
| **Password** | Your IBM i password. It is asked on first connect and stored in the OS keychain. |
| **SSH key** *(optional)* | Only if your administrator set up key-based login |

## Prerequisites on the IBM i

| Requirement | How to check / enable |
|---|---|
| **SSH server running** | `STRTCPSVR SERVER(*SSHD)` |
| **SSH server starts at IPL** | `CHGTCPSVR SVRSPCVAL(*SSHD) AUTOSTART(*YES)` |
| **IBM i 7.3+** | The extension uses the QSYS2 SQL services `OBJECT_STATISTICS`, `SYSPARTITIONSTAT`, `SYSTABLES`, `ACTIVE_JOB_INFO`, `OUTPUT_QUEUE_ENTRIES_BASIC` and `JOBLOG_INFO` |
| **Writable temp folder** | `/tmp` by default (setting `mainframe.ibmi.tempDir`) |
| *(optional)* **db2util** | `yum install db2util` makes SQL faster. Without it, Qshell `db2` is used. |

!!! tip "Quick test from Windows"
    Open a Command Prompt and run `ssh YOURUSER@yourhost`. If you get a shell prompt, the extension will connect too.

## The connection wizard

1. **Connection name**: any label, e.g. `PROD400`.
2. **Host name or IP**.
3. **Port**: `22`.
4. **User profile**.
5. **How do you sign in?**
    - **Password** (recommended): asked on the first connect and kept in the OS keychain.
    - **SSH private key file**: a file dialog opens; pick your key (e.g. `C:\Users\you\.ssh\id_rsa`).

After saving, the connection is tested automatically.

## What appears under the connection

| Node | Content |
|---|---|
| **Libraries** | Your library filters. Each library shows its **source files** (expand for members) and all other **objects** (`*PGM`, `*SRVPGM`, `*FILE`, `*MODULE`, `*DTAARA`…). |
| **IFS** | Your IFS paths. Expand folders; click a file to edit it. |
| **My Spooled Files** | Your spooled files, newest first (up to 300) |
| **My Active Jobs** | Your active jobs. Click one to see its job log. |

## Object library for compiles

By default, compiled objects go to the **same library as the source**.
To use another library: right-click the connection → **Edit Connection** → press ++enter++ through the prompts → **Object library for compiles**.

## How it works

| Operation | Implementation |
|---|---|
| CL commands | PASE `/QOpenSys/usr/bin/system "<command>"` |
| SQL | `db2util -o json` if installed, otherwise Qshell `db2 -f <file>` |
| Read a member | `CPYTOSTMF … STMFCCSID(1208)`, then SFTP download |
| Save a member | SFTP upload, `setccsid 1208`, then `CPYFRMSTMF … MBROPT(*REPLACE)` |
| IFS | SFTP |
| Spooled file | `CPYSPLF … TOFILE(*TOSTMF)` |

!!! warning "Sequence numbers and dates"
    Because members are transferred as stream files, source **sequence numbers and line dates are reset** when you save.

## Common problems

| Message | Fix |
|---|---|
| `All configured authentication methods failed` | Right-click → **Reset Stored Password** |
| `SSH key file not found` | **Edit Connection** → choose **Password**, or pick a valid key file |
| `ECONNREFUSED` / timeout | SSH server not started, wrong host or port, or a firewall or VPN is blocking you |
| `… in QSYS2 type *N not found` | The IBM i release is too old for that SQL service. Upgrade, or install the matching PTF group. |
| Strange characters in members | Check the CCSID of the source file. `mainframe.ibmi.sourceCcsid` should stay `1208`. |

More in [Troubleshooting](../reference/troubleshooting.md).
