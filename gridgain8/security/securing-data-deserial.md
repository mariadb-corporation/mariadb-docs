---
description: >-
  Restrict deserialization in GridGain with the IGNITE_MARSHALLER_WHITELIST and
  IGNITE_MARSHALLER_BLACKLIST system properties.
---

# Securing Data Deserialization

Serialized data is vulnerable to [malicious data attacks](https://lists.apache.org/thread.html/45e7d5e2c6face85aab693f5ae0616563132ff757e5a558da80d0209@%3Cdev.ignite.apache.org%3E) if an attacker finds a way to add malicious code to the classpath of your cluster nodes. Best practice is to make sure that the access to the cluster is protected and granted only to a limited group of people.

However, if the attacker breaks through to your deployment environment, GridGain provides the ability to specify `IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST` as **system properties**. These properties allow you to define a list of classes that will be allowed/disallowed for safe deserialization.

## IGNITE_MARSHALLER_WHITELIST

To use `IGNITE_MARSHALLER_WHITELIST`, create a file containing the list of files **allowed** for deserialization.
For example, a text file (whitelist.txt) would look like so:

{% code title="whitelist.txt" %}
```text
ignite.myexamples.model.Address
ignite.myexamples.model.Person
...
```
{% endcode %}

Then, set the system property when you run your application, or programmatically:

{% tabs %}
{% tab title="VM Options" %}
```text
-DIGNITE_MARSHALLER_WHITELIST=path/to/whitelist.txt
```
{% endtab %}

{% tab title="Java" %}
```java
System.setProperty(IGNITE_MARSHALLER_WHITELIST, "Path/to/whitelist.txt");
```
{% endtab %}
{% endtabs %}

Substitute `path/to/whitelist.txt` with actual path to your whitelist file.

When the `IGNITE_MARSHALLER_WHITELIST` system property is used, an attempt to deserialize any file not on the whitelist will result in an exception:

{% code title="Text" %}
```text
Exception in thread "main" javax.cache.CacheException: class org.apache.ignite.IgniteCheckedException: Deserialization of class ignite.myexamples.model.Organization is disallowed.
```
{% endcode %}

## IGNITE_MARSHALLER_BLACKLIST

To use `IGNITE_MARSHALLER_BLACKLIST`, create a file containing the list of files **disallowed** for deserialization.
For example, a text file (blacklist.txt) would look like so:

{% code title="blacklist.txt" %}
```text
ignite.myexamples.model.SomeFile
ignite.myexamples.model.SomeOtherFile
...
```
{% endcode %}

Then, set the system property when you run your application, or programmatically:

{% tabs %}
{% tab title="VM Options" %}
```text
-DIGNITE_MARSHALLER_BLACKLIST=path/to/blacklist.txt
```
{% endtab %}

{% tab title="Java" %}
```java
System.setProperty(IGNITE_MARSHALLER_BLACKLIST, "Path/to/blacklist.txt");
```
{% endtab %}
{% endtabs %}

Substitute `path/to/blacklist.txt` with actual path to your blacklist file.

When the `IGNITE_MARSHALLER_BLACKLIST` system property is used, an attempt to deserialize any file mentioned on the blacklist will result in an exception:

{% code title="Text" %}
```text
Exception in thread "main" javax.cache.CacheException: class org.apache.ignite.IgniteCheckedException: Deserialization of class ignite.myexamples.model.SomeOtherFile is disallowed.
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
