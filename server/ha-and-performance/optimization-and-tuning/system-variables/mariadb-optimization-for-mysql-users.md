# MariaDB Optimization for MySQL Users

MariaDB contains many new options and optimizations which, for\
compatibility or other reasons, are not enabled in the default install.\
Enabling them helps you gain extra performance from the same hardware\
when upgrading from MySQL to MariaDB. This article contains information\
on options and settings which you should enable, or at least look in\
to, when making the switch.

```
aria-pagecache-buffer-size=##
```

If you are using a log of on-disk temporary tables, increase the above to as much as you can afford. See [Aria Storage Engine](../../../server-usage/storage-engines/aria/aria-storage-engine.md) for more details.

```
key-cache-segments=8
```

If you use/have a lot of MyISAM files, increase the above to 4 or 8. See [Segmented Key Cache](segmented-key-cache.md) and [Segmented Key Cache Performance](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/ySaANiCpRqROWwoll9yo) for more information.

```
thread-handling=pool-of-threads
```

Threadpool is a great way to increase performance in situations where queries are relatively short and the load is CPU bound (e.g. OLTP workloads). To enable it, add the above to your my.cnf file. See [Threadpool in 5.5](../buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
