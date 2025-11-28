---
description: >-
  Coordinated Universal Time (UTC) is the primary time standard by which the
  world regulates clocks and time, and is the internal storage format for
  MariaDB timestamp values.
---

# Coordinated Universal Time

UTC stands for Coordinated Universal Time. It is the world standard for regulating time.

MariaDB stores values internally in UTC, converting them to the required time zone as required.

In general terms it is equivalent to Greenwich Mean Time (GMT), but UTC is used in technical contexts, as it is precisely defined at the subsecond level.

[Time zones](time-zones.md) are offset relative to UTC. For example, time in Tonga is UTC + 13, so 03h00 UTC is 16h00 in Tonga.

## See Also

* [UTC\_DATE](../../../../sql-functions/date-time-functions/utc_date.md)
* [UTC\_TIME](../../../../sql-functions/date-time-functions/utc_time.md)
* [UTC\_TIMESTAMP](../../../../sql-functions/date-time-functions/utc_timestamp.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
