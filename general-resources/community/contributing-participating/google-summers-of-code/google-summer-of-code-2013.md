# Google Summer of Code 2013

We participated in Google Summer of Code 2013. MariaDB and the MariaDB Foundation believes we are making a better database that remains a drop-in replacement to MySQL. We also work on making LGPL connectors (currently in C, Java, C++ in development) and we also work on MariaDB Galera Cluster which allows you to scales your reads & writes.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Or subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers). Or both.

Please keep in mind that in April we travel a lot (conferences, busy time), so if you have a question and nobody on IRC answers — do not feel disappointed, ask in an email to maria-developers@lists.launchpad.net.

### LDAP authentication plugin

We would like the authentication system to be able to authenticate against a LDAP Directory Server.

See [pluggable authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview).

Skills: C, working knowledge of LDAP

Mentor: Sergei Golubchik

### Kerberos authentication plugin

_this project is taken_

Kerberos is a security mechanism used in a lot of financial institutions. A MySQL plugin that allows authentication against Kerberos is the goal here.

See [pluggable authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview).

Skills: C/C++, working knowledge of Kerberos

Mentor: Sergei Golubchik

### Active Directory authentication plugin

The Microsoft Windows world is all about Active Directory and upstream MySQL Enterprise already has this feature (though its a paid offering). It would be great to have an open source equivalent.

See [pluggable authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview).

Skills: C/C++, working knowledge of Active Directory/SAMBA, Windows-based development environment

Mentor: Sergei Golubchik, Vladislav Vaintroub

### Keystone authentication plugin

Keystone is the OpenStack Identity Service. The idea would be to ensure that MariaDB can authenticate to Keystone directly.

Skills: Python, C/C++

Mentor: Mark Riddoch

### Regex enhancements

_this project is taken_

MySQL and MariaDB use an old regex library, it works bytewise, and thus only supports one byte character set. It needs to be replaced by a modern multi-byte character set aware regex library.

Additionally a much requested `REGEX_REPLACE` function should be implemented. (See also [mysql-udf-regexp](https://launchpad.net/mysql-udf-regexp) for some UDF code that could be used as a starting point for this)

Detailed task description: [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425)

Skills: C/C++

Mentor: Alexander Barkov

### Self-Tuning Optimizer

One of the reasons of bad query plans is inadequate cost estimation of individual operations. A cost of reading a row in one engine might be a lot higher than in some other, but optimizer cannot know it. Also, it uses hard-coded constants, assuming, for example, that evaluating a WHERE clause is 5 times cheaper than reading a row from a table.

Obviously, some kind of calibration procedure is needed to get these cost estimates to be relatively correct. It is not easy, because the estimates depend on the actual hardware where MariaDB is run (a cost of a row read is different on HD and SSD), and also — somewhat — on the application.

A simple and low-maintenance solution would be to use self-tuning cost coefficients. They measure the timing and adjust automatically to the configuration where MariaDB is run.

See [MDEV-350](https://jira.mariadb.org/browse/MDEV-350).

Skills: C/C++

Mentor: Sergei Golubchik

### Roles

_this project is taken_

Roles, close to SQL:2003 standard. See [MDEV-4397](https://jira.mariadb.org/browse/MDEV-4397).

Skills: C/C++

Mentor: Sergei Golubchik

### Potential list

suggested development

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
