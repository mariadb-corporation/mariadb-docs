---
description: MyRocks storage engine transactional isolatioin.
---

# MyRocks Transactional Isolation

* MyRocks uses snapshot isolation.
* Support do `READ-COMMITTED` and `REPEATABLE-READ` .
* `SERIALIZABLE` is not supported.
  * There is no "gap locking" which makes Statement Based Replication unsafe (see [MyRocks and Replication](myrocks-and-replication.md)).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
