---
description: >-
  Common installation problems on Windows, such as issues with User Account
  Control (UAC) or unsupported Windows versions, and their solutions.
---

# Installation issues on Windows

## Unsupported Versions of Windows

Recent versions of MariaDB may not install on unsupported Windows versions. See [Deprecated Package Platforms](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/platform-deprecation-policy) to find the final supported versions.

## Systems with User Account Control

Running `mysql_install_db.exe` from a standard command prompt might cause the error:

```
FATAL ERROR: OpenSCManager failed
```

To get rid of it, use the elevated command prompt, for example on Windows 7 start it via 'Run as administrator' option.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
