---
description: >-
  Provides technical instructions on how to set up a new source tree
  specifically for the purpose of merging external updates into MariaDB.
---

# Creating a New Merge Tree

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

A **merge tree** is a branch created specifically to simplify merges of third-party packages into MariaDB. It contains nothing but pristine upstream sources, laid out at the same paths they occupy in the MariaDB tree. That gives a clear separation between upstream changes and MariaDB changes, so that in most cases Git can merge new upstream releases automatically.

MariaDB merge trees live in the [mergetrees](https://github.com/MariaDB/mergetrees) repository. Each third-party package has its own branch, named `merge-<package>` — for example `merge-pcre`, `merge-zlib`, or `merge-innodb-5.7`. The branches are independent of each other and share no history.

Create a merge tree once per package. Afterwards, updating it for each new upstream release is a separate and much shorter procedure — see [Merging with a Merge Tree](merging-with-a-merge-tree.md).

## Prerequisites

The package should already be present in the MariaDB tree, together with any MariaDB changes to it. You also need to know which upstream release corresponds to the copy currently in the tree, because the merge tree must start from exactly that version. Starting from a different version makes the first real merge produce spurious conflicts.

## Creating the Branch

Clone the `mergetrees` repository and create an orphan branch for the package. An orphan branch starts with no history, which is what you want — the merge tree is not a variation of any other merge tree.

```
git clone https://github.com/MariaDB/mergetrees
cd mergetrees
git checkout --orphan merge-pcre
git rm -rf .
```

## Adding the Upstream Sources

Download the upstream source tarball of the same version that is already in the MariaDB tree, and unpack it so that the files sit at **the same paths they have in the MariaDB tree**. This layout is what lets Git match the files up during a merge, so it is the step that matters most.

```
tar xf ~/pcre-8.34.tar.bz2
mv pcre-8.34 pcre
```

Then commit, using the upstream version as the commit message, and push the branch:

```
git add .
git commit -m 'pcre-8.34'
git push --set-upstream origin merge-pcre
```

## Recording the Merge Base

The new branch now has to be connected to the MariaDB tree, so that later merges bring across only the upstream changes since this point. Do that with a **null merge** — a merge that records the ancestry without changing a single file.

In your MariaDB tree, add the merge tree repository as a remote:

```
git remote add merge https://github.com/MariaDB/mergetrees
git fetch merge
```

Then merge the new branch with the `ours` strategy, which keeps the MariaDB tree exactly as it is:

```
git merge --allow-unrelated-histories -s ours merge/merge-pcre
```

{% hint style="info" %}
`-s ours` is what makes this a null merge: the resulting commit has two parents but its content is identical to the MariaDB tree before the merge. `--allow-unrelated-histories` is required because the merge tree branch is an orphan.
{% endhint %}

Verify that nothing changed, then push:

```
git diff HEAD^1 --stat
```

The command produces no output if the merge was correctly a null merge. Use a commit message that identifies the package and the version, following the existing convention:

```
pcre-8.34 mergetree initial merge
```

The merge tree is now ready. From here on, use [Merging with a Merge Tree](merging-with-a-merge-tree.md) to pull in each new upstream release.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
