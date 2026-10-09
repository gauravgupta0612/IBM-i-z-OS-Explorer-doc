# z/OS connection

## What you need

| Item | Value / where to get it |
|---|---|
| **Host** | The z/OSMF host name, e.g. `mvs.company.com` |
| **Port** | The z/OSMF HTTPS port: often `443`, `10443` or `8443`. Ask your z/OS system programmer. |
| **User** | Your TSO/RACF user ID |
| **Password** | Your RACF password or passphrase, stored in the OS keychain |
| **Protocol** | **HTTPS** (HTTP only for test systems) |
| **Certificate** | **Accept self-signed certificate** if z/OSMF uses an internal or self-signed certificate |

## Prerequisites on z/OS

| Requirement | Notes |
|---|---|
| **z/OSMF** started | With the REST files, REST jobs, TSO/E address space and console services |
| **RACF access** | Your user ID must be allowed to use z/OSMF, usually through the `IZUUSER` group and the `IZUDFLT` profiles |
| **TSO account** *(TSO commands only)* | Set `mainframe.zos.tsoAccount` and `mainframe.zos.tsoProc` (see [Settings](../reference/settings.md)) |

!!! tip "Quick test from your browser"
    Open `https://<host>:<port>/zosmf/info`. It should return JSON with `zosmf_version`. If the browser warns about the certificate, choose **Accept self-signed certificate** in the wizard.

## The connection wizard

1. **Connection name**, e.g. `SYSA`
2. **Host name or IP**
3. **Port**
4. **User profile**
5. **Protocol**: HTTPS or HTTP
6. **TLS certificate**: *Verify certificate* or *Accept self-signed certificate*

Three things are added for you: a data set filter `YOURID.*`, a job filter (owner = you, prefix = `*`) and the USS path `/u/yourid`.

## What appears under the connection

| Node | Content |
|---|---|
| **Favorites** | Only when you have favorites: members, data sets and USS files starred with **Add to Favorites** |
| **Data Sets** | Your data set filters. Expand a filter to list data sets; expand a PDS/PDSE for members. Right-click for search, copy, rename, download, upload and attributes. |
| **Unix Files (USS)** | Your USS paths |
| **Jobs** | Your job filters. Expand for jobs, then for the spool files of a job. Right-click a job to view its JCL, resubmit, cancel or purge it. |

Next: the [z/OS developer workflow](../zos/developer-workflow.md) shows a full edit → compile → run cycle. If something doesn't work, send your system programmer the [z/OSMF setup](../zos/zosmf-setup.md) page.

## How it works

All calls use the z/OSMF REST APIs, with Basic authentication over HTTPS and the `X-CSRF-ZOSMF-HEADER` header:

| Function | z/OSMF service |
|---|---|
| Data sets / members | `/zosmf/restfiles/ds` |
| USS | `/zosmf/restfiles/fs` |
| Jobs / spool / submit / job JCL | `/zosmf/restjobs/jobs` |
| Copy / rename / attributes | `/zosmf/restfiles/ds` (`request: copy / rename`) |
| TSO | `/zosmf/tsoApp/tso` |
| Console | `/zosmf/restconsoles/consoles/defcn` |

## Common problems

| Message | Fix |
|---|---|
| `Authentication failed (401)` | Right-click → **Reset Stored Password**. Check that the RACF user isn't revoked. |
| `self signed certificate` / `unable to verify the first certificate` | **Edit Connection** → **Accept self-signed certificate** |
| `403` | Your user has no access to that z/OSMF service. Ask for `IZUUSER` access. |
| `ECONNREFUSED` / timeout | Wrong port, z/OSMF not started, or VPN or firewall |
| Garbled national characters | Set `mainframe.zos.encoding`, e.g. `IBM-037`, `IBM-297` or `IBM-1047` |
