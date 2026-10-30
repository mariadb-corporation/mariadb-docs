---
hidden: true
description: >-
  Configure logging in GridGain.NET, including writing through IIgnite.Logger, custom
  ILogger implementations, and the NLog and log4net integrations.
---

# GridGain.NET Logging

## Overview

By default, Ignite uses underlying the Java log4j logging system. Log messages from both .NET and Java are recorded there.
You can also write to this log via an `IIgnite.Logger` instance:

```csharp
var ignite = Ignition.Start();
ignite.Logger.Info("Hello World!");
```

`LoggerExtensions` class provides convenient shortcuts for `ILogger.Log` method.

## Custom Logger

You can provide a logger implementation via the `IgniteConfiguration.Logger` and `ILogger` interface.
Messages from both .NET and Java will be redirected there.

{% tabs %}
{% tab title="C#" %}
```csharp
var cfg = new IgniteConfiguration
{
  Logger = new MemoryLogger()
}

var ignite = Ignition.Start();

class MemoryLogger : ILogger
{
  // Logger can be called from multiple threads, use concurrent collection
  private readonly ConcurrentBag<string> _messages = new ConcurrentBag<string>();

  public void Log(LogLevel level, string message, object[] args,
                  IFormatProvider formatProvider, string category,
                  string nativeErrorInfo, Exception ex)
  {
    _messages.Add(message);
  }

  public bool IsEnabled(LogLevel level)
  {
    // Accept any level.
    return true;
  }
}
```
{% endtab %}
{% tab title="app.config" %}
```xml
<igniteConfiguration>
<logger type="MyNamespace.MemoryLogger, MyAssembly" />
</igniteConfiguration>
```
{% endtab %}
{% endtabs %}

## NLog & log4net Loggers

GridGain.NET provides `ILogger` implementations for [NLog](http://nlog-project.org/) and [Apache log4net](https://logging.apache.org/log4net/).
They are included in the binary package (`Apache.Ignite.NLog.dll` and `Apache.Ignite.Log4Net.dll`) and can be installed via NuGet:

- `Install-Package Apache.Ignite.NLog`
- `Install-Package Apache.Ignite.Log4Net`

NLog and Log4Net use statically defined configuration, so there is nothing to configure in Ignite besides `IgniteConfiguration.Logger`:

{% tabs %}
{% tab title="C#" %}
```csharp
var cfg = new IgniteConfiguration
{
  Logger = new IgniteNLogLogger()  // or IgniteLog4NetLogger
}

var ignite = Ignition.Start();
```
{% endtab %}
{% tab title="app.config" %}
```xml
<igniteConfiguration>
  <logger type="Apache.Ignite.NLog.IgniteNLogLogger, Apache.Ignite.NLog" />
</igniteConfiguration>
```
{% endtab %}
{% endtabs %}

A simple file-based logging with NLog can be set up like this:

```csharp
var nlogConfig = new LoggingConfiguration();

var fileTarget = new FileTarget
{
  FileName = "ignite_nlog.log"
};
nlogConfig.AddTarget("logfile", fileTarget);

nlogConfig.LoggingRules.Add(new LoggingRule("*", LogLevel.Trace, fileTarget));
LogManager.Configuration = nlogConfig;

var igniteConfig = new IgniteConfiguration
{
  Logger = new IgniteNLogLogger()
};
Ignition.Start(igniteConfig);
```
</content>
