---
description: >-
  Understand the implications of running MariaDB Server as root. This section
  highlights security risks and provides guidance on configuring MariaDB Server
  to operate with less privileged user accounts.
---

# Running MariaDB as root

MariaDB should never be run as the system root user (this is unrelated to the MariaDB root user). If it is, any user with the `FILE` privilege can create or modify any files on the server as root.

If you attempt to run the server (`mariadbd`) as root, MariaDB normally returns the error **Fatal error: Please read "Security" section of the manual to find out how to run mariadbd as root!**. If you need to override this restriction, start `mariadbd` with the [user=root](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#--user) option.

Better practice, and the default in most situations, is to use a separate user, exclusively used for MariaDB. In most distributions, this user is called `mysql`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
