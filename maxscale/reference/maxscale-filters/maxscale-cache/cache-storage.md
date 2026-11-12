---
description: >-
  The storage modules the cache filter can use: in-memory, GridGain, memcached,
  and Redis, with their settings, limitations, and security.
---

# MaxScale Cache Storage

The cache filter stores cached results in a storage module, which is set with the [storage](cache-settings.md#storage) setting.

There are two types of storages that can be used; _local_ and _shared_.

The only _local_ storage implementation is `storage_inmemory` that simply stores the cache values in memory. The storage is not persistent and is destroyed when MaxScale terminates. Since the storage exists in the MaxScale process, it is very fast and provides almost always a performance benefit.

There are three _shared_ storages; `storage_memcached`, `storage_redis` and `storage_gridgain`
that are implemented using [memcached](https://memcached.org/), [redis](https://redis.io/) and
[gridgain](https://www.gridgain.com/) respectively. The `storage_memcached` storage is
available until MaxScale 25.10.

The shared storages are accessed across the network and consequently it is _not_ self-evident that their use will provide any performance benefit. Namely, irrespective of whether the data is fetched from the cache or from the server there will be a network hop and often that network hop is, as far as the performance goes, what costs the most.

The presence of a shared cache _may_ provide a performance benefit

* if the network between MaxScale and the storage server (memcached, Redis or GridGain) is faster than the network between MaxScale and the database server,
* if the used SELECT statements are heavy (that is, take a significant amount of time) to process for the database server, or
* if the presence of the cache reduces the overall load of an otherwise overloaded database server.

As a general rule a _shared_ storage should not be used without first assessing its value using a realistic workload.

## `storage_inmemory`

This simple storage module uses the standard memory allocator for storing the cached data.

```
storage=storage_inmemory
```

This storage module takes no arguments.

## `storage_gridgain`

Available since MaxScale 25.10.3.

This storage module uses [gridgain](https://www.gridgain.com/) for storing the cache data.
This storage can only be used with [cached_data](cache-settings.md#cached_data) specified as `thread_specific`,
which is the default, so it need not explicitly be specified.

Multiple MaxScale instances can share the same gridgain server and items cached by one
MaxScale instance will be used by the other. Note that all MaxScale instances should
have exactly the same configuration, as otherwise there can be unintended sharing.

```
storage=storage_gridgain
```

Storage specific settings are configured using nested parameters.
```
[MyCache]
...
storage=storage_gridgain
storage_gridgain.endpoints=127.0.0.1
```

`storage_gridgain` has the following parameters:

### `endpoints`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: 127.0.0.1:10800
* Description: Defines the comma-separated list of GridGain endpoints.

An endpoint is specified as `<host>[:<port>[..<port_range>]]` and several
endpoints can be specified, separated by a comma.

### `user`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the user used for authenticating with GridGain.

The user to be used when authenticating with GridGain.

### `password`

* Type: password
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the password used for authenticating with GridGain.

The password to be used when authenticating with GridGain.

### `ssl`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Enables SSL when connecting to the GridGain server.

If `true`, SSL will be used in the communication with GridGain in which case
the `ssl_` settings should be specified as well.

### `ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the SSL client certificate used when connecting to the GridGain server.

The SSL client certificate that MaxScale should use with the GridGain server. The certificate must
match the key defined in `ssl_key`.

### `ssl_key`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the SSL client private key used when connecting to the GridGain server.

The SSL client private key MaxScale should use with the GridGain server.

### `ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the CA certificate used for the SSL connection to the GridGain server.

The Certificate Authority (CA) certificate for the CA that signed the certificate
specified with `ssl_cert`.

### `max_value_size`

* Type: [size](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi
* Description: Defines the maximum size of a value that can be stored in GridGain.

The default maximum size of a value to be stored in GridGain.

### `partition_awareness`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Enables GridGain partition awareness, so that requests go directly to the node that owns the data.

[Partition awareness](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/getting-started-with-thin-clients#partition-awareness)
allows a thin GridGain client to send query requests directly to the node that
owns the queried data and should usually be enabled.

### Limitations

* Invalidation is not supported.
* Configuration values given to `max_size` and `max_count` are ignored.

### Security

The data in the GridGain server is _not_ encrypted.

## `storage_memcached`

{% hint style="info" %}
This storage module is available until MaxScale 25.10.
{% endhint %}

This storage module uses [memcached](https://memcached.org/) for storing the cached data.

Multiple MaxScale instances can share the same memcached server and items cached by one MaxScale instance will be used by the other. Note that all MaxScale instances should have exactly the same configuration, as otherwise there can be unintended sharing.

```
storage=storage_memcached
```

`storage_memcached` has the following parameters:

### `server`

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No
* Description: Specifies the Memcached server address. The default port is 11211 is used when no port is provided.

If no port is provided, then the default port `11211` will be used.

### `max_value_size`

* Type: [size](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi
* Description: Defines the maximum size of a value that can be stored in the cache.

By default, the maximum size of a value stored to memcached is 1MiB, but that can be configured to something else, in which case this parameter should be set accordingly.

The value of `max_value_size` will be used for capping `max_resultset_size`, that is, if memcached has been configured to allow larger values than 1MiB but `max_value_size` has not been set accordingly, only resultsets up to 1MiB in size will be cached.

### Example

From MaxScale 23.02 onwards, the storage configuration should be provided as nested parameters.

```
[Cache-Filter]
type=filter
module=cache
storage=storage_memcached
storage_memcached.server=192.168.1.31
storage_memcached.max_value_size=10M
```

Although _deprecated_ in 23.02, the configuration can also be provided using `storage_options`:

```
storage_options="server=192.168.1.31,max_value_size=10M"
```

### Limitations

* Invalidation is not supported.
* Configuration values given to `max_size` and `max_count` are ignored.

### Security

_Neither_ the data in the memcached server _nor_ the traffic between MaxScale and the memcached server is encrypted. Consequently, _anybody_ with access to the memcached server or to the network have access to the cached data.

## `storage_redis`

This storage module uses [redis](https://redis.io/) for storing the cached data.

Note that Redis should be configured with no idle timeout or with a timeout that is very large. Otherwise MaxScale may have to repeatedly connect to Redis, which will hurt both the functionality and the performance.

Multiple MaxScale instances can share the same redis server and items cached by one MaxScale instance will be used by the other. Note that all MaxScale instances should have exactly the same configuration, as otherwise there can be unintended sharing.

```
storage=storage_redis
```

If `storage_redis` cannot connect to the Redis server, caching will silently be disabled and a connection attempt will be made after a [timeout](cache-settings.md#timeout) interval.

If a timeout error occurs during an operation, reconnecting will be attempted after a delay, which will be an increasing multiple of `timeout`. For example, if `timeout` is the default 5 seconds, then reconnection attempts will first be made after 10 seconds, then after 15 seconds, then 20 and so on. However, once 60 seconds have been reached, the delay will no longer be increased but the delay will stay at one minute. Note that each time a reconnection attempt is made, unless the reason for the timeout has disappeared, the client will be stalled for `timeout` seconds.

`storage_redis` has the following parameters:

### `server`

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No
* Description: Defines the Redis server address. The default port is 6379 is used when no port is provided.

If no port is provided, then the default port `6379` will be used.

### `username`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Username used for authentication.

Please see [authentication](#authentication) for more information.

### `password`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Password used for authentication.

Please see [authentication](#authentication) for more information.

### `ssl`

* Type: [boolean](../../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Enable SSL when connectign to the Redis server.

Please see [ssl](#ssl-1) for more information.

### `ssl_cert`

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Defines the SSL client certificate used when connecting to the Redis server.

The SSL client certificate that MaxScale should use with the Redis server. The certificate must match the key defined in `ssl_key`.

Please see [ssl](#ssl-1) for more information.

### `ssl_key`

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Specifies the private key for the SSL client that is used to connect to the Redis server.

The SSL client private key MaxScale should use with the Redis server.

Please see [ssl](#ssl-1) for more information.

### `ssl_ca`

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Specifies the CA certificate used to verify the Redis server certificate.

The Certificate Authority (CA) certificate for the CA that signed the certificate specified with `ssl_cert`.

Please see [ssl](#ssl-1) for more information.

### Authentication

If `password` is provided, MaxScale will authenticate against Redis when a connection has been created. The authentication is performed using the [auth](https://redis.io/commands/auth/) command, with only the `password` as argument, if no `username` was provided in the configuration, or `username` and `password` as arguments, if both were.

Note that if the authentication is in the Redis configuration file specified using `requirepass`, then only the _password_ should be provided. If the Redis server version is 6 or higher and the _Redis ACL system_ is used, then both _username_ and _password_ must be provided.

### SSL

If `ssl_key`, `ssl_cert` and `ssl_ca` are provided, then SSL/TLS will be used in the communication with the Redis server, if `ssl` is set to `true`.

Note that the SSL/TLS support is only available in Redis from version 6 onwards and that the support is not by default built into Redis, but has to be specifically enabled at compile time as explained [here](https://redis.io/docs/management/security/encryption/).

### Example

From MaxScale 23.02 onwards, the storage configuration should be provided as nested parameters.

```
[Cache-Filter]
type=filter
module=cache
storage=storage_redis
storage_redis.server=192.168.1.31
storage_redis.username=hello
storage_redis.password=world
```

Although _deprecated_ in 23.02, the configuration can also be provided using `storage_options`:

```
storage_options="server=192.168.1.31,username=hello,password=world"
```

### Limitations

* There is no distinction between soft and hard ttl, but only hard ttl is used.
* Configuration values given to `max_size` and `max_count` are ignored.

### Invalidation

`storage_redis` supports invalidation, but the caveats documented [here](README.md#best-efforts) are of greater significance since also the communication between the cache and the cache storage is asynchronous and takes place over the network.

_NOTE_ If invalidation is turned on after caching has been used (in non-invalidation mode), redis must be flushed as otherwise there will be entries in the cache that will not be affected by the invalidation.

```
$ redis-cli flushall
```

### Security

The data in the redis server is _not_ encrypted. Consequently, _anybody_ with access to the redis server has access to the cached data.

Unless [SSL](#ssl) has been enabled, _anybody_ with access to the network has access to the cached data.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
