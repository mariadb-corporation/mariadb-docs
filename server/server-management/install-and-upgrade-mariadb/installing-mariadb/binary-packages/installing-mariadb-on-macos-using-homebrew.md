---
description: >-
  How to install MariaDB Server on macOS using the Homebrew package manager,
  including starting the service and securing the installation.
---

# Installing MariaDB on macOS

MariaDB Server is available for installation on macOS via the [Homebrew](https://brew.sh/) package manager. MariaDB Server (together with many client programs and helper tools) is available as a Homebrew "bottle", a precompiled package. If you haven't yet installed Homebrew, [see this section](installing-mariadb-on-macos-using-homebrew.md#homebrew-installation).

## Installing & Starting MariaDB

Install MariaDB Server:

```bash
brew install mariadb
```

{% hint style="info" %}
This can take several minutes to complete, depending on hardware, network, and other factors.
{% endhint %}

Start MariaDB Server:

```bash
mysql.server start
```

Alternatively, and strongly recommended, automatically start MariaDB Server:

```bash
brew services start mariadb
```

{% hint style="info" %}
Automatically starting MariaDB server installs a background service on macOS. Make sure to allow adding that background service. See [this section](installing-mariadb-on-macos-using-homebrew.md#macos-background-service) for more information.
{% endhint %}

## Connecting to MariaDB Server

After MariaDB Server has started, you can connect to the server using the shell user name (see [this section](installing-mariadb-on-macos-using-homebrew.md#terminal-user-and-mariadb-user) for information on the user):

```bash
mariadb
```

Alternatively, connect as root:

```bash
sudo mysql -u root
```

For graphical clients you can use instead of the `mariadb` command-line client, see [this section](installing-mariadb-on-macos-using-homebrew.md#graphical-clients).

## Upgrading MariaDB

Update Homebrew packages:

```bash
brew update
```

Then upgrade MariaDB Server:

```bash
brew upgrade mariadb
```

## Notes & Further Information

### Homebrew Installation

Install Homebrew like this:

1. Open a Terminal (<kbd>⌘ + Space</kbd> to open _Spotlight_, type _Terminal_).
2. Issue this command:\
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`&#x20;
   1. Alternatively, use the package installer (`.pkg`; at the time of writing this, [https://github.com/Homebrew/brew/releases/download/5.0.4/Homebrew-5.0.4.pkg](https://github.com/Homebrew/brew/releases/download/5.0.4/Homebrew-5.0.4.pkg))
3. Refer to the [Homebrew website](https://brew.sh/) for more information, particularly to the [Homebrew documentation](https://docs.brew.sh/).

### MariaDB Configuration

In Homebrew, the configuration file for MariaDB is located at:

* &#x20;`/usr/local/etc/my.cnf` for Intel-based Macs.
* `/opt/homebrew/etc/my.cnf` for Apple Silicon Macs (ARM architecture).

### MariaDB Information

Find information about the MariaDB version, analytics, and more, using the `brew info` command:

```shellscript
~> brew info mariadb
==> mariadb: stable 12.1.2 (bottled)
Drop-in replacement for MySQL
https://mariadb.org/
...
To restart mariadb after an upgrade:
  brew services restart mariadb
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mariadb/bin/mariadbd-safe --datadir\=/opt/homebrew/var/mysql
==> Analytics
install: 6,319 (30 days), 12,735 (90 days), 62,444 (365 days)
install-on-request: 6,291 (30 days), 12,670 (90 days), 62,137 (365 days)
build-error: 8 (30 days)
```

### MariaDB Programs

MariaDB Server (`mariadbd`), the MariaDB command-line client (`mariadb`), and many more clients and tools are installed in `/opt/homebrew/Cellar/mariadb` (for Apple Silicon Macs). Find the location for your machine, as well as the MariaDB programs installed, with these commands:

```shellscript
~> which mariadb
/opt/homebrew/bin/mariadb # in the next command, use this location to cd to
~> cd /opt/homebrew/bin/; ls -1 maria*
mariabackup
mariadb
mariadb-access
...
mariadbd
mariadbd-multi
mariadbd-safe
mariadbd-safe-helper
```

### Terminal User & MariaDB User

To find out which user is used, issue these commands in a shell like _Terminal_:

```shellscript
~> users
myuser
~> mariadb -e "SELECT USER()"
+------------------+
| USER()           |
+------------------+
| myuser@localhost |
+------------------+
```

### macOS Background Service

If you start MariaDB automatically, a macOS background service is added. You can find the MariaDB background service in <kbd>System Settings > General > Login Items & Extensions</kbd>. It's named `mariadbd-safe`.

<div align="left"><figure><img src="../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure></div>

The toggle switch allows you to turn off the automatic start of MariaDB. This prevents MariaDB Server from automatically starting once you reboot macOS.

To review the resource usage of MariaDB Server, use this command (type `q` to exit `top`when done):

```shellscript
top -pid $(pgrep mariadbd)
```

### Graphical Clients

MariaDB doesn't offer graphical clients for working with MariaDB Server, but there are [many third-party graphical clients](../../../../clients-and-utilities/graphical-and-enhanced-clients/), some of which run on macOS. One of those is [Beekeeper Studio](../../../../clients-and-utilities/graphical-and-enhanced-clients/beekeeper-studio.md), a subscription-based client that has a (not too) [limited free version](https://www.beekeeperstudio.io/get), though.

Assuming a standard Homebrew installation of MariaDB, and assuming you connect to MariaDB Server [using the standard shell user](installing-mariadb-on-macos-using-homebrew.md#terminal-user-and-mariadb-user), configure Beekeeper Studio like this:

* Connection type: MariaDB
* Authentication method: Username/Password
* Connection mode: Socket
* Socket path: `/tmp/mysql.sock`
* Username: (name of the shell user, without the `@localhost` suffix)

<div align="left"><figure><img src="../../../../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure></div>

Once connected to MariaDB Server, you can run queries in Beehive Studio:

<figure><img src="../../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

The query shown in this screenshot uses a MariaDB sample database called _nation_ which you can use to get familiar with MariaDB. See [this section](installing-mariadb-on-macos-using-homebrew.md#mariadb-sample-database) for more information.

### MariaDB Sample Database

MariaDB offers a sample database you can use to get familiar with using MariaDB. You can download it here: [https://mariadbtutorial.com/wp-content/uploads/2019/10/nation.zip](https://mariadbtutorial.com/wp-content/uploads/2019/10/nation.zip)

Unzip `nation.zip`, then import the database into MariaDB Server, using this command (assuming you downloaded and unzipped the sample database in the `Downloads` folder):

```shellscript
mariadb < Downloads/nation.sql
```

When done, use that database in the `mariadb` command-line client, like this:

```shellscript
~> mariadb nation
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 14
Server version: 12.1.2-MariaDB Homebrew

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [nation]> SHOW TABLES;
+-------------------+
| Tables_in_nation  |
+-------------------+
| continents        |
| countries         |
| country_languages |
| country_stats     |
| guests            |
| languages         |
| region_areas      |
| regions           |
| vips              |
+-------------------+
9 rows in set (0.001 sec)
```

Alternatively, open the database in [a graphical client](installing-mariadb-on-macos-using-homebrew.md#graphical-clients).

## Building MariaDB Server from source

In addition to the "bottled" MariaDB Server package available from Homebrew, you can use Homebrew to build MariaDB from source. This is useful if you want to use a different version of the server or enable some different capabilities that are not included in the bottle package.

Two components not included in the bottle package are the CONNECT and OQGRAPH engines, because they have non-standard dependencies. To build MariaDB Server with these engines, you must first install `boost` and `judy`. Follow these steps to install the dependencies and build the server:

```bash
brew install boost judy
brew install mariadb --build-from-source
```

You can also use Homebrew to build and install a pre-release version of MariaDB Server. Use this command to build and install a "development" version of MariaDB Server:

```bash
brew install mariadb --devel
```

## Other resources

* [mariadb.rb on github](https://github.com/Homebrew/homebrew-core/blob/master/Formula/m/mariadb.rb)
* [MariaDB Server on macOS: Does it even make sense to try?](https://www.youtube.com/watch?v=VoAPP6GDyYw) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
