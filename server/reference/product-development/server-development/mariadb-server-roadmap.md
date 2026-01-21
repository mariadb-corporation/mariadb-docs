---
description: >-
  Provides a high-level view of upcoming features, version release schedules,
  and the strategic direction for MariaDB Server development.
---

# MariaDB Server Roadmap

{% include "../../../.gitbook/includes/this-page-contains-backgrou....md" %}

This page talks in general about the MariaDB Server roadmap, and how it is formed.The roadmap it describes is located in our [JIRA](tools/jira.md) issue tracker: [**jira.mariadb.org**](https://jira.mariadb.org)

MariaDB was designed as a drop-in replacement of MySQL with more features, new storage engines, fewer bugs, and better performance. We aim to make upgrading from MySQL to MariaDB extremely easy.

The roadmap for MariaDB Server is formed by its engineers and product managers, with input from the community.

MariaDB Server developers work with several [storage engine](../../../server-usage/storage-engines/) vendors and developers to get the best storage engines into MariaDB Server.

The collected information is then turned into specific tasks which are then prioritized and added to the roadmap in the [JIRA](tools/jira.md) issue tracker at [**jira.mariadb.org**](https://jira.mariadb.org)

## Goals and Quality Standards

The primary goal of MariaDB Server is for it to be a practical database developed in the direction users and developers want it to be developed. Each feature should ideally be developed by or for users who want to test and put the feature into production ASAP — this helps ensure we don't implement features no one wants or needs.

We are also putting a lot of effort into speeding up MariaDB Server, and to keep it stable and easy to use!

The MariaDB Server source tree is maintained by MariaDB the company and its developers. They are the primary contributors to the MariaDB Server project and the ones who are ultimately responsible for the quality of the code.

MariaDB Server 5.1, MariaDB Server 5.2, and MariaDB Server 5.3 were built off of [MySQL 5.1](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/development-articles/general-info/broken-reference/README.md).

MariaDB Server 5.5 was a combination of MariaDB Server 5.3 and MySQL 5.5.

MariaDB Server 10.0, and later build off of the previous MariaDB Server releases with backported features from MySQL and entirely new features not found anywhere else.

Short descriptions of the various MariaDB Server releases and their main new features\
can be found on the [MariaDB Server Releases](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server) page.

## Plans

MariaDB 12.3 is an upcoming major development release.

### JIRA

We manage our development plans in JIRA, so the definitive list will be there. [This search](https://jira.mariadb.org/issues/?jql=project+%3D+MDEV+AND+issuetype+%3D+Task+AND+fixVersion+in+%2812.3%29+ORDER+BY+priority+DESC) shows what we **currently** plan for 12.3. It shows all tasks with the **Fix-Version** being 12.3. Not all these tasks will really end up in the release but tasks with the "red" priorities have a much higher chance of being done in time. Practically, you can think of these tasks as "features that **will** be in 12.3". Tasks with the "green" priorities probably won't be in. Think of them as "bonus features that would be **nice to have** in 12.3".

### Contributing

If you want to be part of developing any of these features, see [Contributing to the MariaDB Project](../../community/contributing-participating/contributing-to-the-mariadb-project.md). You can also add new features to this list or to [JIRA](tools/jira.md).

## See Also

* [Current tasks for 12.3](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20issuetype%20%3D%20Task%20AND%20fixVersion%20in%20\(12.3\)%20ORDER%20BY%20priority%20DESC)
* [12.3 Features/fixes by vote](https://jira.mariadb.org/issues/?jql=project%20%3D%20MDEV%20AND%20issuetype%20%3D%20Task%20AND%20fixVersion%20in%20\(12.3\)%20ORDER%20BY%20votes%20DESC%2C%20priority%20DESC)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
