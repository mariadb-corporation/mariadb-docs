---
description: >-
  Known restrictions of the MariaDB Jupyter Kernel include one SQL statement
  per cell, single line magic per cell, no mixing of magic and SQL, and
  required semicolon delimiters.
---

# MariaDB Jupyter Kernel Restrictions and Limitations

### Restrictions and Limitations

Here's a list of the current restrictions and limitations of the MariaDB Jupyter kernel. Trying to stretch what we listed here is at your own risk, the results and the behavior of the kernel might be at the mercy of the universe :-)

* One cell should only contain a single SQL statement. It can be multi-line, a one liner, it doesn't matter, but it needs to only be a single statement.
* A notebook cell can only contain one line magic command (line magics start with `%`). Everything else within the same cell below the line magic command will be ignored.
* [Magic commands](mariadb-jupyter-kernel-magic-commands.md) and SQL statements cannot be mixed within the same notebook cell.
* The kernel does not officially support the [DELIMITER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#delimiters) (MariaDB specific) client command. It might work, but it shouldn't be used. Rather use the `%%delimiter` cell magic command (see `%lsmagic` for usage information).
* Each SQL statement within a notebook cell should end with the `;` MariaDB default delimiter, except in cells using the `%%delimiter` cell magic command where it should end with the user-specified delimiter.

{% @marketo/form formId="4316" %}
