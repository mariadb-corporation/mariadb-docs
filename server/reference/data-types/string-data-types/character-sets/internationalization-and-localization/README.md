---
description: >-
  Discover how MariaDB supports internationalization and localization, enabling
  databases to store and process data in multiple languages.
---

# Internationalization and Localization

{% columns %}
{% column %}
{% content-ref url="coordinated-universal-time.md" %}
[coordinated-universal-time.md](coordinated-universal-time.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Coordinated Universal Time (UTC) is the primary time standard by which the world regulates clocks and time, and is the internal storage format for MariaDB timestamp values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="locales-plugin.md" %}
[locales-plugin.md](locales-plugin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The LOCALES plugin enables the INFORMATION_SCHEMA.LOCALES table and SHOW LOCALES statement, allowing users to view all locales compiled into the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="server-locale.md" %}
[server-locale.md](server-locale.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Server locale settings control the language for date and time functions via lc_time_names and the language for error messages via lc_messages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setting-the-language-for-error-messages.md" %}
[setting-the-language-for-error-messages.md](setting-the-language-for-error-messages.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to configure the lc_messages and lc_messages_dir system variables to display server error messages in a supported local language.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="time-zones.md" %}
[time-zones.md](time-zones.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How MariaDB tracks and converts time zone settings, including named time zones, the time-zone system tables, and per-session configuration.
{% endcolumn %}
{% endcolumns %}
