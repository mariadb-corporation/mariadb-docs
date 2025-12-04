# Storage Engine FAQ

### Are storage engines designed for MySQL compatible with MariaDB?

In most cases, yes. MariaDB tries to keep API compatibility with MySQL, even across major versions.

### Will storage engines created for MariaDB work in MySQL?

It will mostly work. It would need #ifdef's to adjust to MySQL-5.6 API, for example, for multi-read-range API, for table discovery API, etc. But most of the code will work as is, without any changes.

### Do storage engine binaries need to be recompiled for MariaDB?

Yes. You will need to recompile the storage engine against the exact version of MySQL or MariaDB you intend to run it on. This is due to the version of the server being stored in the storage engine binary, and the server will refuse to load it if it was compiled for a different version.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
