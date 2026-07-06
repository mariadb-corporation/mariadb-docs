---
description: >-
  Learn about the connection phase in the client/server protocol. This section
  details how clients establish initial communication with the server, including
  handshaking and authentication processes.
---

# 1 - Connecting

{% columns %}
{% column %}
{% content-ref url="connection.md" %}
[connection.md](connection.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The connection phase involves an initial handshake where the client and server exchange capabilities, default settings, and authentication data to establish a session.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sha256_password-plugin.md" %}
[sha256_password-plugin.md](sha256_password-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The sha256_password plugin manages authentication using SHA-256 encryption, supporting both clear text passwords over SSL and RSA encrypted password exchange.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="caching_sha2_password-authentication-plugin.md" %}
[caching_sha2_password-authentication-plugin.md](caching_sha2_password-authentication-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This plugin implements the caching_sha2_password authentication method, using an in-memory cache for fast authentication or RSA encryption for full verification.
{% endcolumn %}
{% endcolumns %}
