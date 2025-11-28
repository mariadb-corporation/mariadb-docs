---
description: >-
  This event records the preparation phase of an XA transaction, storing the XID
  to support two-phase commit and recovery.
---

# XA\_PREPARE\_LOG\_EVENT

An `XA_PREPARE_LOG_EVENT` records the prepare phase of a distributed transaction using the XA log. It is used to ensure atomicity and consistency of transactions.

## Header

* Event Type is `XA_PREPARE_LOG_EVENT` (`0x26`).

## Fields

* [uint<1>](../protocol-data-types.md#fixed-length-integers) One Phase Commit.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Format ID.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Length of gtrid.
* [uint<1>](../protocol-data-types.md#fixed-length-integers) Length of bqual.

Payload:

* [byte](../protocol-data-types.md#fixed-length-bytes) xid, where n is sum of gtrid and bqual lengths.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
