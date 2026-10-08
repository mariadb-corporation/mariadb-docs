---
hidden: true
description: >-
  Store ASP.NET session state in a distributed GridGain cluster for high
  availability, load balancing, and fault tolerance.
---

# ASP.NET Session State Caching

## Overview

The ASP.NET session state caching is designed to allow you to store user session data in different sources. By default, session state values and information are stored in memory within the ASP.NET process.

GridGain.NET implements a session state store provider that stores session data in a distributed GridGain cluster that spreads the session data across multiple servers in order to provide high availability, load balancing and fault tolerance.

{% hint style="danger" %}
**Development and Debugging**

During development and debugging, IIS will dynamically detect code changes when you build and run your web application. This, however, does not restart the embedded GridGain instance and can cause exceptions and undesired behavior. Make sure to restart IIS manually when using the GridGain Session State Cache.
{% endhint %}

## Installation

- **Binary distribution**: add a reference to Apache.Ignite.AspNet.dll
- **NuGet**: `Install-Package Apache.Ignite.AspNet`

## Configuration

To enable the GridGain-based session state storage, modify the `web.config` file as follows:

{% code title="web.config" %}
```xml
<system.web>
  ...
  <sessionState mode="Custom" customProvider="IgniteSessionStateProvider">
    <providers>
      <add name="IgniteSessionStateProvider"
           type="Apache.Ignite.AspNet.IgniteSessionStateStoreProvider, Apache.Ignite.AspNet"
           igniteConfigurationSectionName="igniteConfiguration"
           applicationId="myApp"
           gridName="myGrid"
           cacheName="aspNetSessionCache" />
    </providers>
  </sessionState>
  ...
</<system.web>
```
{% endcode %}

While the `name` and `type` attributes are required, the other attributes listed below are optional:

| Attribute | Description |
|---|---|
| `igniteConfigurationSectionName` | The `web.config` section name defined in `configSections`. See [Configuration: web.config](net-configuration-options.md#configure-with-application-or-web-config-files) for more details. This configuration will be used to start Ignite if it is not started yet. |
| `applicationId` | Should only be used when multiple web applications share the same Ignite session state cache. Assign different ID strings to avoid session data conflicts between applications. It is recommended to use a separate cache for each application via `cacheName` attribute. |
| `gridName` | Session state provider calls `Ignition.TryGetIgnite` with this grid name to check whether Ignite is already started. |
| `cacheName` | Session state cache name. Default is `ASPNET_SESSION_STATE`. |

For more details on how to start Ignite within an ASP.NET application, refer to [ASP.NET Output Caching](asp-net-output-caching.md). Also, see [ASP.NET Deployment](net-deployment-options.md#asp.net-deployment) for web deployment specifics related to the `IGNITE_HOME` variable.
