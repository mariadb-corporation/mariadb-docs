---
description: >-
  How MariaDB Shell connects to MariaDB Server: connection URIs, local sockets,
  option files, TLS, SSH tunnels, compression, and stored passwords.
icon: plug
---

# Connecting to a Server

MariaDB Shell connects to MariaDB Server, and to MySQL servers, over the classic client/server protocol through MariaDB Connector/C. You describe the target with a connection URI such as `mariadb://dba@db1.example.com:3306/shop`, with a dictionary of connection options in Python, or with command-line options such as `-h`, `-P`, and `-u`.

The pages in this section explain each part of a connection, from the URI syntax to tunnels and stored passwords.

{% hint style="info" %}
To open a first connection and learn how the global session works, see [Sessions](../getting-started/sessions.md).
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="connection-uris-and-options.md" %}
[connection-uris-and-options.md](connection-uris-and-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The URI syntax with the `mariadb://` scheme, connection dictionaries, the connection command-line options, and which setting wins when they overlap.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sockets-and-named-pipes.md" %}
[sockets-and-named-pipes.md](sockets-and-named-pipes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Local connections through a Unix socket file, or through a named pipe on Windows.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="option-files-and-login-paths.md" %}
[option-files-and-login-paths.md](option-files-and-login-paths.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The option files and groups that MariaDB Shell reads at startup, and how it uses `~/.mylogin.cnf`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encrypted-connections.md" %}
[encrypted-connections.md](encrypted-connections.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The TLS modes and how they behave against MariaDB Server, certificates, revocation lists, ciphers, and protocol versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ssh-tunnels.md" %}
[ssh-tunnels.md](ssh-tunnels.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reaching a server through SSH with a `mariadb+ssh://` URI or with the `--ssh` options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="compressed-connections.md" %}
[compressed-connections.md](compressed-connections.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Turning on protocol compression for slow or metered links.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="credential-store.md" %}
[credential-store.md](credential-store.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How MariaDB Shell remembers passwords and other secrets, the helper used on each platform, and the functions that manage stored entries.
{% endcolumn %}
{% endcolumns %}
