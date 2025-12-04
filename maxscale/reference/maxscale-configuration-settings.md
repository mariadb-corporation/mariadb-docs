# MaxScale Configuration Settings

## Configuration Settings

### General

#### [MaxScale](../maxscale-management/deployment/maxscale-configuration-guide.md)

**Global Settings**

[**admin\_audit**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**admin\_audit\_exclude\_methods**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `GET`, `PUT`, `POST`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `CONNECT`, `TRACE`
* Default: No exclusions

[**admin\_audit\_file**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `/var/log/maxscale/admin_audit.csv`

[**admin\_auth**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_enabled**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_gui**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_host**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"127.0.0.1"`

[**admin\_jwt\_algorithm**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `auto`, `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`, `PS256`, `PS384`, `PS512`, `ES256`, `ES384`, `ES512`, `ED25519`, `ED448`
* Default: `auto`

[**admin\_jwt\_issuer**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `maxscale`

[**admin\_jwt\_key**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_jwt\_max\_age**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `24h`

[**admin\_log\_auth\_failures**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**admin\_oidc\_url**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readonly\_service**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_pam\_readwrite\_service**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `8989`

[**admin\_readwrite\_hosts**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `%`

[**admin\_secure\_gui**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**admin\_ssl\_ca**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cert**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_cipher**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No

[**admin\_ssl\_key**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**admin\_ssl\_version**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

[**admin\_verify\_url**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**auth\_connect\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**auto\_tune**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string list
* Values: `all` or list of auto tunable parameters, separated by `,`
* Default: No
* Mandatory: No
* Dynamic: No

[**cachedir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/cache/maxscale`

[**config\_sync\_cluster**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_db**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mysql`

[**config\_sync\_interval**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5s`

[**config\_sync\_password**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: password
* Mandatory: No
* Dynamic: Yes
* Default: None

[**config\_sync\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**config\_sync\_user**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connector\_plugindir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**core\_file**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: No

[**datadir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale`

[**debug**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**dump\_last\_statements**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `on_close`, `on_error`, `never`
* Default: `never`

[**execdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/bin`

[**host\_cache\_size**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: integer
* Default: 128
* Dynamic: Yes

[**key\_manager**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Dynamic: Yes
* Values: `none`, `file`, `kmip`, `vault`
* Default: `none`

[**language**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/`

[**libdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: OS Dependent

[**load\_persisted\_configs**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**local\_address**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**log\_augmentation**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**log\_debug**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_throttling**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number, [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations), [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10, 1000ms, 10000ms`

[**log\_warn\_super\_user**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**log\_warning**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**logdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/log/maxscale`

[**max\_auth\_errors\_until\_block**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**maxlog**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**module\_configdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/etc/maxscale.modules.d/`

[**ms\_timestamp**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**passive**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**persist\_runtime\_changes**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: No

[**persistdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/maxscale.cnf.d/`

[**piddir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/run/maxscale`

[**query\_classifier\_cache\_size**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: System Dependent

[**query\_retries**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1`

[**query\_retry\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**rebalance\_period**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**rebalance\_threshold**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `20`

[**rebalance\_window**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**retain\_last\_statements**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**secretsdir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**session\_trace**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**session\_trace\_match**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sharedir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/usr/share/maxscale`

[**skip\_name\_resolve**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**sql\_mode**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `default`, `oracle`
* Default: `default`

[**substitute\_variables**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**syslog**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**threads**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number or `auto`
* Mandatory: No
* Dynamic: No
* Default: `auto`

[**threads\_max**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: positive integer
* Default: 256
* Dynamic: No

[**trace\_file\_dir**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No

[**trace\_file\_size**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes

[**users\_refresh\_interval**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**users\_refresh\_time**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `30s`

[**writeq\_high\_water**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `65536`

[**writeq\_low\_water**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `1024`

**Listener**

[**address**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `"::"`

[**authenticator**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**authenticator\_options**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**connection\_init\_sql\_file**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**connection\_metadata**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: stringlist
* Default: `character_set_client=auto,character_set_connection=auto,character_set_results=auto,max_allowed_packet=auto,system_time_zone=auto,time_zone=auto,tx_isolation=auto,maxscale=auto`
* Dynamic: Yes
* Mandatory: No

[**port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: No
* Default: `0`

[**protocol**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: protocol
* Mandatory: No
* Dynamic: No
* Default: `mariadb`

[**service**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

[**socket**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `port` is not provided.
* Dynamic: No
* Default: `""`

[**sql\_mode**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `default`, `oracle`
* Default: `default`

[**user\_mapping\_file**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

**Server**

[**address**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `socket` is not provided.
* Dynamic: Yes
* Default: `""`

[**disk\_space\_threshold**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: Custom
* Mandatory: No
* Dynamic: No
* Default: None

[**extra\_port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_routing\_connections**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**monitorpw**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**monitoruser**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**persistmaxtime**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**persistpoolmax**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `3306`

[**priority**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**private\_address**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**proxy\_protocol**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**rank**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `primary`, `secondary`
* Default: `primary`

[**replication\_custom\_options**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Default: None
* Dynamic: Yes

[**socket**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes, if `address` is not provided.
* Dynamic: Yes
* Default: `""`

**Service**

[**auth\_all\_servers**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**cluster**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: monitor
* Mandatory: No
* Dynamic: Yes
* Default: None

[**connection\_keepalive**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`
* Auto tune: [Yes](../maxscale-management/deployment/maxscale-configuration-guide.md)

[**disable\_sescmd\_history**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enable\_root\_user**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**filters**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: filter list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**force\_connection\_keepalive**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**idle\_session\_pool\_time**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `-1s`

[**log\_auth\_warnings**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**log\_debug**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_info**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_notice**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_warning**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**max\_connections**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_sescmd\_history**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `50`

[**multiplex\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

[**net\_write\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [durations](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory No
* Dynamic: Yes
* Default: `0s`

[**password**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**prune\_sescmd\_history**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_last\_statements**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**router**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: router
* Mandatory: Yes
* Dynamic: No

[**servers**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: server list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**session\_track\_trx\_state**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**strip\_db\_esc**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**targets**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: target list
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user\_accounts\_file**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**user\_accounts\_file\_usage**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `add_when_load_ok`, `file_only_always`
* Default: `add_when_load_ok`

[**version\_string**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: None

[**wait\_timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`
* Auto tune: [Yes](../maxscale-management/deployment/maxscale-configuration-guide.md)

**Settings for File-based Key Manager**

[**file.keyfile**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

**Settings for HashiCorp Vault Key Manager**

[**vault.ca**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**vault.host**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Default: `localhost`
* Dynamic: Yes

[**vault.mount**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Default: `secret`
* Dynamic: Yes

[**vault.port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: integer
* Default: `8200`
* Dynamic: Yes

[**vault.timeout**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Default: 30s
* Dynamic: Yes

[**vault.tls**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: true
* Dynamic: Yes

[**vault.token**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: password
* Mandatory: Yes
* Dynamic: Yes

**Settings for KMIP Key Manager**

[**kmip.ca**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Default: `""`
* Dynamic: Yes

[**kmip.cert**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.host**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**kmip.key**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**kmip.port**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: integer
* Mandatory: Yes
* Dynamic: Yes

**Settings for TLS/SSL Encryption**

[**ssl**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ssl\_ca**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_cert\_verify\_depth**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`

[**ssl\_cipher**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_crl**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_key**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ssl\_verify\_peer\_certificate**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ssl\_verify\_peer\_host**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`

[**ssl\_version**](../maxscale-management/deployment/maxscale-configuration-guide.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`

### Authenticators

#### [Authentication-Modules](https://github.com/mariadb-corporation/docs-server/blob/test/en/maxscale-25-01-authentication-modules/README.md)

**Settings**

[**lower\_case\_table\_names**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#lower_case_table_names)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `0`

[**match\_host**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#match_host)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**skip\_authentication**](https://mariadb.com/kb/en/maxscale-25-01-authentication-modules/#skip_authentication)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [GSSAPI-Authenticator](maxscale-authenticators/maxscale-gssapi-client-authenticator.md)

**Settings**

[**gssapi\_keytab\_path**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: Kerberos Default

[**principal\_name**](maxscale-authenticators/maxscale-gssapi-client-authenticator.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `mariadb/localhost.localdomain`

#### [MySQL-Authenticator](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)

**Settings**

[**log\_password\_mismatch**](maxscale-authenticators/maxscale-mariadb-mysql-authenticator.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

#### [PAM-Authenticator](maxscale-authenticators/maxscale-pam-authenticator.md)

**Settings**

[**pam\_backend\_mapping**](maxscale-authenticators/maxscale-pam-authenticator.md)

* Type: [enumeration](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `mariadb`
* Default: `none`

[**pam\_mapped\_pw\_file**](maxscale-authenticators/maxscale-pam-authenticator.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: None

[**pam\_mode**](maxscale-authenticators/maxscale-pam-authenticator.md)

* Type: [enumeration](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `password`, `password_2FA`, `suid`
* Default: `password`

[**pam\_use\_cleartext\_plugin**](maxscale-authenticators/maxscale-pam-authenticator.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

### Filters

#### [BinlogFilter](maxscale-filters/maxscale-binlog-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-binlog-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-binlog-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_dest**](maxscale-filters/maxscale-binlog-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rewrite\_src**](maxscale-filters/maxscale-binlog-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [CCRFilter](maxscale-filters/maxscale-consistent-critical-read-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**global**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**ignore**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**options**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**time**](maxscale-filters/maxscale-consistent-critical-read-filter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `60s`

#### [Cache](maxscale-filters/maxscale-cache.md)

**Settings**

[**cache\_in\_transactions**](maxscale-filters/maxscale-cache.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `read_only_transactions`, `all_transactions`
* Default: `all_transactions`

[**cached\_data**](maxscale-filters/maxscale-cache.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `shared`, `thread_specific`
* Default: `thread_specific`

[**clear\_cache\_on\_parse\_errors**](maxscale-filters/maxscale-cache.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**debug**](maxscale-filters/maxscale-cache.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**enabled**](maxscale-filters/maxscale-cache.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**hard\_ttl**](maxscale-filters/maxscale-cache.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**invalidate**](maxscale-filters/maxscale-cache.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `never`, `current`
* Default: `never`

[**max\_count**](maxscale-filters/maxscale-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_rows**](maxscale-filters/maxscale-cache.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_resultset\_size**](maxscale-filters/maxscale-cache.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**max\_size**](maxscale-filters/maxscale-cache.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)

[**rules**](maxscale-filters/maxscale-cache.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""` (no rules)

[**selects**](maxscale-filters/maxscale-cache.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `assume_cacheable`, `verify_cacheable`
* Default: `assume_cacheable`

[**soft\_ttl**](maxscale-filters/maxscale-cache.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s` (no limit)

[**storage**](maxscale-filters/maxscale-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `storage_inmemory`

[**storage\_options**](maxscale-filters/maxscale-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default:

[**timeout**](maxscale-filters/maxscale-cache.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `5s`

[**users**](maxscale-filters/maxscale-cache.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `mixed`, `isolated`
* Default: `mixed`

**`storage_memcached`**

[**max\_value\_size**](maxscale-filters/maxscale-cache.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: 1Mi

[**server**](maxscale-filters/maxscale-cache.md)

* Type: The Memcached server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

**`storage_redis`**

[**password**](maxscale-filters/maxscale-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**server**](maxscale-filters/maxscale-cache.md)

* Type: The Redis server address specified as `host[:port]`
* Mandatory: Yes
* Dynamic: No

[**ssl**](maxscale-filters/maxscale-cache.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**ssl\_ca**](maxscale-filters/maxscale-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_cert**](maxscale-filters/maxscale-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**ssl\_key**](maxscale-filters/maxscale-cache.md)

* Type: Path to existing readable file.
* Mandatory: No
* Dynamic: No
* Default: `""`

[**username**](maxscale-filters/maxscale-cache.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

#### [Comment](maxscale-filters/maxscale-comment-filter.md)

**Settings**

[**inject**](maxscale-filters/maxscale-comment-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

#### [LDIFilter](maxscale-filters/maxscale-ldi-filter.md)

**Settings**

[**host**](maxscale-filters/maxscale-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `s3.amazonaws.com`

[**key**](maxscale-filters/maxscale-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**no\_verify**](maxscale-filters/maxscale-ldi-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**port**](maxscale-filters/maxscale-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0

[**protocol\_version**](maxscale-filters/maxscale-ldi-filter.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 0
* Values: 0, 1, 2

[**region**](maxscale-filters/maxscale-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `us-east-1`

[**secret**](maxscale-filters/maxscale-ldi-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes

[**use\_http**](maxscale-filters/maxscale-ldi-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

#### [Masking](maxscale-filters/maxscale-masking-filter.md)

**Settings**

[**check\_subqueries**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_unions**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**check\_user\_variables**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**large\_payload**](maxscale-filters/maxscale-masking-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `abort`
* Default: `abort`

[**prevent\_function\_usage**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**require\_fully\_parsed**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**rules**](maxscale-filters/maxscale-masking-filter.md)

* Type: path
* Mandatory: Yes
* Dynamic: Yes

[**treat\_string\_arg\_as\_field**](maxscale-filters/maxscale-masking-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**warn\_type\_mismatch**](maxscale-filters/maxscale-masking-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `never`, `always`
* Default: `never`

#### [Maxrows](maxscale-filters/maxscale-maxrows-filter.md)

**Settings**

[**debug**](maxscale-filters/maxscale-maxrows-filter.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `0`

[**max\_resultset\_return**](maxscale-filters/maxscale-maxrows-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `empty`, `error`, `ok`
* Default: `empty`

[**max\_resultset\_rows**](maxscale-filters/maxscale-maxrows-filter.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: (no limit)

[**max\_resultset\_size**](maxscale-filters/maxscale-maxrows-filter.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: `64Ki`

#### [Named-Server-Filter](maxscale-filters/maxscale-named-server-filter.md)

**Settings**

[**matchXY**](maxscale-filters/maxscale-named-server-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-named-server-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**source**](maxscale-filters/maxscale-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**targetXY**](maxscale-filters/maxscale-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-named-server-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Query-Log-All-Filter](maxscale-filters/maxscale-query-log-all-filter.md)

**Settings**

[**append**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**duration\_unit**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

[**exclude**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**flush**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**log\_data**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

[**log\_type**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

[**match**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**newline\_replacement**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

[**options**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

[**separator**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

[**source**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**source\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**source\_match**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**use\_canonical\_form**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [bool](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**user**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**user\_exclude**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

[**user\_match**](maxscale-filters/maxscale-query-log-all-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

#### [Regex-Filter](maxscale-filters/maxscale-regex-filter.md)

**Settings**

[**log\_file**](maxscale-filters/maxscale-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**log\_trace**](maxscale-filters/maxscale-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-regex-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: Yes
* Dynamic: Yes

[**options**](maxscale-filters/maxscale-regex-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**replace**](maxscale-filters/maxscale-regex-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**source**](maxscale-filters/maxscale-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-regex-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [RewriteFilter](maxscale-filters/maxscale-rewrite-filter.md)

**Settings**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**log\_replacement**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: Native
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`

[**template\_file**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes
* Default: No default value

**Settings per template in the template file**

[**case\_sensitive**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: From maxscale.cnf

[**continue\_if\_matched**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false

[**ignore\_whitespace**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: true

[**regex\_grammar**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: string
* Values: `Native`, `ECMAScript`, `Posix`, `EPosix`, `Awk`, `Grep`, `EGrep`
* Default: From maxscale.cnf

[**what\_if**](maxscale-filters/maxscale-rewrite-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false

#### [Tee-Filter](maxscale-filters/maxscale-tee-filter.md)

**Settings**

[**exclude**](maxscale-filters/maxscale-tee-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**match**](maxscale-filters/maxscale-tee-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-tee-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `ignorecase`, `case`, `extended`
* Default: `ignorecase`

[**service**](maxscale-filters/maxscale-tee-filter.md)

* Type: service
* Mandatory: No
* Dynamic: Yes
* Default: none

[**source**](maxscale-filters/maxscale-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**sync**](maxscale-filters/maxscale-tee-filter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**target**](maxscale-filters/maxscale-tee-filter.md)

* Type: target
* Mandatory: No
* Dynamic: Yes
* Default: none

[**user**](maxscale-filters/maxscale-tee-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Throttle](maxscale-filters/maxscale-throttle-filter.md)

**Settings**

[**continuous\_duration**](maxscale-filters/maxscale-throttle-filter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 2s

[**max\_qps**](maxscale-filters/maxscale-throttle-filter.md)

* Type: number
* Mandatory: Yes
* Dynamic: Yes

[**sampling\_duration**](maxscale-filters/maxscale-throttle-filter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 250ms

[**throttling\_duration**](maxscale-filters/maxscale-throttle-filter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: Yes
* Dynamic: Yes

#### [Top-N-Filter](maxscale-filters/maxscale-top-filter.md)

**Settings**

[**count**](maxscale-filters/maxscale-top-filter.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `10`

[**exclude**](maxscale-filters/maxscale-top-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**filebase**](maxscale-filters/maxscale-top-filter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**match**](maxscale-filters/maxscale-top-filter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

[**options**](maxscale-filters/maxscale-top-filter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `ignorecase`, `case`, `extended`
* Default: `case`

[**source**](maxscale-filters/maxscale-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**user**](maxscale-filters/maxscale-top-filter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

#### [Wcar](maxscale-filters/maxscale-workload-capture-and-replay.md)

**Settings**

[**capture\_dir**](maxscale-filters/maxscale-workload-capture-and-replay.md)

* Type: path
* Default: /var/lib/maxscale/wcar/
* Mandatory: No
* Dynamic: No

[**capture\_duration**](maxscale-filters/maxscale-workload-capture-and-replay.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Default: 0s
* Mandatory: No
* Dynamic: No

[**capture\_size**](maxscale-filters/maxscale-workload-capture-and-replay.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Default: 0
* Mandatory: No
* Dynamic: No

[**start\_capture**](maxscale-filters/maxscale-workload-capture-and-replay.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Mandatory: No
* Dynamic: No

### Monitors

#### [Galera-Monitor](maxscale-monitors/galera-monitor.md)

**Settings**

[**available\_when\_donor**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**disable\_master\_failback**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**disable\_master\_role\_setting**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**root\_node\_as\_master**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**set\_donor\_nodes**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

[**use\_priority**](maxscale-monitors/galera-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Default: false
* Dynamic: Yes

#### [MariaDB-Monitor](maxscale-monitors/mariadb-monitor.md)

**Settings**

[**assume\_unique\_hostnames**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**cooperative\_monitoring\_locks**](maxscale-monitors/mariadb-monitor.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `majority_of_all`, `majority_of_running`
* Default: `none`

[**enforce\_read\_only\_servers**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_read\_only\_slaves**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**enforce\_writable\_master**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failcount**](maxscale-monitors/mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `5`

[**maintenance\_on\_low\_disk\_space**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_conditions**](maxscale-monitors/mariadb-monitor.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `connecting_slave`, `connected_slave`, `running_slave`, `primary_monitor_master`, `disk_space_ok`
* Default: `primary_monitor_master, disk_space_ok`

[**script\_max\_replication\_lag**](maxscale-monitors/mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `-1`

[**slave\_conditions**](maxscale-monitors/mariadb-monitor.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `linked_master`, `running_master`, `writable_master`, `primary_monitor_master`
* Default: `none`

**Settings for Backup operations**

[**backup\_storage\_address**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**backup\_storage\_path**](maxscale-monitors/mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**rebuild\_port**](maxscale-monitors/mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `4444`

[**ssh\_check\_host\_key**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**ssh\_keyfile**](maxscale-monitors/mariadb-monitor.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: None

[**ssh\_port**](maxscale-monitors/mariadb-monitor.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `22`

[**ssh\_timeout**](maxscale-monitors/mariadb-monitor.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**ssh\_user**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

**Settings for Cluster manipulation operations**

[**auto\_failover**](maxscale-monitors/mariadb-monitor.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `true`, `on`, `yes`, `1`, `false`, `off`, `no`, `0`, `safe`
* Default: `false`

[**auto\_rejoin**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**demotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**enforce\_simple\_topology**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**failover\_timeout**](maxscale-monitors/mariadb-monitor.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**handle\_events**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**master\_failure\_timeout**](maxscale-monitors/mariadb-monitor.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**promotion\_sql\_file**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_master\_ssl**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**replication\_password**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**replication\_user**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**servers\_no\_promotion**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**switchover\_on\_low\_disk\_space**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**switchover\_timeout**](maxscale-monitors/mariadb-monitor.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**verify\_master\_failure**](maxscale-monitors/mariadb-monitor.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

**Settings for Primary server write test**

[**write\_test\_fail\_action**](maxscale-monitors/mariadb-monitor.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Default: `log`
* Values: `log`, `failover`
* Dynamic: Yes

[**write\_test\_interval**](maxscale-monitors/mariadb-monitor.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Dynamic: Yes
* Default: 0s

[**write\_test\_table**](maxscale-monitors/mariadb-monitor.md)

* Type: string
* Dynamic: Yes
* Default: `mxs.maxscale_write_test`

#### [Monitor-Common](maxscale-monitors/common-monitor-parameters.md)

**Settings**

[**backend\_connect\_attempts**](maxscale-monitors/common-monitor-parameters.md)

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `1`

[**backend\_connect\_timeout**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_read\_timeout**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**backend\_write\_timeout**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `3s`

[**disk\_space\_check\_interval**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `0s`

[**disk\_space\_threshold**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**events**](maxscale-monitors/common-monitor-parameters.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master_down`, `master_up`, `slave_down`, `slave_up`, `server_down`, `server_up`, `lost_master`, `lost_slave`, `new_master`, `new_slave`
* Default: All events

[**journal\_max\_age**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `28800s`

[**module**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**monitor\_interval**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `2s`

[**password**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**script**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: None

[**script\_timeout**](maxscale-monitors/common-monitor-parameters.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `90s`

[**servers**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**user**](maxscale-monitors/common-monitor-parameters.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

### Protocols

#### [MariaDB](maxscale-protocols/maxscale-mariadb-protocol-module.md)

**Settings**

[**allow\_replication**](maxscale-protocols/maxscale-mariadb-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

#### [NoSQL](maxscale-protocols/maxscale-nosql-protocol-module.md)

**Settings**

[**authentication\_db**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"NoSQL"`

[**authentication\_key\_id**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_password**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**authentication\_required**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**authentication\_shared**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**authentication\_user**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: Yes, if `authentication_shared` is true.

[**authorization\_enabled**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**auto\_create\_databases**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

[**auto\_create\_tables**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `true`

[**cursor\_timeout**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Default: `60s`

[**debug**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `none`, `in`, `out`, `back`
* Default: `none`

[**host**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `"%"`

[**id\_length**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: count
* Mandatory: No
* Range: `[35, 2048]`
* \*Default: `35`

[**internal\_cache**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: ''

[**log\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: `false`

[**on\_unknown\_command**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `return_error`, `return_empty`
* Default: `return_error`

[**ordered\_insert\_behavior**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Values: `atomic`, `default`
* Default: `default`

[**password**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

[**user**](maxscale-protocols/maxscale-nosql-protocol-module.md)

* Type: string
* Mandatory: No
* Default: `""`

### Routers

#### [Binlogrouter](maxscale-routers/maxscale-binlogrouter.md)

**Settings**

[**archivedir**](maxscale-routers/maxscale-binlogrouter.md)

* Type: string
* Mandatory: Yes
* Default: No
* Dynamic: No

[**compression\_algorithm**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `none`, `zstandard`
* Default: `none`

[**datadir**](maxscale-routers/maxscale-binlogrouter.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `/var/lib/maxscale/binlogs`

[**ddl\_only**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: false

[**encryption\_cipher**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `AES_CBC`, `AES_CTR`, `AES_GCM`
* Default: `AES_GCM`

[**encryption\_key\_id**](maxscale-routers/maxscale-binlogrouter.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**expiration\_mode**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Dynamic: No
* Values: `purge`, `archive`
* Default: `purge`

[**expire\_log\_duration**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `0s`

[**expire\_log\_minimum\_files**](maxscale-routers/maxscale-binlogrouter.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `2`

[**net\_timeout**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `10s`

[**number\_of\_noncompressed\_files**](maxscale-routers/maxscale-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `2`

[**rpl\_semi\_sync\_slave\_enabled**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Default: false
* Dynamic: Yes

[**select\_master**](maxscale-routers/maxscale-binlogrouter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**server\_id**](maxscale-routers/maxscale-binlogrouter.md)

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `1234`

#### [Diff](maxscale-routers/maxscale-diff.md)

**Settings**

[**explain**](maxscale-routers/maxscale-diff.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `other`, \`both'
* Default: `both`

[**explain\_entries**](maxscale-routers/maxscale-diff.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 2

[**explain\_period**](maxscale-routers/maxscale-diff.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 15m

[**main**](maxscale-routers/maxscale-diff.md)

* Type: server
* Mandatory: Yes
* Dynamic: No

[**max\_request\_lag**](maxscale-routers/maxscale-diff.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 10

[**on\_error**](maxscale-routers/maxscale-diff.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `close`, `ignore`
* Default: `ignore`

[**percentile**](maxscale-routers/maxscale-diff.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 1
* Max: 100
* Default: 99

[**qps\_window**](maxscale-routers/maxscale-diff.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: 15m

[**report**](maxscale-routers/maxscale-diff.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_discrepancy`, `never`
* Default: `on_discrepancy`

[**reset\_replication**](maxscale-routers/maxscale-diff.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

[**retain\_faster\_statements**](maxscale-routers/maxscale-diff.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**retain\_slower\_statements**](maxscale-routers/maxscale-diff.md)

* Type: non-negative integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**samples**](maxscale-routers/maxscale-diff.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Min: 100
* Default: 1000

[**service**](maxscale-routers/maxscale-diff.md)

* Type: service
* Mandatory: Yes
* Dynamic: No

#### [KafkaCDC](maxscale-routers/maxscale-kafkacdc.md)

**Settings**

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

[**cooperative\_replication**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**enable\_idempotence**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**exclude**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**gtid**](maxscale-routers/maxscale-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkacdc.md)

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkacdc.md)

* Type: path
* Mandatory: No
* Dynamic: No
* Default: `""`

[**match**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**read\_gtid\_from\_kafka**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`

[**send\_schema**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**server\_id**](maxscale-routers/maxscale-kafkacdc.md)

* Type: number
* Mandatory: No
* Dynamic: No
* Default: `1234`

[**timeout**](maxscale-routers/maxscale-kafkacdc.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `10s`

[**topic**](maxscale-routers/maxscale-kafkacdc.md)

* Type: string
* Mandatory: Yes
* Dynamic: No

#### [KafkaImporter](maxscale-routers/maxscale-kafkaimporter.md)

**Settings**

[**batch\_size**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `100`

[**bootstrap\_servers**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: string
* Mandatory: Yes
* Dynamic: Yes

[**engine**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: string
* Default: `InnoDB`
* Mandatory: No
* Dynamic: Yes

[**kafka\_sasl\_mechanism**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

[**kafka\_sasl\_password**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_sasl\_user**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

[**kafka\_ssl\_ca**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_cert**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**kafka\_ssl\_key**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**table\_name\_in**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `topic`, `key`
* Default: `topic`

[**timeout**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `5000ms`

[**topics**](maxscale-routers/maxscale-kafkaimporter.md)

* Type: stringlist
* Mandatory: Yes
* Dynamic: Yes

#### [Mirror](maxscale-routers/maxscale-mirror.md)

**Settings**

[**exporter**](maxscale-routers/maxscale-mirror.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: Yes
* Dynamic: Yes
* Values: `log`, `file`, `kafka`

[**file**](maxscale-routers/maxscale-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_broker**](maxscale-routers/maxscale-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**kafka\_topic**](maxscale-routers/maxscale-mirror.md)

* Type: string
* Default: No default value
* Mandatory: No
* Dynamic: Yes

[**main**](maxscale-routers/maxscale-mirror.md)

* Type: target
* Mandatory: Yes
* Dynamic: Yes

[**on\_error**](maxscale-routers/maxscale-mirror.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Default: `ignore`
* Mandatory: No
* Dynamic: Yes
* Values: `ignore`, `close`

[**report**](maxscale-routers/maxscale-mirror.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Default: `always`
* Mandatory: No
* Dynamic: Yes
* Values: `always`, `on_conflict`

#### [ReadConnRoute](maxscale-routers/maxscale-readconnroute.md)

**Settings**

[**master\_accept\_reads**](maxscale-routers/maxscale-readconnroute.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**max\_replication\_lag**](maxscale-routers/maxscale-readconnroute.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**router\_options**](maxscale-routers/maxscale-readconnroute.md)

* Type: [enum\_mask](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `slave`, `synced`, `running`
* Default: `running`

#### [ReadWriteSplit](maxscale-routers/maxscale-readwritesplit.md)

**Settings**

[**causal\_reads**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `none`, `local`, `global`, `fast`, `fast_global`, `universal`, `fast_universal`
* Default: `none`

[**causal\_reads\_timeout**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**delayed\_retry**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**delayed\_retry\_timeout**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 10s

[**lazy\_connect**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_accept\_reads**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**master\_failure\_mode**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `fail_instantly`, `fail_on_write`, `error_on_write`
* Default: `fail_on_write` (MaxScale 23.08: `fail_instantly`)

[**master\_reconnection**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false(<= MaxScale 23.08)

[**max\_replication\_lag**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 0s

[**max\_slave\_connections**](maxscale-routers/maxscale-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**retry\_failed\_reads**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**slave\_connections**](maxscale-routers/maxscale-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 255

[**slave\_selection\_criteria**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `least_current_operations`, `adaptive_routing`, `least_behind_master`, `least_router_connections`, `least_global_connections`
* Default: `least_current_operations`

[**strict\_multi\_stmt**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_sp\_calls**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**strict\_tmp\_tables**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true (>= MaxScale 24.02), false (<= MaxScale 23.08)

[**transaction\_replay**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_attempts**](maxscale-routers/maxscale-readwritesplit.md)

* Type: integer
* Mandatory: No
* Dynamic: Yes
* Default: 5

[**transaction\_replay\_checksum**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `full`, `result_only`, `no_insert_id`
* Default: `full`

[**transaction\_replay\_max\_size**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [size](../maxscale-management/deployment/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: Yes
* Default: 1 MiB

[**transaction\_replay\_retry\_on\_deadlock**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_retry\_on\_mismatch**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**transaction\_replay\_safe\_commit**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: true

[**transaction\_replay\_timeout**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 30s (>= MaxScale 24.02), 0s (<= MaxScale 23.08)

[**use\_sql\_variables\_in**](maxscale-routers/maxscale-readwritesplit.md)

* Type: [enum](../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `master`, `all`
* Default: `all`

#### [SchemaRouter](maxscale-routers/maxscale-schemarouter.md)

**Settings**

[**allow\_duplicates**](maxscale-routers/maxscale-schemarouter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: false

[**ignore\_tables**](maxscale-routers/maxscale-schemarouter.md)

* Type: stringlist
* Mandatory: No
* Dynamic: Yes
* Default: `""`

[**ignore\_tables\_regex**](maxscale-routers/maxscale-schemarouter.md)

* Type: [regex](../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: No
* Default: `""`

[**max\_staleness**](maxscale-routers/maxscale-schemarouter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: 150s

[**refresh\_databases**](maxscale-routers/maxscale-schemarouter.md)

* Type: [boolean](../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`

[**refresh\_interval**](maxscale-routers/maxscale-schemarouter.md)

* Type: [duration](../maxscale-management/deployment/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: Yes
* Default: `300s`

#### [SmartRouter](maxscale-routers/maxscale-smartrouter.md)

**Settings**

[**master**](maxscale-routers/maxscale-smartrouter.md)

* Type: target
* Mandatory: Yes
* Dynamic: No

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
