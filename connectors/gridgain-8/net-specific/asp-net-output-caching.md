---
hidden: true
description: >-
  Use a GridGain (Ignite) cache as an ASP.NET output cache, with configuration
  for launching Ignite automatically or manually.
---

# ASP.NET Output Caching

## Overview

Ignite cache can be used as an ASP.NET output cache. This can work especially well for web farms where cached output will be shared between web servers.

## Installation

- **Binary distribution**: add a reference to `Apache.Ignite.AspNet.dll`
- **NuGet**: `Install-Package GridGain.Ignite.AspNet`

## Launching Ignite Automatically

To start Ignite automatically for output caching, configure it [in the web.config file via IgniteConfigurationSection](net-configuration-options.md#configure-with-application-or-web-config-files)

{% code title="web.config" %}
```xml
<configuration>
    <configSections>
        <section name="igniteConfiguration" type="Apache.Ignite.Core.IgniteConfigurationSection, Apache.Ignite.Core" />
    </configSections>

    <igniteConfiguration autoGenerateIgniteInstanceName="true">
        <cacheConfiguration>
            <cacheConfiguration name='myWebCache' />
        </cacheConfiguration>
    </igniteConfiguration>
</configuration>
```
{% endcode %}

Enable the caching in the `web.config` settings:

{% code title="web.config" %}
```xml
<system.web>
  <caching>
    <outputCache defaultProvider="apacheIgnite">
      <providers>
          <add name="apacheIgnite" type="Apache.Ignite.AspNet.IgniteOutputCacheProvider, Apache.Ignite.AspNet" igniteConfigurationSectionName="igniteConfiguration" cacheName="myWebCache" />
      </providers>
    </outputCache>
  </caching>
</system.web>
```
{% endcode %}

## Launching Ignite Manually

You can start an Ignite instance manually and specify it's name in the provider configuration:

{% code title="web.config" %}
```xml
<system.web>
  <caching>
    <outputCache defaultProvider="apacheIgnite">
      <providers>
          <add name="apacheIgnite" type="Apache.Ignite.AspNet.IgniteOutputCacheProvider, Apache.Ignite.AspNet" cacheName="myWebCache" />
      </providers>
    </outputCache>
  </caching>
</system.web>
```
{% endcode %}

The Ignite instance needs to be started before any request is served. Typically this is done in the `Application_Start` method of the `global.asax`.

See [ASP.NET Deployment](net-deployment-options.md#asp.net-deployment) for web deployment specifics related to the `IGNITE_HOME` variable.
