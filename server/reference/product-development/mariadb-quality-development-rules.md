---
description: >-
  Outlines strict quality standards for new features, including requirements for
  design specifications, testability, and mandatory Worklog quality checklists.
---

# MariaDB Quality Development Rules

Those are quality-improving rules that everyone with a write access to the MariaDB repository is expected to follow:

* Respect previews
  * A feature can be pushed into an RC release X.Y.1 only after it was in an earlier preview. Normally, in X.Y.0, but generally any earlier preview will do.
* Tester sign-off for all new features
  * A feature being in the preview is a necessary, but not a sufficient condition. It needs to be tested (by a dedicated tester, not a developer) and the tester has to say it's good enough
  * Testing might discover bugs, that's normal, they have to be fixed before the feature is pushed (or — at the tester's discretion — they could be fixed after the push, if they're minor)
  * For tester's sake, develop in a dedicated branch with the version and the issue number in the branch name, for example, `bb-11.1-[MDEV-11111](https://jira.mariadb.org/browse/MDEV-11111)`, and let the release master know when it's ready, so that they could cherry-pick it into a preview.
* Features must not be pushed directly into the GA release bypassing the above
  * Keep an eye on the release schedule ([jira.mariadb.org](https://jira.mariadb.org)) to know when the next release is due
  * Or simply remember that preview happen in mid-March/mid-June/mid-September/mid-December, innovation releases — in early February, early May, early August, early November, see [mariadb-release-model](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/release-model).
* Get your commit reviewed.
  * If you don't know who would be the best reviewer for your PR, assign whoever github suggests — this person can reassign, if github was wrong
* Don't push into the red (in buildbot) branch
  * Fix failures first (or make sure they're fixed)
  * Eventually buildbot will evolve to simply not let you to
* Blocker issues block a release
  * we don't release if there's a Blocker bug open, that's why they're called blockers
  * so fix them asap, as your first priority, you don't want all the users to wait specifically for you
* There's no penalty for breaking these rules, we hope that everyone wants quality bug-free releases anyway
  * but if there will be serial violators, some kind of a penalty can be introduced later

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
