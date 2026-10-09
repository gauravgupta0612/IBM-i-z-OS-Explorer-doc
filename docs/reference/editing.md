# Editing & languages

## Remote files in the editor

When you open a member, data set or file from the tree, VS Code edits it **directly on the host** through a virtual file system (`mf:` URIs):

| Source | Read with | Saved with ++ctrl+s++ |
|---|---|---|
| z/OS member / sequential data set | z/OSMF REST (text, optional code page) | z/OSMF REST, with an **ETag** conflict check |
| z/OS USS file | z/OSMF REST | z/OSMF REST |
| IBM i source member | `CPYTOSTMF` + SFTP | SFTP + `CPYFRMSTMF` |
| IBM i IFS file | SFTP | SFTP |

Spool files, IBM i spooled files and job logs open as **read-only** documents.

The editor tab title shows the member name with an extension, e.g. `HELLO.jcl` or `PAYROLL.rpgle`. The extension only selects the language; it isn't part of the real member name.

## Syntax highlighting

| Language | Highlights |
|---|---|
| **JCL** | `//` statements (JOB, EXEC, DD, PROC, SET, IF/THEN/ELSE, INCLUDE, JCLLIB…), keyword parameters (DSN, DISP, SPACE, DCB…), symbols (`&VAR`), comments `//*` |
| **RPGLE** | `**FREE`, `dcl-*` / `end-*`, op-codes, built-in functions (`%trim`…), special values (`*on`, `*blanks`…), fixed-format comments, compiler directives (`/copy`, `/if`…) |
| **CL** | Control commands (PGM, DCL, IF, DO, MONMSG, CALL…), variables (`&VAR`), operators (`*EQ`, `*CAT`…), `/* comments */` |
| **COBOL** | Divisions, sections, verbs, PIC/VALUE/OCCURS, level numbers, column 7 comments |

Comment toggling (++ctrl+slash++) and bracket matching work for all four languages.

## Tips

- **Compare with local:** right-click a remote editor tab → **Select for Compare**, then right-click a local file → **Compare with Selected**.
- **Save a local copy:** **File → Save As…** and pick a local folder.
- **Search inside a member:** ++ctrl+f++ works as usual.
- **Search across members on the host:** right-click a PDS or data set filter (z/OS), or a source file, library or IFS folder (IBM i) → **Search Text…**. See [Data sets](../zos/datasets.md#search-text) and [Libraries](../ibmi/libraries.md#search-text-in-source).
- **Snippets:** type a prefix such as `jobcard`, `program` or `dcl-proc` and press ++tab++ ([full list](../zos/jcl-templates.md#snippets)).
