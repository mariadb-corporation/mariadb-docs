---
description: >-
  Protect GridGain data in transit and at rest — SSL/TLS for nodes and clients, transparent data encryption, deserialization safeguards, and securing the JMX interface.
---

# Encryption and Transport Security

This section groups the following topics:

{% columns %}
{% column %}
{% content-ref url="../ssl-tls.md" %}
[SSL/TLS](../ssl-tls.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure SSL/TLS encryption for GridGain cluster nodes and clients, enable client certificate authentication, and manage certificates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../tde.md" %}
[Transparent Data Encryption](../tde.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Transparent Data Encryption in GridGain: encrypt data at rest per cache, generate a master key, and rotate master and cache keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../securing-data-deserial.md" %}
[Securing Data Deserialization](../securing-data-deserial.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restrict deserialization in GridGain with the IGNITE_MARSHALLER_WHITELIST and IGNITE_MARSHALLER_BLACKLIST system properties.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../securing-jmx.md" %}
[Securing JMX](../securing-jmx.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Secure the JMX server that GridGain nodes start, by disabling remote JMX or enabling password authentication and SSL.
{% endcolumn %}
{% endcolumns %}
