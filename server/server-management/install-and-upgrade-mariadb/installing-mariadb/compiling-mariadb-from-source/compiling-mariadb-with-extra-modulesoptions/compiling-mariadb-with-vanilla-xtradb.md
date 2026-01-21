---
description: >-
  A guide for compiling older versions of MariaDB (specifically 5.3) with the
  original XtraDB engine from Percona Server, useful for testing purposes.
---

# Compiling MariaDB with Vanilla XtraDB

Sometimes, one needs to have MariaDB compiled with Vanilla XtraDB. This page describes the process to do this. The process is rather crude, as my goal was just a once-off compile for testing (that is, not packaging or shipping) purposes.

The process is applicable to [MariaDB 5.3.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/mariadb-534-release-notes) and XtraDB from Percona Server 5.1.61.

```bash
wget http://s.petrunia.net/scratch/make-vanilla-xtradb-work-with-mariadb.diff

bzr branch /path/to/mariadb-5.3 5.3-vanilla-xtradb-r3

cd 5.3-vanilla-xtradb-r3/storage/
tar czf innodb_plugin.tgz innodb_plugin/
rm -rf innodb_plugin
tar czf xtradb.tgz xtradb/
rm -rf xtradb
cd ../../

tar zxvf ~/Percona-Server-5.1.61.tar.gz
cp -r Percona-Server-5.1.61/storage/innodb_plugin 5.3-vanilla-xtradb-r3/storage/
patch -p1 -d 5.3-vanilla-xtradb-r3/storage/innodb_plugin/ < make-vanilla-xtradb-work-with-mariadb.diff

cd 5.3-vanilla-xtradb-r3/

BUILD/autorun.sh
./configure --with-plugin-innodb_plugin
make
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
