---
description: >-
  Manage binary type metadata programmatically through the GridGain Java and .NET APIs to list, retrieve, and remove binary types.
---

# Managing Metadata Programmatically

## Overview

GridGain enables you to manage metadata (binary types) in your environment via the [Java](https://www.gridgain.com/sdk/latest/javadoc/org/apache/ignite/IgniteBinary.html) and [.NET](https://www.gridgain.com/sdk/latest/dotnetdoc/api/Apache.Ignite.Core.Binary.IBinary.html) APIs.

The following operations are supported:

- [List Metadata for All Binary Types](#list-metadata-for-all-binary-types)
- [Get Metadata for a Specific Binary Type](#get-metadata-for-a-specific-binary-type)
- [Remove a Binary Type](#remove-a-binary-type)

{% hint style="info" %}
The same operations can be performed with the use of [--meta commands](../../reference/cli-tool/README.md#binary-type-management) of GridGain's `control.sh|bat` script.
{% endhint %}

## List Metadata for All Binary Types

This operation retrieves metadata for all binary types defined in your environment.

{% tabs %}
{% tab title="Java" %}
```java
public Collection<BinaryType> types() throws BinaryObjectException;
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
ICollection<IBinaryType> GetBinaryTypes();
```
{% endtab %}
{% endtabs %}

## Get Metadata for a Specific Binary Type

This operation retrieves metadata for the binary type indicated by `typeId` or `typeName`.

{% tabs %}
{% tab title="Java" %}
```java
public BinaryType type(int typeId) throws BinaryObjectException;

public BinaryType type(String typeName) throws BinaryObjectException;
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
IBinaryType GetBinaryType(int typeId);

IBinaryType GetBinaryType(string typeName);
```
{% endtab %}
{% endtabs %}

## Remove a Binary Type

This operation removes the binary type indicated by `typeId`.

{% tabs %}
{% tab title="Java" %}
```java
public void removeType(int typeId) throws IgniteException;
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
void RemoveBinaryType(int typeId);
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
