---
description: >-
  Explains the operational steps and commands required to execute a code merge
  using a pre-configured merge tree.
---

# Merging with a Merge Tree

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

If you have a [merge tree](creating-a-new-merge-tree.md), you merge into MariaDB as follows:

1. MariaDB merge trees are in the [mergetrees](https://github.com/MariaDB/mergetrees) repository. Add it as a new remote:

```
git remote add merge https://github.com/MariaDB/mergetrees
```

1. Check out the branch you want to update and merge, for example:

```
git checkout merge-innodb-5.6
```

1. delete everything in the branch
2. download the latest released source tarball, unpack it, copy files into the repository:

* for InnoDB-5.6: use the content of the `storage/innobase/` of the latest MySQL 5.6 source release tarball.
* for performance schema 5.6: use `storage/perfschema`, `include/mysql/psi`, `mysql-test/suite/perfschema`, and `mysql-test/suite/perfschema_stress` from the latest MySQL 5.6 source release tarball.
* for SphinxSE: use `mysqlse/` subdirectory from the latest Sphinx source release tarball.
* for XtraDB: use the content of the `storage/innobase/` of the latest Percona-Server source release tarball (5.5 or 5.6 as appropriate).
* for pcre: simply unpack the latest pcre release source tarball into the repository, rename `pcre-X-XX/` to `pcre`.

1. Now `git add .`, `git commit` (use the tarball version as a comment), `git push`
2. merge this branch into MariaDB
3. Sometimes after a merge, some changes may be needed:

* for performance schema 5.6: update `storage/perfschema/ha_perfschema.cc`, plugin version under `maria_declare_plugin`.
* for InnoDB-5.6: update `storage/innobase/include/univ.i`, setting `INNODB_VERSION_MAJOR`, `INNODB_VERSION_MINOR`, `INNODB_VERSION_BUGFIX` to whatever MySQL version you were merging from.
* for XtraDB-5.5: update `storage/xtradb/include/univ.i`, setting `PERCONA_INNODB_VERSION`, `INNODB_VERSION_STR` to whatever Percona-Server version you were merging from.
* for XtraDB-5.6: update `storage/xtradb/include/univ.i`, setting `PERCONA_INNODB_VERSION`, `INNODB_VERSION_MAJOR`, `INNODB_VERSION_MINOR`, `INNODB_VERSION_BUGFIX` to whatever Percona-Server version you were merging from.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
