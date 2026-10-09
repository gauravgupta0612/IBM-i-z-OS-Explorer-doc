# z/OSMF setup (for system programmers)

The z/OS side of the extension talks **only** to z/OSMF REST services. It installs nothing on z/OS. This page lists what has to be in place, and how to check it.

!!! note "Audience"
    This page is for the **z/OS system programmer** and **security administrator**. Developers can send them the link.

## Services used

| Feature in the extension | z/OSMF service | URL prefix |
|---|---|---|
| Data sets, members, copy, rename, search, download | z/OS data set and file REST interface | `/zosmf/restfiles/ds` |
| USS files | z/OS data set and file REST interface | `/zosmf/restfiles/fs` |
| Jobs, spool, submit, cancel, purge, job JCL | z/OS jobs REST interface | `/zosmf/restjobs/jobs` |
| TSO commands | TSO/E address space services | `/zosmf/tsoApp/tso` |
| MVS console commands | z/OS console services | `/zosmf/restconsoles/consoles` |
| Connection test | z/OSMF information | `/zosmf/info` |

Every request uses HTTPS with Basic authentication (user ID and password or passphrase) and the header `X-CSRF-ZOSMF-HEADER: true`. No browser is involved, so CORS settings don't matter.

## Checklist

### z/OSMF server

- [ ] The z/OSMF started tasks are running (by default the angel `IZUANG1` and the server `IZUSVR1`). The server is ready when message `CWWKF0011I` appears.
- [ ] Note the HTTPS port (message `IZUG349I` in the log; often 443 or 10443). Developers enter it in the connection wizard.
- [ ] The server certificate is trusted by the developers' PCs, **or** developers choose *Accept self-signed certificate*. A certificate signed by your internal CA is better.

### Users

- [ ] Each developer's user ID is connected to the z/OSMF user group (default **`IZUUSER`**), created by the IBM-supplied security setup jobs (IZUSEC / IZUAUTH, depending on the release).
- [ ] Each developer has an **OMVS segment** (for USS access) and a **TSO segment** (for TSO commands).

### Data set and file REST interface

- [ ] The CEA started task is running and has the **TRUSTED** attribute (RACF).
- [ ] `COMMON_TSO` is configured in `IZUPRMxx`, and the z/OSMF user group is authorized to its logon procedure and account number.
- [ ] The logon procedure region is large enough (at least 65536 KB is commonly recommended).
- [ ] `IPCMSGQBYTES` in `BPXPRMxx` is at least 20971520.

### Jobs REST interface

- [ ] Developers can submit jobs, and are allowed to view and purge their own jobs through JESSPOOL / JESJOBS rules. To see other users' jobs (job filter owner `*`), they need the matching `JESSPOOL` access.

### TSO/E address space services

- [ ] The account number and logon procedure developers use are valid for them. In the extension these are the settings `mainframe.zos.tsoAccount` (default `ACCT#`) and `mainframe.zos.tsoProc` (default `IKJACCNT`). Tell developers the right values.

### Console services

- [ ] The `OPERCMD` class is active and MVS commands are protected (`MVS.**`).
- [ ] Developers who may use console commands have access to `MVS.MCSOPER.<userid>` and to the commands they need, for example `MVS.DISPLAY.**` for display commands only.

## Verify from a browser

Log in with a developer's user ID:

| URL | Expected |
|---|---|
| `https://<host>:<port>/zosmf/info` | JSON with `zosmf_version` |
| `https://<host>:<port>/zosmf/restjobs/jobs?owner=<USERID>` | JSON list of the user's jobs |
| `https://<host>:<port>/zosmf/restfiles/ds?dslevel=<USERID>.*` | JSON list of data sets |

## Verify from the extension

| Action | Expected result |
|---|---|
| **Test Connection** | *Connected to z/OS … (z/OSMF …)* |
| Expand **Data Sets** | The user's data sets |
| **Issue TSO Command** `TIME` | The current time |
| **Issue MVS Console Command** `D T` | `IEE136I LOCAL: TIME=…` |

## Typical errors

| Error in the extension | Usual cause |
|---|---|
| `401` | Wrong password, revoked user, or the user isn't in the z/OSMF user group |
| `403` on one service only | The user lacks authority for that service (TSO, console, JES) |
| TSO command hangs or returns nothing | Wrong account or logon procedure, or CEA / COMMON_TSO not set up |
| Console command returns `IEE345I … AUTHORITY INVALID` | Missing `OPERCMD` access |
| `self signed certificate` | Certificate not trusted; use an internal-CA certificate, or have developers accept it |

For the exact RACF statements, see IBM's *z/OSMF Configuration Guide* for your z/OS release, and the Zowe documentation on [configuring z/OSMF security](https://docs.zowe.org/stable/user-guide/cli-install-configure-zosmf-security). The same z/OSMF setup serves Zowe and this extension.
