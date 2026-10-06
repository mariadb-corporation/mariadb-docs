---
hidden: true
description: >-
  Run GridGain.NET on Windows, Linux, and macOS with .NET Framework and .NET
  Core, including Java detection and known issues.
---

# Cross-Platform Support

## Overview

GridGain.NET supports both .NET Framework and .NET Core. It is possible to run .NET nodes and develop GridGain.NET applications for Linux and macOS, as well as Windows.

## .NET Core

**Requirements:**

- [.NET Core SDK 2.0+](https://www.microsoft.com/net/download/)
- [Java 8+](http://www.oracle.com/technetwork/java/javase/downloads/index.html) (macOS requires JDK, otherwise JRE works)

**Running Examples**
[Binary distribution](https://ignite.apache.org/download.cgi#binaries) includes .NET Core examples:

- Download [binary distribution](https://ignite.apache.org/download.cgi#binaries) from the Ignite website and extract into any directory.
- `cd platforms/dotnet/examples/dotnetcore`
- `dotnet run`

## Java Detection

GridGain.NET looks for a Java installation directory in the following places:

- `HKLM\Software\JavaSoft\Java Runtime Environment` (Windows)
- `/usr/bin/java` (Linux)
- `/Library/Java/JavaVirtualMachines` (macOS)

If you changed the default location of Java, then specify the actual path using one of the methods below:

- Set the `IgniteConfiguration.JvmDllPath` property
- or set the `JAVA_HOME` environment variable

## Known Issues

**No Java runtime present, requesting install**

Java `8u151` has a known bug on macOS: [JDK-7131356](https://bugs.openjdk.java.net/browse/JDK-7131356). Make sure to install `8u152` or later.

**Serializing delegates is not supported on this platform**

.NET Core does not support delegate serialization, `System.MulticastDelegate.GetObjectData`, instead it throws an exception so GridGain.NET can not serialize delegates or objects containing them.

**Could not load file or assembly 'System.Configuration.ConfigurationManager'**

Known [.NET issue (506)](https://github.com/dotnet/standard/issues/506), in some cases additional package reference is required:

- `dotnet add package System.Configuration.ConfigurationManager`
