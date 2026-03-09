---
description: >-
  Covers the historic procedures for merging updates from the TokuDB storage
  engine source tree into MariaDB.
---

# Merging TokuDB (obsolete)

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

{% hint style="info" %}
**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.
{% endhint %}

We merge TokuDB from Tokutek **git** repositories on GutHub:

* [tokudb-engine](https://github.com/Tokutek/tokudb-engine)
* [ft-index](https://github.com/Tokutek/ft-index)

Just merge normally at release points (use tag names) and don't forget to update `storage/tokudb/CMakeLists.txt`, setting `TOKUDB_VERSION` correctly.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
