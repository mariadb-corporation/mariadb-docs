---
description: >-
  A synthetic event sent by the master after the initial handshake to inform the
  replica of its current GTID state, it is not written to the binary log.
---

# Fake GTID\_LIST event

This event is sent by master server to the registering replica. It is sent only once, after the [Format Description Event](format_description_event.md).

{% hint style="info" %}
The fake `GTID_LIST` event is not written in the binlog file. It's created by the master and sent to newly connected replica before any "real" binlog event.
{% endhint %}

## Header

* Event type is set to `163` (`0xa3`).
* Time stamp set to `0`.
* NextPos tells which is the binlog position of next event.
* Flags are set to `ARTIFICIAL` (`0x20`).

## Content

The content is the same as the "real" [GTID\_LIST](gtid_list_event.md).

* **of GTIDs**
* domain\_id
* server\_id
* sequence
* ...

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
