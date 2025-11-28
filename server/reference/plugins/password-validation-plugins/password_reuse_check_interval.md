---
description: >-
  This system variable defines the retention period in days for the password
  history used by the Password Reuse Check Plugin to prevent reuse.
---

# password\_reuse\_check\_interval Variable

The `password_reuse_check_interval` system variable is available when the [password\_reuse\_check plugin](password-reuse-check-plugin.md) is installed. It determines the retention period for the password history in days. Zero, the default, means that passwords are never discarded.

* Command line: `--password_reuse_check_interval=#`
* Scope: Global
* Read-only: No
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `36500`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
