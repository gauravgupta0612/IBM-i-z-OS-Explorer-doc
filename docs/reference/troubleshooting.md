# Troubleshooting

!!! tip "Always look at the log first"
    **View → Output** → **IBM i & z/OS**. Every request and every error is written there.

## Connecting

| Symptom | Cause | Fix |
|---|---|---|
| `ENOENT: no such file or directory, open '…\Microsoft VS Code\<text>'` | Text was typed where an SSH key **file** was expected (early pre-release builds only) | **Edit Connection** → choose **Password** |
| `SSH key file not found` | Key file moved or wrong | **Edit Connection** → pick the key file again, or choose **Password** |
| `All configured authentication methods failed` / `401` | Wrong or expired password | Right-click → **Reset Stored Password** |
| `ECONNREFUSED` | Service not started or wrong port | IBM i: `STRTCPSVR *SSHD`. z/OS: check that z/OSMF is up and the port is right. |
| `ETIMEDOUT` / `Timed out while waiting for handshake` | Network, VPN or firewall | Connect the VPN; test with `ssh user@host` or open `https://host:port/zosmf/info` in a browser |
| `self signed certificate` | Internal certificate on z/OSMF | **Edit Connection** → **Accept self-signed certificate** |
| `Password entry cancelled` | The password prompt was closed | Run the action again and enter the password |

## IBM i

| Symptom | Fix |
|---|---|
| Library list is empty | Your profile may lack `*USE` on the libraries; try **Enter library name(s) manually…** |
| `… in QSYS2 type *N not found` / SQL errors on tree nodes | IBM i older than 7.3, or the matching Db2 PTF group is missing |
| Member opens with `*** Error` / `CPYTOSTMF` failed | Check authority to the member and that `/tmp` (or `mainframe.ibmi.tempDir`) is writable |
| Characters wrong in a member | Keep `mainframe.ibmi.sourceCcsid` at `1208`; check the source file CCSID (should not be 65535) |
| Compile errors not in the Problems panel | The command must contain `OPTION(*EVENTF)`; RPG III / OPM compilers don't produce event files |
| SQL is slow | Install `db2util`: `yum install db2util` |
| Spooled file won't open | `CPYSPLF … TOFILE(*TOSTMF)` needs IBM i 7.3 or later and authority to the spooled file |

## z/OS

| Symptom | Fix |
|---|---|
| `403 Forbidden` | Ask for access to z/OSMF (`IZUUSER`) and the REST services |
| Save fails with `412` | The member changed on the host since you opened it. Choose **Overwrite**, or reopen it. |
| Migrated data set (cloud icon) | Click it to **recall** it, then refresh |
| TSO command never returns | Check `mainframe.zos.tsoAccount` / `tsoProc`; your account must be allowed to log on to TSO |
| National characters wrong | Set `mainframe.zos.encoding` (e.g. `IBM-037`, `IBM-273`, `IBM-297`, `IBM-1047`) |
| Job list shows only some jobs | Raise `mainframe.zos.maxItems`, or use a narrower job filter |

## New in 1.1

| Symptom | Fix |
|---|---|
| Compile can't find a `/COPY` member or file | Add its library to the [Library List](../ibmi/library-list.md), then compile again |
| Library list seems ignored | Run `DSPLIBL OUTPUT(*PRINT)` with **Run CL Command** to see the list actually used |
| IBM i search finds nothing | Check the search term; the search is plain text (no wildcards). For IFS, binary files are skipped. |
| z/OS search is slow | It reads every member: search one PDS instead of a whole filter, or cancel from the notification |
| Generated JCL fails with `PROCEDURE NOT FOUND` | Uncomment the `JCLLIB` line in the template and set your site's procedure library |
| `Reply…` fails with *already replied* | Refresh the message queue; answered inquiries no longer offer a reply |
| Upload Folder refuses to start | Two files would become the same member (e.g. `PGM1.cbl` and `PGM1.cpy`); rename one |

## Still stuck?

Open an issue at <https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer/issues>. Include:

- the extension version (**Extensions** → *IBM i & z/OS Explorer*);
- your VS Code version and operating system;
- the relevant lines from **Output → IBM i & z/OS**, with host names masked if needed (for example `xxxx`).
