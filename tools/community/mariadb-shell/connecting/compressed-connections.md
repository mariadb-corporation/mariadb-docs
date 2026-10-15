---
description: >-
  Turn on protocol compression to reduce the data sent between MariaDB Shell
  and the server over slow or metered links.
---

# Compressed Connections

Protocol compression reduces the amount of data that travels between MariaDB Shell and the server, at the cost of CPU time on both ends. It pays off on slow or metered network links, and for large result sets or bulk transfers. On a fast local network, it usually slows things down.

Compression is off by default.

## Turning Compression On

Use `-C` or `--compress` on the command line, or the `compression` connection option in a URI or a dictionary:

{% tabs %}
{% tab title="Command line" %}
```sh
mariadb-shell -C dba@db1.example.com/shop --sql
```
{% endtab %}

{% tab title="URI" %}
```text
mariadb://dba@db1.example.com/shop?compression=REQUIRED
```
{% endtab %}

{% tab title="Python" %}
```python
shell.connect({"uri": "dba@db1.example.com/shop", "compression": "REQUIRED"})
```
{% endtab %}

{% tab title="Option file" %}
```ini
[mariadb-shell]
compress
```
{% endtab %}
{% endtabs %}

The `compression` option and `--compress` accept the following values, in any letter case:

| Value | Effect |
| --- | --- |
| `REQUIRED`, `true`, `1` | Compression on. `-C` without a value means `REQUIRED`. |
| `PREFERRED` | Compression on. |
| `DISABLED`, `false`, `0` | Compression off. This is the default. |

MariaDB Server compresses the classic protocol with zlib. Connector/C negotiates compression with the server during the handshake, and `REQUIRED` and `PREFERRED` behave the same.

To confirm that a session is compressed, check the `Compression` session status variable:

```text
MariaDB db1.example.com:3306 ssl  SQL > SHOW SESSION STATUS LIKE 'Compression';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| Compression   | ON    |
+---------------+-------+
```

## Algorithm and Level Options

MariaDB Shell also accepts the `compression-algorithms` and `compression-level` connection options, which select the algorithm and its level against MySQL 8.0 and later servers. MariaDB Connector/C has no such settings, so with MariaDB Shell these options have no effect:

* `compression-algorithms` doesn't select an algorithm, and, unlike in MySQL Shell, it doesn't turn compression on by itself. A connection with only `compression-algorithms=zlib` is not compressed. Set `compression` as well.
* `compression-level` doesn't change the compression level.

The one check that still applies is a conflict: `compression=REQUIRED` together with `compression-algorithms=uncompressed` is rejected.
