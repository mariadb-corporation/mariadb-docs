---
description: >-
  How MariaDB is distributed through mirror sites, and how to volunteer your
  server as an official MariaDB mirror.
---

# Mirror Sites for MariaDB

We rely on mirrors to distribute MariaDB to the world through the official download site at [download](https://mariadb.org/download). If you would like to volunteer to become a mirror, thank you! Getting you set up is easy.

{% hint style="success" %}
The state of MariaDB mirrors is monitored at [https://mirmon.mariadb.org/](https://mirmon.mariadb.org/)
{% endhint %}

## How to Become a MariaDB Mirror

The only requirements for becoming a mirror are:
1. A willingness to mirror MariaDB;
1. Mirroring is done using rsync;
1. An https mirror should be utilised (http mirrors are not accepted any more);
1. Available bandwidth and disk space:

   - Each release of MariaDB takes about between 60-120GB of disk space for
     all of the various packages we create. There are several MariaDB releases
     per year, but only the most recent two from each main MariaDB series (as
     of November 2026 this is 10.6, 10.11, 11.4, 11.8, 12.3, 13.0, 13.1 and 13.2) are
     kept on the mirrors;
   - We recommend our mirrors have at least a 100Mbit/sec connection to the
     Internet.

1. The ability to do directory listings on mirrored sub-directories on your mirror host (for some platforms the [download](https://mariadb.org/download) page links directly to mirrored sub-directories);
1. The mirror should update itself, preferably every 6 hours, but at the very least, twice a day. (See [Updating Notes](mirror-sites-for-mariadb.md) for more information);
1. Not mandatory: provide `rsync` or `ftp` access to the mirror for our mirrorbits system (See: [Mirrorbits](https://mariadb.org/mirrorbits)).

### Updating Notes

MariaDB will normally have no more than one release per series (10.4, 10.5, etc...) per month. There may be times when this is not the case (such as if a major bug is found), but those times are few.

Timing for release announcements is generally oriented to the U.S. Eastern time zone. So if your mirror only updates less frequently than every 6 hours, have it update after midnight, but before 06:00, U.S. Eastern Time.

With rsync, it is no problem to update several times per day, and doing so is encouraged.

## rsync Information

The two primary rsync URLs for mirrors to use are:

USA:

```
rsync.osuosl.org::mariadb
```

Europe:

```
mirror.netcologne.de::mariadb
```

Here are suggested rsync commands for a mirror to use:

```
rsync -a --partial --delete-after --delay-updates mirror.netcologne.de::mariadb /path/to/local/download/directory/rsync_test
```

```
rsync -a --partial --delete-after --delay-updates rsync.osuosl.org::mariadb /path/to/local/download/directory/rsync_test
```

Be aware that when using the above rsync command, a "mariadb" directory **will not** be created. Instead, the contents of the mariadb module is rsynced into whatever local folder you specify. We suggest creating a "mariadb" folder for this.

It is also a good idea to test your rsync command before adding it to a cron job by adding the `-v --dry-run` flags to the command temporarily so you can see what it will do (without actually doing anything).

As of November 2026, running the above command will use around 640GB of disk space in total.

See the [rsync documentation](https://rsync.samba.org/documentation.html) for details on what each of the arguments in the command above does.

### Secondary rsync mirrors

We also have several secondary rsync mirrors you can pull from. In many instances pulling from the secondary mirror is faster than pulling from the primary rsync mirrors. Here they are, with the country they are located in. Simply replace the rsync URI in the example above with one from this list to use it.

The country sorted and actualized list of rsync mirrors can be found on https://mirmon.mariadb.org/.

### The MariaDB Foundation mirrorbits system

The MariaDB Foundation maintains a mirror manager system (see: [mirrorbits](https://mariadb.org/mirrorbits)). It is hosted by Hetzner in Germany, it is **not** available via `rsync` so you can't use it as a source for your mirror but you are encouraged to use it for your MariaDB installation and deployments. You can check the status of the service at https://mirror.mariadb.org/mirrorstats.

## Getting Added to the Mirror List

Once you have initially mirrored the MariaDB release tree, please send an email to (mirror (at) mariadb \[dot] org) with the following information:

1. The name of the company or organization sponsoring the mirror (so we can give credit where credit is due).
1. Contact name (and email address) for your mirror (so we know who to contact if there are any issues)
1. The general physical location (e.g. "Paris, France", "Hong Kong", or "Austin, Texas, USA") of the mirror (we use geolocation to try and send people to a mirror close to them).
1. The base public URL for the mirror (e.g. `'http://mirror.example.net/pub/mariadb'`).
1. The mirror you are using to rsync from

Once we receive your email and verify your mirror is working we'll add you to the list of mirrors. Apologies in advance in case of slow responses - mirror updates are usually batched around release time.

Thank you for volunteering to mirror MariaDB!

## Credits

The primary MariaDB mirrors have been generously provided by the [Oregon State University Open Source Lab](https://osuosl.org) (at rsync.osuosl.org) and [NetCologne](https://www.netcologne.de) (at mirror.netcologne.de).

Other mirrors are listed on https://mirmon.mariadb.org/ and can be selected on the [mariadb.org/download/](https://mariadb.org/download/) site.

## The MariaDB Archive

The distributed mirrors above only hold the most recent 3-4 releases of each MariaDB series (10.6, 10.11, etc...). If you need to access older MariaDB releases, there is an archive server that contains every MariaDB release. This server is available via the web at [archive.mariadb.org](https://archive.mariadb.org) and via rsync at:

```
archive.mariadb.org::mariadb
```

### Mirroring the MariaDB Archive with rsync

If you want to mirror the archive mirror, please contact us at mirror@mariadb.org in advance.

To mirror the archive with rsync, something like the following will get you everything:

```
rsync -avP archive.mariadb.org::mariadb/ /path/to/local/dir/
```

...or you can specify a specific release such as:

```
rsync -avP archive.mariadb.org::mariadb/mariadb-10.4.13/ /path/to/local/dir/
```

**Warning**, as of November 2026, the entire archive will use around 15 TB of disk space in total, and if you want to keep your mirror up to date (via cron routine for instance), please **first compare** the STATUS file **before** doing the rsync. This file is updated anytime a new content is added in the archive tree.

You can use something like the following:

```
rsync archive.mariadb.org::mariadb/STATUS /tmp/STATUS
diff -q /tmp/STATUS /path/to/local/dir/STATUS || rsync -avP archive.mariadb.org::mariadb/ /path/to/local/dir/
```

We reserve the right to block IPs that continually rsync the archive mirror when no new content was added, since it uselessly overloads the archive server, which uses a slow remote storage system.

To get a listing of the top level items in the archive including a list of every MariaDB release, just do:

```
rsync archive.mariadb.org::mariadb
```

If you would like to become a full archive mirror of MariaDB and be listed here, just let us know via the [contact information above](mirror-sites-for-mariadb.md#getting-added-to-the-mirror-list). Thanks!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
