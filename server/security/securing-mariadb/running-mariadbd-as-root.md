---
description: >-
  Understand the implications of running MariaDB Server as root. This section
  highlights security risks and provides guidance on configuring MariaDB Server
  to operate with less privileged user accounts.
---

# Running mariadbd as root

MariaDB should never normally be run as the system's root user (this is unrelated to the MariaDB root user). If it is, any user with the FILE privilege can create or modify any files on the server as root.

MariaDB will normally return the error **Fatal error: Please read "Security" section of the manual to find out how to run mariadbd as root!** if you attempt to run mariadbd as root. If you need to override this restriction for some reason, start mariadbd with the [user=root](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#--user) option.

Better practice, and the default in most situations, is to use a separate user, exclusively used for MariaDB. In most distributions, this user is called `mysql`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
