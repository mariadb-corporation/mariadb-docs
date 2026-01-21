---
description: >-
  Documents the legacy process previously used to incorporate upstream changes
  from MySQL into the MariaDB server.
---

# Merging from MySQL (obsolete)

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

{% hint style="info" %}
**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.
{% endhint %}

## Merging from MySQL into MariaDB

### Merging code changes from MySQL bzr repository

We generally merge only released versions of MySQL into MariaDB trunk. This is\
to be able to release a well-working release of MariaDB at any time, without\
having to worry about including half-finished changes from MySQL. Merges of\
MySQL revisions in-between MySQL releases can still be done (eg. to reduce the\
merge task to smaller pieces), but should then be pushed to the maria-5.1-merge\
branch, not to the main lp:maria branch.

The merge command should thus generally be of this form:

```
bzr merge -rtag:mysql-<MYSQL-VERSION> lp:mysql-server/5.1
```

As a general rule, when the MySQL and MariaDB side has changes with the same\
meaning but differing text, pick the MySQL variant when resolving this\
conflict. This will help reduce the number of conflicts in subsequent merges.

### Buildbot testing

To assist in understanding test failures that arise during the merge, we pull\
the same revision to be merged into the\
lp:maria-captains/maria/mysql-5.1-testing tree for buildbot test. This allows\
to check easily if any failures introduced are also present in the vanilla\
MySQL tree being merged.

### Helpful tags and diffs

To help keep track of merges, we tag the result of a merge:

```
mariadb-merge-mysql-<MYSQL-VERSION>
```

For example, when merging MySQL 5.1.39, the commit of the merge would be\
tagged like this:

```
mariadb-merge-mysql-5.1.39
```

The right-hand parent of tag:mariadb-merge-mysql-5.1.39 will be the revision\
tag:mysql-5.1.39. The left-hand parent will be a revision on the MariaDB\
trunk.

When merging, these tags and associated revisions can be used to generate some\
diffs, which are useful when resolving conflicts. Here is a diagram of the\
history in a merge:

```
B----maria------A0-------A1
 \              /       /
  \            /       /
   ---mysql---Y0------Y1
```

Here,

* `'B'` is the base revision when MariaDB was originally\
  branched from MySQL.
* `'A0'` is the result of the last MySQL merge, eg.`tag:mariadb-merge-mysql-5.1.38`.
* `'Y0'` is the MySQL revision that was last merged, eg.`tag:mysql-5.1.38`.
* `'Y1'` is the MySQL revision to be merged in the new merge,\
  eg. `tag:mysql-5.1.39`.
* `'A1'` is the result of committing the new merge, to be\
  tagged as eg. `tag:mariadb-merge-mysql-5.1.39`.

Then, these diffs can be useful:

* `'bzr diff -rY0..before:A1'` - this is the MariaDB side of changes to be merged.
* `'bzr diff -rY0..Y1'` - this is the MySQL side of changes to be merged.
* `'bzr diff -rA0..before:A1'` - these are the new changes on the MariaDB side to be merged; this can be useful do separate them from other MariaDB-specific changes that have already been resolved against conflicting MySQL changes.

### Merging documentation from MySQL source tarballs

The documentation for MySQL is not maintained in the MySQL source bzr\
repository. Therefore changes to MySQL documentation needs to be merged\
separately.

Only some of the MySQL documentation is available under the GPL (man pages,\
help tables, installation instructions). Notably the MySQL manual is not\
available under the GPL, and so is not included in MariaDB in any form.

The man pages, help tables, and installation instruction READMEs are obtained\
from MySQL source tarballs and manually merged into the MariaDB source trees.\
The procedure for this is as follows:

There is a tree on Launchpad used for tracking merges:

```
lp:~maria-captains/maria/mysql-docs-merge-base
```

(At the time of writing, this procedure only exists for the 5.1 series of MySQL\
and MariaDB. Additional merge base trees will be needed for other release\
series.)

This tree must **only** be used to import new documentation files from new\
MySQL upstream source tarballs. The procedure to import a new set of files when\
a new MySQL release happens is as follows:

* Download the new MySQL source tarball and unpack it, say to mysql-5.1.38
* run these commands:

```
T=../mysql-5.1.38
bzr branch lp:~maria-captains/maria/mysql-docs-merge-base
cd mysql-docs-merge-base
for i in Docs/INSTALL-BINARY INSTALL-SOURCE INSTALL-WIN-SOURCE support-files/MacOSX/ReadMe.txt scripts/fill_help_tables.sql $(cd "$T" && find man -type f | grep '\.[0-9]$' | grep -v '^man/ndb_' | grep -v '^man/mysqlman.1$') ; do cp "$T/$i" $i; bzr add $i ; done
bzr commit -m"Imported MySQL documentation files from $T"
bzr push lp:~maria-captains/maria/mysql-docs-merge-base
```

* Now do a normal merge from `lp:maria-captains/maria/mysql-docs-merge-base` into `lp:maria`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
