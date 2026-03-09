---
description: >-
  Outlines the workflow for contributing to MariaDB via GitHub, including branch
  management, pull requests, and coding standards for developers.
---

# Working with GitHub

{% include "../../../.gitbook/includes/this-page-contains-backgrou....md" %}

## Benefits of a Pull Request

A pull request created on GitHub provides visibility to the entire userbase on the changes that are occurring in MariaDB Server.

The pull request created automatically triggers the required Buildbot builds associated with it.

The created pull request is associated with a MariaDB Server branch where it is to be merged. There have been cases where a passing protected branch build has been incorrectly pushed to a former branch by mistake.

A pull request on GitHub can be reviewed, and those reviewing it might have valuable insight. By putting all the reviews in one location, reviewers can learn off each other and not repeat works already review. The reviews are there for future reference if additional though is requires as to why a particular change was made.

A pull request has a clear indicator of the reviews conducted, by who, and who you are expecting further reviews from.

When a developer with commit access, either the author or a reviewer has completed and passed a review, they can mark the pull request as auto-merge, enabling the pull request to be merge once the \[\[branch-protection-using-buildbot|protected branch builds] have passed.

## Mechanism of Creating a Pull Request

A pull request can be created on the MariaDB GitHub web page, [server](https://github.com/MariaDB/server), or any fork created using GitHub.

Alternately GitHub has an open source \[[|command](https://cli.github.com/|command) line client] that has RPM and Deb packages, and a static compiled executable. This is actively maintained.

### Creating a Branch

So to make a GitHub pull request you already have some code/changes that you have committed locally. Ideally, this will be on its own branch, rebased onto the MariaDB server branch where it is intended to merge.

A pull request starts from a public branch. You can either create a pull request from a public fork of the MariaDB Server, or if you have access, a branch on the MariaDB Server. Both will achieve the same outcome.

If you are creating on the MariaDB server, a branch name of the MDEV associated with the issue is recommended. If there are targetted branch names that need specific fixes, then prepending the target branch name to the newly created branch is recommended.

Previous documentation suggested a bb-\*prefix. This will trigger duplicate runs through Buildbot so your assistance in saving it some work would be appreciated.

This gives other server developers a reasonable visibility of to why the branch is there, a way to check if it can be deleted, and who to ask about in a single branch name.

### Creating a Pull Request

If you push with a command line client over a ssh transport remote, the output from GitHub will provide a link to create the pull request. This can be opened in your browser to complete the process.

To use the _gh cli_, use \[\[[gh\_pr\_create|](https://cli.github.com/manual/gh_pr_create|)`gh pr create`] to interactively create it, or use a variety of the command line options to increase the automation.

Common options you may wish to use:

* \--base BRANCH - the branch to commit to
* \--assignee GITHUB\_HANDLE - the primary person you wish to review this
* \--review GITHUB\_HANDLE - multiple people you wish to review this
* \--fill - to create the PR content base on your commit(s) in your branch
* \--draft - if you have a partial concept or unfinished work for a review. This gives a clear indication to not merge as is.
* \--label MariaDB\ Corporation - a label to make it easy to distinguish your affiliation to make the MariaDB Foundations job easier to identify external contributions.

### Wait for Review

While waiting for a review it might be possible that someone introduces changes in the code what conflict with your code. It might also be the case that you have some improvements to make. If this is the case, rebase or adjust your commits locally, and then _git push --force-with-lease_ to the same branch as before. This will automaticity update the pull request and retrigger buildbot.

### Examining Buildbot Results.

From the pull request number created, substitute that into the ID of the URL below will access all the builds based on that PR.

[grid?branch=refs%2Fpull%2FID%2Fmerge](https://buildbot.mariadb.org/#/grid?branch=refs%2Fpull%2FID%2Fmerge)

### Related Articles

(when they are written)

* Reviews
* Automerge
* Rebasing your PR on a different branch (quick version - rebase, force push and then edit the title of the PR to the base branch).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
