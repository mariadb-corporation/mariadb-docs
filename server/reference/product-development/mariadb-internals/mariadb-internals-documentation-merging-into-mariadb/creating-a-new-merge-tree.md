---
description: >-
  Provides technical instructions on how to set up a new source tree
  specifically for the purpose of merging external updates into MariaDB.
---

# Creating a New Merge Tree

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

This article is obsolete. We don't use bzr anymore. This howto needs to be rewritten to explain how to create a merge tree in git.

**Merge tree** in the context of this HOWTO is a tree created specifically to simplify merges of third-party packages into MariaDB. WIth a merge tree there's a clear separation between upstream changes and our changes and in most cases bzr can do the merges automatically.

Here's how I created a merge tree for pcre:

* prerequisites: we already have pcre in the MariaDB tree, together with our changes (otherwise one can trivially create a bzr repository out of source pcre tarball).
* create an empty repository:

```
mkdir pcre
cd pcre
bzr init
```

* download pcre source tarball of the same version that we have in the tree — `pcre-8.34.tar.bz2`
* unpack it in the same place where the files are in the source tree:

```
tar xf ~/pcre-8.34.tar.bz2
mv pcre-8.34 pcre
```

* Add files to the repository with the same file-ids as in the MariaDB tree!

```
bzr add --file-ids-from ~/Abk/mysql/10.0
```

* All done. Commit and push

```
bzr commit -m pcre-8.34
bzr push --remember lp:~maria-captains/maria/pcre-mergetree
```

* Now null-merge that into your MariaDB tree. Note, that for the initial merge you need to specify the revision range `0..1`

```
cd ~/Abk/mysql/10.0
bzr merge -r 0..1 ~/mergetrees/pcre/
```

* Remove pcre files that shouldn't be in MariaDB tree, revert all changes that came from pcre (remember — it's a null-merge, pcre-8.34 is already in MariaDB tree), rename files in place as needed, resolve conflicts:

```
bzr rm `bzr added`
bzr revert --no-backup `bzr modified`
bzr resolve pcre
```

* Verify that the tree is unchanged and commit:

```
bzr status
bzr commit -m 'pcre-8.34 mergetree initial merge'
```

* Congratulations, your new merge tree is ready!

Now see [Merging with a merge tree](merging-with-a-merge-tree.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
