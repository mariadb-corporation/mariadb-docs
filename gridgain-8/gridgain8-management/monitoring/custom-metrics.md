---
description: >-
  How to register your own metrics in custom registries with the IgniteMetrics
  API, and the permissions and limitations that apply to them.
---

# Custom Metrics

{% hint style="warning" %}
Custom metrics are an experimental feature and can be changed in future releases.
{% endhint %}

In addition to [generic metrics](../../reference/monitoring/generic-metrics.md), you can register your own metrics. The configured [metric exporters](../../reference/monitoring/generic-metrics.md#metric-exporters) expose them alongside the built-in metrics.

Custom metrics only exist on the node where you register them.

## Managing Custom Registries

You can get an instance of the `IgniteMetrics` object from the `Ignite.metrics()` method. Use it to manage custom registries:

- `getOrCreate("registryName")` method creates the custom registry with the given name, or gets it if it already exists.
- `remove("registryName")` method removes the custom registry and all of its metrics.

GridGain adds the `custom.` prefix to every custom registry name. For example, `getOrCreate("admin.sessions")` creates the `custom.admin.sessions` registry. A name that already starts with `custom.` is not prefixed again. Registry names and metric names are limited to 256 characters. To change the limit, set the `IGNITE_CUSTOM_METRICS_MAX_NAME_LENGTH` system property to a positive value.

## Registering Metrics

The registry gets metric values from a supplier each time the metric is read. The following example registers a metric that reports the number of active user sessions:

{% tabs %}
{% tab title="Java" %}
```java
AtomicInteger activeSessions = new AtomicInteger();

// Creates the custom.admin.sessions registry.
MetricRegistry registry = ignite.metrics().getOrCreate("admin.sessions");

// Full metric name: custom.admin.sessions.active.
registry.register("active", activeSessions::get, "Number of active user sessions.");

// Removes the metric.
registry.remove("active");

// Removes the registry and all of its metrics.
ignite.metrics().remove("admin.sessions");
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Security

When [authorization](../../security/authorization-permissions.md) is enabled, every call to `IgniteMetrics.getOrCreate()` (even for an existing registry), `IgniteMetrics.remove()`, `MetricRegistry.register()` and `MetricRegistry.remove()` requires the `CUSTOM_METRICS_MANAGE` system permission. The permission is checked on every call.

Reading custom metrics does not require a permission.

## Limitations

- You cannot change the built-in metrics through this API.
- Custom metrics are not persisted. Register them again after a node restarts.
- Custom metrics cannot be configured.
- The API is available in Java only. Thin clients, the .NET and C++ APIs, and the REST API do not support custom metrics.
