# Building MariaDB on FreeBSD

It is relatively straightforward to build MariaDB from source on FreeBSD. When working with an individual host, you can use Ports to compile particular or multiple versions of MariaDB. When working with multiple hosts, you can use `Poudriere` to build MariaDB once, then serve it as a package to multiple FreeBSD hosts.

## Using Ports

The FreeBSD Ports Collection provides a series of `Makefiles` that you can use to retrieve source code, configure builds, install dependencies and compile software. This allows you to use more advanced releases than what is normally available through the package managers as well as enable any additional features that interest you.

In the event that you have not used Ports before on your system, you need to first fetch and extract the Ports tree. This downloads the Ports tree from FreeBSD and extracts it onto your system, placing the various Makefiles, patches and so on in the `/usr/ports/` directory.

```bash
# portsnap fetch extract
```

In the event that you have used Ports before on this system, run `Portsnap` again to download and install any updates to the Ports tree.

```bash
# portsnap fetch update
```

This ensures that you are using the most up to date release of the Ports tree that is available on your system.

### Building MariaDB from Ports

Once `Portsnap` has installed or updated your Ports tree, you can change into the relevant directory and install MariaDB. Ports for MariaDB are located in the `/usr/ports/databases/` directory.

```bash
$ ls /usr/ports/databases | grep mariadb
```

```
mariadb-connector-c
mariadb-connector-odbc
mariadb100-client
mariadb100-server
mariadb101-client
mariadb101-server
mariadb102-client
mariadb102-server
mariadb103-client
mariadb103-server
mariadb55-client
mariadb55-server
```

Note that FreeBSD treats the Server and Client as separate packages. The Client is a dependency of the Server, so you only need to build the Server to get both. It also provides a number of different versions. You can search the available ports from [Fresh Ports](https://www.freshports.org/databases). Decide what version of MariaDB you want to install, the change into the relevant directory. Once in the directory, run Make to build MariaDB.

```bash
# cd /usr/ports/databases/mariadb103-server
# make
```

In addition to downloading and building MariaDB, Ports also downloads and build any libraries on which MariaDB depends. Each port it builds will take you to a GUI window where you can select various build options. In the case of MariaDB, this includes various storage engines and specific features you need in your build.

Once you finish building the ports, install MariaDB on your system and clean the directory to free up disk space.

```bash
# make install clean
```

This installs FreeBSD on your server. You can now enable, configure and start the service as you normally would after installing MariaDB from a package.

## Using `Poudriere`

`Poudriere` is a utility for building FreeBSD packages. It allows you to build MariaDB from a FreeBSD Jail, then serve it as a binary package to other FreeBSD hosts. You may find this is particularly useful when building to deploy multiple MariaDB servers on FreeBSD, such as with Galera Cluster or similar deployments.

### Building MariaDB

Once you've configured your host to use `Jails` and `Poudriere`, initialize a jail to use in building packages and a jail for managing ports.

```bash
# poudriere jail -c -j package-builder -v 11.2-RELEASE
# poudriere ports -c -p local-ports
```

This creates two `jails`, `package-builder` and `local-ports`, which you can then use to build MariaDB. Create a text file to define the packages you want to build. Poudriere will build these packages as well as their dependencies. MariaDB is located at `databases/mariadb103-server`. Adjust the path to match the version you want to install.

```bash
$ vi maraidb-package-builder.txt
```

```
databases/mariadb103-server
```

Use the `options` command to initialize the build options for the packages you want Poudriere to compile.

```bash
# poudriere options -j package-builder -p local-ports -z mariadb-builder -f mariadb-package-builder.txt
```

Lastly, use the `bulk` command to compile the packages.

```bash
# poudriere bulk -j package-builder -p local-ports -z mariadb-builder -f mariadb-package-builder.txt
```

### Using Poudriere Repositories

In order to use Poudriere, you need to set up and configure a web server, such as `Nginx` or `Apache` to serve the directory that `Poudriere` built. For instance, in the case of the above example, you would map to the `package-builder` `jail`: `/usr/local/poudriere/data/packages/package-builder/`. 

You may find it useful to map this directory to a sub-domain, for instance `httpspkg.example.com` or something similar.

Lastly, you need to configure the FreeBSD hosts to use the `Poudriere` repository you just created. On each host, disable the FreeBSD official repositories and enable your `Poudriere` repository as an alternative.

```bash
# vi /usr/local/etc/pkg/repos/FreeBSD.conf
```

```
FreeBSD: {
      enabled: no
}
```

Then add the URL for your `Poudriere` repository to configuration file:

```bash
# vi /usr/local/etc/pkg/repos/mariadb.conf
```

```
custom: {
      url: "https://pkg.example.com",
      enabled: yes
}
```

You can then install MariaDB from `Poudriere` using the package manager.

```bash
# pkg install mariadb103-server
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
