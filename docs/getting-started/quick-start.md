# Quick start

## 1. Open the view

Click the **IBM i & z/OS** icon in the activity bar. You see two sections: **z/OS** and **IBM i**.

## 2. Add a connection

=== "IBM i"

    1. Click **+** in the **IBM i** section title.
    2. Answer the prompts:

        | Prompt | Example |
        |---|---|
        | Connection name | `PROD400` |
        | Host name or IP | `myibmi.company.com` |
        | Port | `22` |
        | User profile | `GGUPTA` |
        | How do you sign in? | **Password** |

    3. The connection is tested straight away. Type your password when asked.

=== "z/OS"

    1. Click **+** in the **z/OS** section title.
    2. Answer the prompts:

        | Prompt | Example |
        |---|---|
        | Connection name | `SYSA` |
        | Host name or IP | `mvs.company.com` |
        | Port | `443` (or `10443`, ask your system programmer) |
        | User profile | `IBMUSER` |
        | Protocol | **HTTPS** |
        | TLS certificate | **Verify certificate**, or **Accept self-signed certificate** for internal certificates |

    3. The connection is tested straight away. Type your password when asked.

A message such as **"Connected to IBM i 7.5 …"** or **"Connected to z/OS 03.01.00 (z/OSMF …)"** confirms it works.

## 3. Explore

Expand the connection:

| z/OS | IBM i |
|---|---|
| **Data Sets**: one filter (`YOURID.*`) is added for you | **Libraries**: your own library is added for you |
| **Unix Files (USS)**: `/u/yourid` | **IFS**: `/home/YOURID` |
| **Jobs**: your own jobs | **Library List**: libraries for CL and compiles |
| | **My Spooled Files**, **My Active Jobs** and **Message Queues** |

Click any member or file to open it. Edit it, then press ++ctrl+s++ to save it **on the host**.

## 4. Try the main actions

- **z/OS:** open a JCL member and press ++ctrl+alt+s++ to submit it. Choose **Wait & Show Output** to see the spool when the job ends.
- **IBM i:** open an RPGLE member and press ++ctrl+e++ to compile it. Any errors appear in the **Problems** panel.
- **IBM i SQL:** right-click the connection → **Run SQL** and type `select * from qsys2.library_list_info`.
- **z/OS JCL from a template:** right-click a COBOL member → **Generate JCL from Template…** (see the [developer workflow](../zos/developer-workflow.md)).
- **Search:** right-click a PDS, source file or library → **Search Text…**.

## 5. Next steps

| You are… | Read |
|---|---|
| A z/OS developer | [z/OS developer workflow](../zos/developer-workflow.md) |
| An IBM i developer | [Library list](../ibmi/library-list.md) and [Compile](../ibmi/compile.md) |
| A z/OS system programmer | [z/OSMF setup](../zos/zosmf-setup.md) |
| Setting up a team | [Export and import connections](../reference/productivity.md#export-and-import-connections) |

!!! info "Where do I see what happened?"
    **View → Output** → choose **IBM i & z/OS** in the dropdown. Every request sent to the host is listed there, without passwords.
