---
description: >-
  Fix the file extensions of MyISAM table files with mariadb-fix-extensions
  (formerly mysql_fix_extensions).
---

# mariadb-fix-extensions

`mariadb-fix-extensions` converts the extensions for [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/server/clients-and-utilities/reference/storage-engines/myisam-storage-engine/README.md) (or ISAM) table files to their canonical forms.

{% hint style="info" %}
Previously, the client was called `mysql_fix_extensions`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

It looks for files with extensions matching any lettercase variant of `.frm`, `.myd`, `.myi`, `.isd`, and `.ism` and renames them to have extensions of `.frm`, `.MYD`, `.MYI`, `.ISD`, and `.ISM`, respectively. This can be useful after transferring the files from a system with case-insensitive file names (such as Windows) to a system with case-sensitive file names.

Invoke `mariadb-fix-extensions` as follows, where `data_dir` is the path name to the MariaDB data directory:

```bash
mariadb-fix-extensions data_dir
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
