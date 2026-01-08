---
description: >-
  Explains the MyISAM log (`myisam.log`), a specialized log for recording
  changes to MyISAM tables for debugging purposes, enabled via the `--log-isam`
  option.
---

# MyISAM Log

The MyISAM log records all changes to [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) tables. It is not enabled by default. To enable it, start the server with the [--log-isam](../starting-and-stopping-mariadb/mariadbd-options.md) option, for example:

```
--log-isam=myisam.log
```

The _isam_ instead of _myisam_ above is not a typo - it's a legacy from when the predecessor to the MyISAM format, called ISAM. The option can be used without specifying a filename, in which case the default, _myisam.log_ is used.

To process the contents of the log file, use the [myisamlog](../../clients-and-utilities/myisam-clients-and-utilities/myisamlog.md) utility.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
