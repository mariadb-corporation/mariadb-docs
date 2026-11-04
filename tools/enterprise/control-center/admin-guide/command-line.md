---
description: >-
  The management.sh|bat Control Center Agent management tool: commands,
  connection options, and basic options.
---

# Control Center Agent Management Tool

The `management.sh|bat` script is part of GridGain used to configure connections to Control Center. It is located in the GridGain `bin` folder.

You can define the `management.sh|bat` log directory via an environment variable:

{% tabs %}
{% tab title="Linux/Unix" %}
```bash
$ MANAGEMENT_JVM_OPTS=-Djava.util.logging.config.file=<PATH_TO_CONFIG> ./management.sh
```
{% endtab %}

{% tab title="Windows" %}
```bash
$ MANAGEMENT_JVM_OPTS=-Djava.util.logging.config.file=<PATH_TO_CONFIG> ./management.bat
```
{% endtab %}
{% endtabs %}

## Commands

Options in this section specify the command to the script.

| Command | Description |
|---|---|
| --uri | Specifies the URI that the agent will use to connect to Control Center. |
| --off | Disables Control Center Agent and stops any active connections. |
| --on | Enables Control Center Agent and tries to connect to known clusters. Uses previously configured connection parameters. |
| --status | Prints information about current connection status and the connection parameters. |
| --token | Generates a new connection token that can be used to attach clusters to Control Center. New token is printed as a part of the output of this command. |

## Connection Options

Options in this section configure the connection between the cluster and Control Center. Can only be specified if `--uri` is specified.

| Parameter | Description |
|---|---|
| --management-cipher-suites | The list of cipher suites for management.sh. You can find the full list of supported suites in [Java documentation](https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#jsse-cipher-suite-names). Example of multiple cipher suites: `--management-cipher-suites TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_DH_DSS_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384`. |
| --management-keystore-type | The type of keystore to use for management.sh. You can find the full list in [Java Documentation](https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#keystore-types). |
| --management-keystore | Path to the keystore file. Can be relative or absolute. |
| --management-keystore-password | Keystore password. Can only be in plaintext. |
| --management-truststore-type | The type of truststore to use. |
| --management-truststore | Path to the truststore file. Can be relative or absolute. |
| --management-truststore-password | Truststore password. Can only be in plaintext. |
| --management-session-timeout | Controls the maximum amount of time that can pass between action requests within the same security session in the cluster. It can be looked at as a maximum inactivity period. |
| --management-session-expiration-timeout | Specifies the amount of time when a security session in the cluster is considered valid. If this amount of time passes, then the session is expired even if it was actively used. It can be viewed as a “created TTL”. |

## Basic Options

Options below specify parameters for connection to a GridGain node by the CLI tool.

| Parameter | Description |
|---|---|
| --host | Host name or IP address of a GridGain node. |
| --port | Port number on the host of a GridGain node. |
| --user | The username that is used to authenticate user in the cluster. If credentials are not specified, they will be requested interactively. |
| --password | The password that is used to authenticate user in the cluster. If credentials are not specified, they will be requested interactively. |
| --verbose | When specified, detailed information about internal errors during command execution will be shown. |
| --ssl-protocol | SSL protocol to use for connections. Full list of supported SSL protocols can be found here in [Java documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SunJSSE_Protocols). For example, the following list is valid: `SSLv3,TLSv1` |
| --ssl-cipher-suites | The list of cipher suites that are used in SSL connection. You can find the full list of supported suites in [Java documentation](https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#jsse-cipher-suite-names). Example of multiple cipher suites: `--ssl-cipher-suites TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_DH_DSS_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384`. |
| --ssl-key-algorithm | Key algorithm used during SSL connection. Full list of supported algorithms can be found in [Java documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.html) under the KeyManagerFactory section. Default value: `SunX509`. |
| --keystore-type | The type of keystore to use. You can find the full list in [Java Documentation](https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#keystore-types). Default value: `JKS`. |
| --keystore | Path to the keystore file. Can be relative or absolute. |
| --keystore-password | Keystore password. Can only be in plaintext. |
| --truststore-type | The type of truststore to use. |
| --truststore | Path to the truststore file. Can be relative or absolute. |
| --truststore-password | Truststore password. Can only be in plaintext. |
| command | Script command. Possible commands are listed in the Command section. |
