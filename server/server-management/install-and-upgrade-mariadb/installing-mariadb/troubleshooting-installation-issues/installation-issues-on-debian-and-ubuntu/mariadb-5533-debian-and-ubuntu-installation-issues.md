---
description: >-
  Specific instructions for resolving dependency breakage that occurred with the
  release of MariaDB 5.5.33 on Debian and Ubuntu systems.
---

# MariaDB 5.5.33 Debian and Ubuntu Installation Issues

{% hint style="warning" %}
This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.
{% endhint %}

Shortly after the [MariaDB 5.5.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes) release we became aware of some installation issues with the Debian and Ubuntu repositories. These issues were fixed in [MariaDB 5.5.33a](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533a-release-notes), but due to how apt works, steps need to be taken to solve the broken dependencies before upgrading.

We know of three scenarios when dependencies were broken. The steps to fix each of them are pretty much the same, only the list of broken dependencies and hence the list of packages to take care of them differs. The basic idea is to downgrade those certain packages to 5.5.32 temporarily before upgrading them to 5.5.33a.

If you ran into issues when moving from [MariaDB 5.5.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5532-release-notes) to [MariaDB 5.5.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533a-release-notes), look through each of the three scenarios to see which one applies to you and then follow the steps to apply that fix.

## Applying the fix

To get your system ready to apply the fix, do the following:

* Comment out the standard [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) repo in the `/etc/apt/sources.list` or `/etc/apt/sources.list.d/mariadb.repo` file (or wherever you have the repositories configured).
* Add a [MariaDB 5.5.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5532-release-notes) repository to the `sources.list`. The easiest way is to add the following. Just replace '`{os}`' and '`{dist}`' with the appropriate values.

```bash
deb http://ftp.osuosl.org/pub/mariadb/mariadb-5.5.32/repo/{os} {dist} main
```

For example, on Debian Wheezy the line would be:

```bash
deb http://ftp.osuosl.org/pub/mariadb/mariadb-5.5.32/repo/debian wheezy main
```

And on Ubuntu Raring the line would be:

```bash
deb http://ftp.osuosl.org/pub/mariadb/mariadb-5.5.32/repo/ubuntu raring main
```

* Then run '`sudo apt-get update`'
* Then '`sudo apt-get install`' the list of packages to downgrade as given in the applicable section below.
* Next, modify our sources.list to remove the 5.5.32 repo and switch back to the normal 5.5 repo
* Then '`sudo apt-get update`' to get things back to normal
* As a final optional step, once your normal mirror has at least [MariaDB 5.5.33a](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/mariadb-5533a-release-notes) you can '`sudo apt-get upgrade`' to upgrade. To check what version of MariaDB our mirror has, run the following command (after running '`sudo apt-get update`'):

```bash
apt-cache show mariadb-server | grep Version
```

## 5.5.32 server + 5.5.32 client upgraded to the initial (17 Sep 2013) release of 5.5.33

In this first scenario, both client and server were partially upgraded to 5.5.33 before the process aborted. The problem looks like this:

```
You might want to run 'apt-get -f install' to correct these.
The following packages have unmet dependencies:
 libmariadbclient18 : Depends: libmysqlclient18 (= 5.5.32+maria-1~wheezy) but 5.5.33+maria-1~wheezy is installed
 libmysqlclient18 : Depends: libmariadbclient18 (= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-client-5.5 : Depends: libmariadbclient18 (>= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-client-core-5.5 : Depends: libmariadbclient18 (>= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-server : Depends: mariadb-server-5.5 (= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-server-core-5.5 : Depends: libmariadbclient18 (>= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
```

To fix it, the following server and client packages need to be temporarily downgraded to 5.5.32 (replace '`wheezy`' with the name of whatever distribution you are using):

```bash
sudo apt-get install \
  libmysqlclient18=5.5.32+maria-1~wheezy \
  mariadb-client-5.5=5.5.32+maria-1~wheezy \
  mariadb-client-core-5.5=5.5.32+maria-1~wheezy \
  mariadb-server=5.5.32+maria-1~wheezy \
  mariadb-server-core-5.5=5.5.32+maria-1~wheezy
```

## 5.5.32 Galera server and 5.5.32 MariaDB client upgraded to 5.5.33

In this scenario, the client upgraded, but Galera-server did not. The problem looks like this:

```
The following packages have unmet dependencies:
 libmariadbclient18 : Depends: libmysqlclient18 (= 5.5.32+maria-1~wheezy) but 5.5.33+maria-1~wheezy is installed
 libmysqlclient18 : Depends: libmariadbclient18 (= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-client-5.5 : Depends: libmariadbclient18 (>= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
 mariadb-client-core-5.5 : Depends: libmariadbclient18 (>= 5.5.33+maria-1~wheezy) but 5.5.32+maria-1~wheezy is installed
```

To fix it, only the client packages need to be temporarily downgraded to 5.5.32 (replace wheezy with whatever your distribution is):

```bash
sudo apt-get install \
  libmysqlclient18=5.5.32+maria-1~wheezy \
  mariadb-client-5.5=5.5.32+maria-1~wheezy \
  mariadb-client-core-5.5=5.5.32+maria-1~wheezy
```

## 5.3.12 server + 5.3.12 client + 5.5.32 libmariadbclient18 upgraded to 5.5.33

In this scenario, only the library upgraded. The problem looks like this:

```
The following packages have unmet dependencies:
  libmariadbclient18: Depends: libmysqlclient18 (= 5.5.32+maria-1~lucid) but 5.5.33+maria-1~lucid is installed
  libmysqlclient18: Depends: libmariadbclient18 (= 5.5.33+maria-1~lucid) but 5.5.32+maria-1~lucid is installed
```

To fix it, the library needs to be downgraded to 5.5.32 (replace wheezy with your distribution):

```bash
sudo apt-get install \
  libmysqlclient=5.5.32+maria-1~wheezy \
  libmariadbclient=5.5.32+maria-1~wheezy
```

After switching back to the 5.5 repo, the libraries won't get upgraded, they will stay 5.5.32 until you upgrade the server to 5.5.33a.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
