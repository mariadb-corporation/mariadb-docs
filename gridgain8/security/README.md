---
description: >-
  Overview of GridGain security features, including encrypted communications,
  authentication, authorization, and auditing.
icon: shield-halved
---

# Security and Auditing

GridGain's security features allow you to perform security activities, such as encrypting communications, configuring authentication and authorization methods, and performing audits. For example, you can secure the communications between cluster nodes by using SSL/TLS encryption.
What is more, GridGain provides a convenient and flexible way for managing user roles and permissions. For example, Control Center allows to share its features between team members using the [Teams](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD/control-center/profile/teams) functionality.

{% hint style="info" %}
Some of the security features explained in this topic are the features of the GridGain Enterprise and Ultimate editions.
{% endhint %}

The GridGain security functionality includes the following features:

{% columns %}
{% column %}
{% content-ref url="authentication-and-authorization/" %}
[Authentication and Authorization](authentication-and-authorization/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control who can connect to a GridGain cluster and what they may do — authentication mechanisms, permission-based authorization, custom authenticators, and multi-tenant isolation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="encryption-and-transport/" %}
[Encryption and Transport Security](encryption-and-transport/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Protect GridGain data in transit and at rest — SSL/TLS for nodes and clients, transparent data encryption, deserialization safeguards, and securing the JMX interface.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hardening-and-compliance/" %}
[Hardening, Auditing, and CVEs](hardening-and-compliance/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Harden a GridGain deployment and stay compliant — cluster hardening practices, event-based auditing, and the list of fixed security vulnerabilities.
{% endcolumn %}
{% endcolumns %}
