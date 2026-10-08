---
description: >-
  Addresses compatibility issues between MariaDB and older PHP5 client
  libraries, specifically regarding header and library version mismatches.
---

# Installation Issues with PHP5

PHP5 may give an error if used with the old connect method:

```
'mysql_connect(): Headers and client library minor version mismatch. Headers:50156 Library:50206'
```

This is because the library wrongly checks and expects that the client library must be the exact same version as PHP was compiled with. You would get the same error if you tried to upgrade just the MySQL client library without upgrading PHP at the same time.

Ways to fix this issue:

1. Switch to using the [mysqlnd driver](https://dev.mysql.com/downloads/connector/php-mysqlnd/) in PHP (Recommended solution).
2. Run with a lower [error reporting level](https://php.net/error-reporting):

```php
$err_level = error_reporting(0);
$conn = mysql_connect('params');
error_reporting($err_level);
```

1. Recompile PHP with the MariaDB client libraries.
2. Use your original MySQL client library with the MariaDB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
