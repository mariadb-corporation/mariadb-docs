# MaxScale Monitor

## Overview

MaxScale Monitor monitors MaxScale instances. It connects to the REST-APIs of
monitored MaxScales and fetches general MaxScale and server information.
MaxScale monitor is part of the MariaDB Enterprise Manager and cannot be
activated within a normal MaxScale.

## Required Grants

The MaxScale monitor requires access to the REST-APIs of monitored MaxScales.
Read-only access is sufficient for basic monitoring, admin access is required
for any features that modify the MaxScales. Create user accounts on the
MaxScales with MaxCtrl:
```
maxctrl create user --type=admin MyMonitorUser MyMonitorPw
```

## Configuration

A minimal configuration is below. *type*, *module*, monitored servers and login
credentials are mandatory.

```
[MyMxsMonitor]
type=monitor
module=mxsmon
servers=MyMaxScale1,MyMaxScale2
user=admin
password=mariadb
```

Configure the monitored MaxScales as servers.
```
[MyMaxScale1]
type=server
address=192.168.0.1
port=8989

[MyMaxScale2]
type=server
address=192.168.0.2
port=8989
```
Add `ssl=true` to a server to force the monitor to use HTTPS. Other supported
[SSL settings](../Getting-Started/Configuration-Guide.md#tlsssl-encryption)
are `ssl_key`, `ssl_cert`, `ssl_ca`, `ssl_verify_peer_certificate` and
`ssl_verify_peer_host`.

For a list of optional parameters that all monitors support, read the
[Monitor Common](Monitor-Common.md) document.

The following lists optional parameters specific to the MaxScale Monitor.

### `advertised_url`

- **Type**: string
- **Mandatory**: No
- **Dynamic**: Yes
- **Default**: None

Public URL of the Enterprise Manager admin interface. The manager configures
*admin_oidc_url* on monitored MaxScales to this value so that they use the
Manager as an authentication provider for the REST-API and GUI. This enables
automatic login from the Manager GUI to MaxScale GUI. The MaxScale monitor
will only try to configure *admin_oidc_url* once per MaxScale, when first
successfully connecting. If the attempt fails for any reason, the monitor
or the Enterprise Manager must be restarted to try again.

If this setting is left unset, the MaxScale monitor will guess its value by
combining the system hostname with the REST-API port, e.g. `http://myhost:8990`.

```
advertised_url=mypublichostname:8990
```

## Usage

Show status of monitored MaxScales with MaxCtrl (assuming that Enterprise
Manager in running on the local machine and its REST-API listens on port
8990):
```
maxctrl --hosts=127.0.0.1:8990 list servers
┌──────────────┬───────────┬───────┬─────────────┬────────┬────────────────────┬─────────────┬─────────────────┐
│ Server       │ Address   │ Port  │ Connections │ Status │ Status Info        │ GTID        │ Monitor         │
├──────────────┼───────────┼───────┼─────────────┼────────┼────────────────────┼─────────────┼─────────────────┤
│ MyMaxScale1  │ 127.0.0.1 │ 8989  │ 0           │ Up     │                    │             │ MXS-Monitor     │
├──────────────┼───────────┼───────┼─────────────┼────────┼────────────────────┼─────────────┼─────────────────┤
```

Show detailed information about monitored MaxScales and their monitored servers:
```
maxctrl --hosts=127.0.0.1:8990 show monitors
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
