---
description: >-
  Format and supported arguments for the GridGain 9 ODBC driver connection
  string, with connection string samples.
---

# Connection String

## Connection String Format

The ODBC Driver supports standard connection string format. Here is the formal syntax:

```
connection-string ::= empty-string[;] | attribute[;] | attribute; connection-string
empty-string ::=
attribute ::= attribute-keyword=attribute-value | DRIVER=[{]attribute-value[}]
attribute-keyword ::= identifier
attribute-value ::= character-string
```

In simple terms, an ODBC connection URL is a string with parameters of the choice separated by semicolon.

## Supported Arguments

The ODBC driver supports and uses several connection string/DSN arguments. All parameter names are case-insensitive - `ADDRESS`, `Address`, and `address` all are valid parameter names and refer to the same parameter. If an argument is not specified, the default value is used. The exception to this rule is the `ADDRESS` attribute. If it is not specified, `SERVER` and `PORT` attributes are used instead.

| Attribute keyword | Description | Default Value |
| --- | --- | --- |
| `ADDRESS` | Address of the remote node to connect to. The format is: `<host>[:<port>]`. For example: `localhost`, `example.com:12345`, `127.0.0.1`, `192.168.3.80:5893`. If this attribute is specified, then `SERVER` and `PORT` arguments are ignored. | None. |
| `SERVER` | Address of the node to connect to. This argument value is ignored if ADDRESS argument is specified. | None. |
| `PORT` | Port on which `OdbcProcessor` of the node is listening. This argument value is ignored if `ADDRESS` argument is specified. | `10800` |
| IDENTITY | Identity to use for authentication. Depending on the authenticator used on the server side, it can be a user name or another unique identifier. See the [Authentication](../../../administrators-guide/security/authentication.md) topic for details. | None. |
| SECRET | Secret to use for authentication. Depending on the authenticator used on the server side, it can be a user password or another type of user-specific secret. See the [Authentication](../../../administrators-guide/security/authentication.md) topic for details. | None. |
| `SCHEMA` | Schema name. | `PUBLIC` |
| `PAGE_SIZE` | Number of rows returned in response to a fetching request to the data source. Default value should be fine in most cases. Setting a low value can result in slow data fetching while setting a high value can result in additional memory usage by the driver, and additional delay when the next page is being retrieved. | `1024` |
| `HEARTBEAT_INTERVAL` | The interval in milliseconds between heartbeat messages sent by the ODBC client. Minimum value is 500. Set to 0 to disable heartbeat messages. | `30000` (30 seconds) |
| `SSL_MODE` | Determines whether the SSL connection should be negotiated with the server. Use `require` or `disable` mode as needed. | `disable`. |
| `SSL_KEY_FILE` | Specifies the path to the file containing the SSL server private key. | None. |
| `SSL_CERT_FILE` | Specifies the path to the file containing the SSL server certificate. | None. |
| `SSL_CA_FILE` | Specifies the path to the file containing the SSL server certificate authority (CA). | None. |

## Connection String Samples

You can find samples of the connection string below. These strings can be used with `SQLDriverConnect` ODBC call to establish connection with a node.

{% tabs %}
{% tab title="Specific schema" %}
```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800;SCHEMA=yourSchemaName
```
{% endtab %}

{% tab title="Default schema" %}
```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800
```
{% endtab %}

{% tab title="Authentication" %}
```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800;IDENTITY=yourid;SECRET=yoursecret
```
{% endtab %}

{% tab title="Custom page size" %}
```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800;SCHEMA=yourSchemaName;PAGE_SIZE=4096
```
{% endtab %}
{% endtabs %}
