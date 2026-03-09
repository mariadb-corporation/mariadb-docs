---
description: >-
  Explains how to set up Git to automatically notify relevant mailing lists or
  systems when new commits are pushed to the repository.
---

# Configuring Git to Send Commit Notices

Commit emails for MariaDB are sent to [commits@lists.mariadb.org](https://lists.mariadb.org/postorius/lists/commits.lists.mariadb.org/). You can find the archive [here](https://lists.mariadb.org/hyperkitty/list/commits@lists.mariadb.org/).

To allow others to see what you are working on in your MariaDB tree:

1. [subscribe](https://lists.askmonty.org/cgi-bin/mailman/listinfo/commits) to the email list
2. configure git to send your commits to [commits@mariab.org](https://lists.askmonty.org/cgi-bin/mailman/listinfo/commits).

Download the [post-commit git trigger](https://bazaar.launchpad.net/~maria-captains/mariadb-tools/trunk/view/head:/git_template/hooks/post-commit) script. Configure as:

```bash
git config --global hooks.postcommitrecipients "commits@mariadb.org"
git config --global hooks.postcommitbranches "*"
```

Also you might want to check the [README](https://bazaar.launchpad.net/~maria-captains/mariadb-tools/trunk/view/head:/git_template/README) for the post-commit trigger.

The post-commit git trigger uses _sendmail_ for sending emails. Some platforms don't have _sendmail_ and then you'll need to modify to make use of something that is supported.

Also, the post-commit trigger is just one approach. You can also use git-email on at least Debian and Fedora to send commit emails to the MariaDB commits email list.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
