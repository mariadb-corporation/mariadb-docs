# Compression Plugins

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

Compressions plugins were added in a [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes) preview release.

The various MariaDB storage engines, such as [InnoDB](../../../server-usage/storage-engines/innodb/), [RocksDB](../../../server-usage/storage-engines/myrocks/), [Mroonga](../../../server-usage/storage-engines/mroonga/), can use different compression libraries.

Before [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes), each separate library would have to be compiled in order to be available for use, resulting in numerous runtime/rpm/deb dependencies, most of which would never be used by users.

From [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes), five additional MariaDB compression libraries (besides the default zlib) are available as plugins (note that these affect InnoDB and Mroonga only; RocksDB still uses the compression algorithms from its own library):

* bzip2
* lzma
* lz4
* lzo
* snappy

## Installing

Depending on how MariaDB was installed, the libraries may already be available for installation, or may first need to be installed as .deb or .rpm packages, for example:

```bash
apt-get install mariadb-plugin-provider-lz4
```

Once available, [install as a plugin](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md), for example:

```sql
INSTALL SONAME 'provider_lz4';
```

The compression algorithm can then be used, for example, in [InnoDB compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md):

```sql
SET GLOBAL innodb_compression_algorithm = lz4;
```

## Upgrading

When upgrading from a release without compression plugins, if a non-zlib compression algorithm was used, those tables will be unreadable until the appropriate compression library is installed. [mariadb-upgrade](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md) should be run. The `--force` option (to run [mariadb-check](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlcheck.md)) or `mariadb-check` itself will indicate any problems with compression, for example:

```
Warning  : MariaDB tried to use the LZMA compression, but its provider plugin is not loaded

Error    : Table 'test.t' doesn't exist in engine

status   : Operation failed
```

or

```
Error    : Table test/t is compressed with lzma, which is not currently loaded. 
  Please load the lzma provider plugin to open the table

error    : Corrupt
```

In this case, the appropriate compression plugin should be installed, and the server restarted.

## See Also

* [10.7 preview feature: Compression Provider Plugins](https://mariadb.org/10-7-preview-feature-provider-plugins/) (mariadb.org blog)
* Add zstd as a compression plugin - [MDEV-34290](https://jira.mariadb.org/browse/MDEV-34290)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
