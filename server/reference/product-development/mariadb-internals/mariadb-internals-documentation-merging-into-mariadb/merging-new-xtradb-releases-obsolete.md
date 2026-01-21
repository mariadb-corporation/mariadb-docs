---
description: >-
  Details the now-obsolete workflow for integrating updated releases of the
  XtraDB storage engine into MariaDB.
---

# Merging New XtraDB Releases (obsolete)

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

{% hint style="info" %}
**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.
{% endhint %}

### Background

Percona used to maintain XtraDB as a patch series against the InnoDB plugin. This affected how we started merging XtraDB in.

Now Percona maintains a normal source repository on launchpad (`lp:percona-server`). But we continue to merge the old way to preserve the history of our changes.

### Merging

There used to be a `lp:percona-xtradb` tree, that we were merging from as:

```
bzr merge lp:percona-xtradb
```

Now we have to maintain our own XtraDB-5.5 repository to merge from. It is `lp:~maria-captains/maria/xtradb-mergetree-5.5`. Follow the procedures as described in [Merging with a merge tree](merging-with-a-merge-tree.md) to merge from it.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
