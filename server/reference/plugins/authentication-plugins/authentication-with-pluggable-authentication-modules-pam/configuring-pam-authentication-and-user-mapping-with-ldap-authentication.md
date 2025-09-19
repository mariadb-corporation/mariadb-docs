# Configuring PAM Authentication and User Mapping with LDAP Authentication

In this article, we will walk through the configuration of PAM authentication using the [pam](authentication-plugin-pam.md) authentication plugin and user and group mapping with the [pam\_user\_map](user-and-group-mapping-with-pam.md) PAM module. The primary authentication will be handled by the [pam\_ldap](https://linux.die.net/man/5/pam_ldap) PAM module, which performs LDAP authentication. We will also set up an OpenLDAP server.

## Hypothetical Requirements

In this walkthrough, we are going to assume the following hypothetical requirements:

* The LDAP user `foo` should be mapped to the MariaDB user `bar`. (`foo: bar`)
* Any LDAP user in the LDAP group `dba` should be mapped to the MariaDB user `dba`. (`@dba: dba`)

## Setting up the OpenLDAP Server

Before we can use LDAP authentication, we first need to set up our OpenLDAP Server. This is usually done on a server that is completely separate from the database server.

### Installing the OpenLDAP Server and Client Components

On the server acting as the OpenLDAP Server, first, we need to install the OpenLDAP components.

On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/), that would go like this:

```bash
sudo yum install openldap openldap-servers openldap-clients nss-pam-ldapd
```

### Configuring the OpenLDAP Server

Next, let's to configure the OpenLDAP Server. The easiest way to do that is to copy the template configuration file that is included with the installation. In many installations, that will be at `/usr/share/openldap-servers/DB_CONFIG.example`:

```bash
sudo cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
sudo chown ldap. /var/lib/ldap/DB_CONFIG
```

#### Configuring the OpenLDAP Port

Sometimes it is useful to change the port used by OpenLDAP. For example, some cloud environments block well-known authentication services, so they block the default LDAP port.

On some systems, the port can be changed by setting `SLAPD_URLS` in `/etc/sysconfig/slapd`:

```ini
SLAPD_URLS="ldapi:/// ldap://0.0.0.0:3306/"
```

I used `3306` because that is the port that is usually used by `mysqld`, so I know that it is not blocked.

### Starting the OpenLDAP Server

Next, let's start the OpenLDAP Server and configure it to start on reboot. On [systemd](../../../../server-management/starting-and-stopping-mariadb/systemd.md) systems, that would go like this:

```bash
sudo systemctl start slapd
sudo systemctl enable slapd
```

### Installing the Standard LDAP objectClasses

In order to use LDAP for authentication, we also need to install some standard `objectClasses`, such as `posixAccount` and `posixGroup`. In LDAP, things like `objectClasses` are defined in [LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system) files. In many installations, these specific `objectClasses` are defined in `/etc/openldap/schema/nis.ldif`. `nis.ldif` also depends on `core.ldif` and `cosine.ldif`. However, `core.ldif` is usually installed by default.

We can install them with [ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify\&sektion=1\&apropos=0\&manpath=OpenLDAP+2.4-Release):

```bash
sudo ldapmodify -a -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
sudo ldapmodify -a -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
```

### Creating the LDAP Directory Manager User

Next, let’s create a directory manager user. We can do this by using OpenLDAP's [olc](https://www.openldap.org/doc/admin24/slapdconf2.html) configuration system to change the [olcRootDN](https://www.openldap.org/doc/admin24/slapdconf2.html#olcRootDN:%20%3CDN%3E) directive to the DN of the directory manager user, which means that the user will be a privileged LDAP user that is not subject to access controls. We will also set the root password for the user by changing the [olcRootPW](https://www.openldap.org/doc/admin24/slapdconf2.html#olcRootPW:%20%3Cpassword%3E) directive.

We will also set the DN suffix for our backend LDAP database by changing the [olcSuffix](https://www.openldap.org/doc/admin24/slapdconf2.html#olcSuffix:%20%3Cdn%20suffix%3E) directive.

Let’s use the [slappasswd](https://www.openldap.org/software/man.cgi?query=slappasswd\&apropos=0\&sektion=8\&manpath=OpenLDAP+2.4-Release\&format=html) utility to generate a password hash from a clear-text password. Simply execute:

```bash
slappasswd
```

This utility provides a password hash that looks like this: `{SSHA}AwT4jrvmokeCkbDrFAnGvzzjCMb7bvEl`

OpenLDAP's [olc](https://www.openldap.org/doc/admin24/slapdconf2.html) configuration system also uses [LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system) files. Now that we have the password hash, let’s create an `LDIF` file to create the directory manager user:

```bash
tee ~/setupDirectoryManager.ldif <<EOF
dn: olcDatabase={1}monitor,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to * 
    by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth" read 
    by dn.base="cn=Manager,dc=support,dc=mariadb,dc=com" read 
    by * none

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=support,dc=mariadb,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootDN
olcRootDN: cn=Manager,dc=support,dc=mariadb,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcRootPW
olcRootPW: {SSHA}AwT4jrvmokeCkbDrFAnGvzzjCMb7bvEl

dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcAccess
olcAccess: {0}to attrs=userPassword,shadowLastChange 
    by   dn="cn=Manager,dc=support,dc=mariadb,dc=com" write 
    by anonymous auth 
    by self write 
    by * none
olcAccess: {1}to dn.base="" 
    by * read
olcAccess: {2}to * 
    by dn="cn=Manager,dc=support,dc=mariadb,dc=com" write 
    by * read
EOF
```

Note that this is using the `dc=support,dc=mariadb,dc=com` domain for the directory. You can change it to whatever is relevant to you.

Now let’s run the `ldif` file with [ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify\&sektion=1\&apropos=0\&manpath=OpenLDAP+2.4-Release):

```bash
sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f ~/setupDirectoryManager.ldif
```

We will use the new directory manager user to make changes to the LDAP directory after this step.

### Creating the Structure of the Directory

Next, let's create the structure of the directory by creating parts of our tree.

```bash
tee ~/setupDirectoryStructure.ldif <<EOF
dn: dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: dcObject
objectclass: organization
o: MariaDB Support Team
dc: support

dn: cn=Manager,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalRole
cn: Manager
description: Directory Manager

dn: ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: Groups

dn: ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: organizationalUnit
ou: System Users
EOF
```

Now, let’s use our new directory manager user and run the [LDIF](https://www.digitalocean.com/community/tutorials/how-to-use-ldif-files-to-make-changes-to-an-openldap-system) file with [ldapmodify](https://www.openldap.org/software/man.cgi?query=ldapmodify\&sektion=1\&apropos=0\&manpath=OpenLDAP+2.4-Release):

```
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/setupDirectoryStructure.ldif
```

### Creating the LDAP Users and Groups

Let's go ahead and create the LDAP users and groups that we are using for this scenario.

First, let's create the `foo` user:

```bash
tee ~/createFooUser.ldif <<EOF
dn: uid=foo,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: foo
uid: foo
uidNumber: 16859
gidNumber: 100
homeDirectory: /home/foo
loginShell: /bin/bash
gecos: foo
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createFooUser.ldif
```

Next, let's create a couple of users to go into the `dba` group:

```bash
tee ~/createDbaUsers.ldif <<EOF
dn: uid=gmontee,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: gmontee
uid: gmontee
uidNumber: 16860
gidNumber: 100
homeDirectory: /home/gmontee
loginShell: /bin/bash
gecos: gmontee
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0

dn: uid=bstillman,ou=People,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: bstillman
uid: bstillman
uidNumber: 16861
gidNumber: 100
homeDirectory: /home/bstillman
loginShell: /bin/bash
gecos: bstillman
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createDbaUsers.ldif
```

Note that each of these users needs a password, so we can set it for each user with [ldappasswd](https://www.openldap.org/software/man.cgi?query=ldappasswd\&apropos=0\&sektion=1\&manpath=OpenLDAP+2.4-Release\&format=html):

```
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=foo,ou=People,dc=support,dc=mariadb,dc=com
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=gmontee,ou=People,dc=support,dc=mariadb,dc=com
ldappasswd -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -S uid=bstillman,ou=People,dc=support,dc=mariadb,dc=com
```

Next, let's create our `dba` group:

```bash
tee ~/createDbaGroup.ldif <<EOF
dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: posixGroup
gidNumber: 678
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createDbaGroup.ldif
```

Next, let's add our two users to it:

```bash
tee ~/addUsersToDbaGroup.ldif <<EOF
dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
changetype: modify
add: memberuid
memberuid: gmontee

dn: cn=dba,ou=Groups,dc=support,dc=mariadb,dc=com
changetype: modify
add: memberuid
memberuid: bstillman
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/addUsersToDbaGroup.ldif
```

We also need to create LDAP users with the same name as the `bar` and `dba` MariaDB users. See [here](user-and-group-mapping-with-pam.md#pam-user-with-same-name-as-mapped-mariadb-user-must-exist) to read more about the reasons to do so. No one will be logging in as these users, so they do not need passwords. Instead of the `People` `organizationalUnit`, we create them in the `System Users` `organizationalUnit`.

```bash
tee ~/createSystemUsers.ldif <<EOF
dn: uid=bar,ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: bar
uid: bar
uidNumber: 16862
gidNumber: 100
homeDirectory: /home/bar
loginShell: /bin/bash
gecos: bar
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0

dn: uid=dba,ou=System Users,dc=support,dc=mariadb,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: dba
uid: dba
uidNumber: 16863
gidNumber: 100
homeDirectory: /home/dba
loginShell: /bin/bash
gecos: dba
userPassword: {crypt}x
shadowLastChange: -1
shadowMax: -1
shadowWarning: 0
EOF
ldapmodify -a -x -D cn=Manager,dc=support,dc=mariadb,dc=com -W -f ~/createSystemUsers.ldif
```

## Setting up the MariaDB Server

At this point, we can move on to setting up the MariaDB Server.

### Installing LDAP and PAM Libraries

First, we need to make sure that the LDAP and PAM libraries are installed.

On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/), we need to install the following packages:

```bash
sudo yum install openldap-clients nss-pam-ldapd pam pam-devel
```

### Configuring LDAP

Next, let's configure LDAP on the system. We can use [authconfig](https://linux.die.net/man/8/authconfig) for this:

```bash
sudo authconfig --enableldap \
   --enableldapauth \
   --ldapserver="ldap://172.30.0.238:3306" \
   --ldapbasedn="dc=support,dc=mariadb,dc=com" \
   --enablemkhomedir \
   --update
```

{% hint style="warning" %}
Be sure to replace `-–ldapserver` and `-–ldapbasedn` with values that are relevant for your environment.
{% endhint %}

### Installing the pam\_user\_map PAM Module

{% tabs %}
{% tab title="Current" %}
The `pam_user_map` PAM module is included in the base install. No installation is needed.
{% endtab %}

{% tab title="< 10.5.2 / 10.4.13 / 10.3.23 / 10.2.32.7" %}
Next, let's [install the pam\_user\_map PAM module](user-and-group-mapping-with-pam.md#installing-the-pam_user_map-pam-module).

Before the module can be compiled from source, we may need to install some dependencies.

On RHEL, CentOS, and other similar Linux distributions that use [RPM packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/), we need to install `gcc` and `pam-devel`:

```bash
sudo yum install gcc pam-devel
```

On Debian, Ubuntu, and other similar Linux distributions that use [DEB packages](../../../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files.md), we need to install `gcc` and `libpam0g-dev`:

```bash
sudo apt-get install gcc libpam0g-dev
```

And then we can build and install the library with the following:

```bash
wget https://raw.githubusercontent.com/MariaDB/server/10.4/plugin/auth_pam/mapper/pam_user_map.c 
gcc pam_user_map.c -shared -lpam -fPIC -o pam_user_map.so 
sudo install --mode=0755 pam_user_map.so /lib64/security/
```
{% endtab %}
{% endtabs %}

### Configuring the pam\_user\_map PAM Module

Next, let's [configure the pam\_user\_map PAM module](user-and-group-mapping-with-pam.md#configuring-the-pam_user_map-pam-module) based on our hypothetical requirements.

The configuration file for the `pam_user_map` PAM module is `/etc/security/user_map.conf`. Based on our requirements, ours would look like:

```
foo: bar
@dba:dba
```

### Installing the PAM Authentication Plugin

Next, let's [install the pam authentication plugin](authentication-plugin-pam.md#installing-the-plugin).

Log into the MariaDB Server and execute the following:

```sql
INSTALL SONAME 'auth_pam';
```

### Configuring the PAM Service

{% hint style="info" %}
For modern Linux distributions (like RHEL 8 and newer) that use SSSD (System Security Services Daemon) to connect to an LDAP provider, the `pam_sss.so` module is the modern equivalent of `pam_ldap.so`. In such a configuration, `pam_sss.so` replaces `pam_ldap.so`. For more information, please see the [Red Hat Enterprise Linux documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/configuring_authentication_and_authorization_in_rhel/understanding-sssd-and-its-benefits_configuring-authentication-and-authorization-in-rhel#how-SSSD-works_understanding-SSSD-and-its-benefits).
{% endhint %}

Next, let's [configure the PAM service](authentication-plugin-pam.md#configuring-the-pam-service). We will call our service `mariadb`, so our PAM service configuration file will be located at `/etc/pam.d/mariadb` on most systems.

#### Configuring PAM to Allow Only LDAP Authentication

Since we are only doing LDAP authentication with the [pam\_ldap](https://linux.die.net/man/5/pam_ldap) PAM module and group mapping with the `pam_user_map` PAM module, our configuration file would look like this:

```
auth required pam_ldap.so
auth required pam_user_map.so
account required pam_ldap.so
```

#### Configuring PAM to Allow LDAP and Local Unix Authentication

If we want to allow authentication from LDAP users **and** from local Unix users through [pam\_unix](https://linux.die.net/man/8/pam_unix), while giving priority to the local users, then we could do this instead:

```
auth [success=1 new_authtok_reqd=1 default=ignore] pam_unix.so audit
auth required pam_ldap.so try_first_pass
auth required pam_user_map.so
account sufficient pam_unix.so audit
account required pam_ldap.so
```

**Configuring the pam\_unix PAM Module**

If you also want to allow authentication from local Unix users, the `pam_unix` PAM module adds [some additional configuration steps](authentication-plugin-pam.md#configuring-the-pam-service) on a lot of systems. We basically have to give the user that runs `mysqld` access to `/etc/shadow`.

If the `mysql` user is running `mysqld`, then we can do that by executing the following:

```bash
sudo groupadd shadow
sudo usermod -a -G shadow mysql
sudo chown root:shadow /etc/shadow
sudo chmod g+r /etc/shadow
```

The server needs to be restarted for this change to take affect.

## Creating MariaDB Users

Next, let's [create the MariaDB users](authentication-plugin-pam.md#creating-users). Remember that our PAM service is called `mariadb`.

First, let's create the MariaDB user for the user mapping: `foo: bar`

That means that we need to create a `bar` user:

```sql
CREATE USER 'bar'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'bar'@'%' ;
```

And then let's create the MariaDB user for the group mapping: `@dba: dba`

That means that we need to create a `dba` user:

```sql
CREATE USER 'dba'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' ;
```

And then to allow for the user and group mapping, we need to [create an anonymous user that authenticates with the pam authentication plugin](user-and-group-mapping-with-pam.md#creating-users) that is also able to `PROXY` as the `bar` and `dba` users. Before we can create the proxy user, we might need to [clean up some defaults](../../../sql-statements/account-management-sql-statements/create-user.md#fixing-a-legacy-default-anonymous-account):

```sql
DELETE FROM mysql.db WHERE User='' AND Host='%';
FLUSH PRIVILEGES;
```

And then let's create the anonymous proxy user:

```sql
CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
GRANT PROXY ON 'bar'@'%' TO ''@'%';
GRANT PROXY ON 'dba'@'%' TO ''@'%';
```

## Testing our Configuration

Next, let's test our configuration by [verifying that mapping is occurring](user-and-group-mapping-with-pam.md#verifying-that-mapping-is-occurring). We can verify this by logging in as each of our users and comparing the return value of [USER()](../../../sql-functions/secondary-functions/information-functions/user.md), which is the original user name and the return value of [CURRENT\_USER()](../../../sql-functions/secondary-functions/information-functions/current_user.md), which is the authenticated user name.

### Testing LDAP Authentication

First, let's test our `foo` user:

```bash
$ mysql -u foo -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 134
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------+----------------+
| USER()                                         | CURRENT_USER() |
+------------------------------------------------+----------------+
| foo@ip-172-30-0-198.us-west-2.compute.internal | bar@%          |
+------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `foo` LDAP user was properly mapped to the `bar` MariaDB user by looking at the return value of [CURRENT\_USER()](../../../sql-functions/secondary-functions/information-functions/current_user.md).

Then let's test our `gmontee` user in the `dba` group:

```bash
$ mysql -u gmontee -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 135
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+----------------------------------------------------+----------------+
| USER()                                             | CURRENT_USER() |
+----------------------------------------------------+----------------+
| gmontee@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+----------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

And then let's test our `bstillman` user in the `dba` group:

```bash
$ mysql -u bstillman -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 136
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+------------------------------------------------------+----------------+
| USER()                                               | CURRENT_USER() |
+------------------------------------------------------+----------------+
| bstillman@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+------------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `gmontee` and `bstillman` LDAP users in the `dba` LDAP group were properly mapped to the `dba` MariaDB user by looking at the return values of `CURRENT_USER()`.

### Testing Local Unix Authentication

If you chose the option that also allowed local Unix authentication, then let's test that out. Let's create a Unix user and give the user a password real quick:

```bash
sudo useradd alice
sudo passwd alice
```

And let's also map this user to `dba`:

```
@dba:dba
foo: bar
alice: dba
```

And we know that the existing anonymous user already has the `PROXY` privilege granted to the `dba` user, so this should just work without any other configuration. Let's test it out:

```bash
$ mysql -u alice -h 172.30.0.198
[mariadb] Password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 141
Server version: 10.3.10-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SELECT USER(), CURRENT_USER();
+--------------------------------------------------+----------------+
| USER()                                           | CURRENT_USER() |
+--------------------------------------------------+----------------+
| alice@ip-172-30-0-198.us-west-2.compute.internal | dba@%          |
+--------------------------------------------------+----------------+
1 row in set (0.000 sec)
```

We can verify that our `alice` Unix user was properly mapped to the `dba` MariaDB user by looking at the return values of [CURRENT\_USER()](../../../sql-functions/secondary-functions/information-functions/current_user.md).

## Integrating with MariaDB MaxScale

If you are connecting to MariaDB Server through MariaDB MaxScale, it is also recommended to configure the proxy to authenticate users via [MaxScale PAM Authenticator](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-authenticators/maxscale-pam-authenticator).



<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
