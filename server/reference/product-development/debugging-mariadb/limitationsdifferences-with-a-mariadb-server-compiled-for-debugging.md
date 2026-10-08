---
description: >-
  Highlights the performance impacts and behavioral changes to expect when
  running a MariaDB server compiled with debug options.
---

# Limitations/Differences with a MariaDB Server Compiled for Debugging

{% include "../../../.gitbook/includes/hint-lower-level-development.md" %}

A MariaDB server configured with `--with-debug=full` has the following differences from a normal MariaDB server:

* You can have maximum of 1000 tables locked at the same time in one statement. (Define `MAX_LOCKS` in mysys/thrlock.c). This is to detect loops in the used lists.
* You can have maximum of 1000 threads locking the same table. (Define `MAX_THREADS` in mysys/thrlock.c). This is to detect loops in the used lists.
* Deadlock detection of mutex will be done at runtime. If wrong mutex handling is found an error will be printed to the error log. (Define `SAFE_MUTEX`)
* Memory overrun/underrun and not freed memory will be reported to the error log (Define `SAFEMALLOC`)
* You can get a trace of what `mysqld` (and most other binaries) is doing by starting it with the `--debug` option. The trace is usually put in `/tmp` or `C:\`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
