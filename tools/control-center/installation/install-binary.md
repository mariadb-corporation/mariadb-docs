---
description: >-
  Installing GridGain Control Center from the binary package, including work
  folder, URI, port, and SSL configuration.
---

# Control Center Binary Package

## Downloading and Installing the Binary Package

1. Obtain the Control Center binaries and license from our [Sales](https://www.gridgain.com/contact).
2. Unpack the archive into a directory of your choice (“installation directory”).
3. Once you have unpacked the package, launch Control Center by running `control-center.sh` (or `control-center.bat` for Windows) in the installation directory.

{% hint style="info" %}
Control Center requires that you have a Java x64 installed and `JAVA_HOME` configured.
{% endhint %}

Control Center starts with the default configuration and listens on the default port (3000). Open `http://localhost:3000` in your browser and sign up for an account.

{% hint style="warning" %}
When Control Center starts, it creates a directory named “work” in the installation directory. This directory contains all user data, logs, screen and widget configuration, etc. You would want to keep that directory when upgrading to a newer version of Control Center.
{% endhint %}

## Explicitly Defining Your Work Folder

By default, Control Center stores all data in `$CC_ROOT/work`. However, we recommend using a folder outside of the default location to simplify version update operations. To change the default `work` folder, do one of the following:

- Define the `IGNITE_WORK_DIR` environment variable; for example:

  `IGNITE_WORK_DIR=/path/to/cc/work $CC_ROOT/control-center.sh`

  Define the `JAVA_OPTS` env variable; for example:

  `JAVA_OPTS="${JAVA_OPTS} -DIGNITE_WORK_DIR=/path/to/cc/work" $CC_ROOT/control-center.sh`
- Explicitly define the work folder in `$CC_ROOT/ignite-config.xml`:

  ```xml
  <bean class="org.apache.ignite.configuration.IgniteConfiguration">
      ...
      <property name="workDirectory" value="/your/path/to/cc-work"/>
  ```

## Setting Control Center URI

The Control Center URI is the URI where the GridGain Control Center is running. Your clusters will need to know this URI to be able to establish connection with Control Center.

Set the URI by using the management script:

```bash
{GRIDGAIN_HOME}/bin/management.sh --uri http://localhost:3000
```

Note the ID of the cluster in the node output. You will need it to add the cluster in the Control Center UI. See [Connecting a Cluster](../cluster-management.md#adding-clusters).

You can also set the URI in System Properties: `-Dcontrol.center.agent.uris=https://portal-test.gridgain.com`.

{% hint style="info" %}
This option works only when you are launching a new cluster. Restarting an already running cluster and adding this System Property will not work.
{% endhint %}

## Open Port Requirements

To ensure proper Control Center operation, port 3000 must be open for the system's backend.

## SSL Configuration

To configure SSL for the on-premise version of GridGain Control Center:

1. Create an `application.properties` file in the Control Center root folder.
2. Add the following lines to the file:

   ```properties
   server.port=
   server.ssl.client-auth=need
   server.ssl.protocol=TLS
   server.ssl.key-store-type=JKS
   server.ssl.key-store=node.jks
   server.ssl.key-store-password={safe_password}
   server.ssl.trust-store-type=JKS
   server.ssl.trust-store=trust.jks
   server.ssl.trust-store-password={safe_password}
   ```
3. Run the following command:

   ```bash
   bash control-center.sh
   ```

   Control Center is started at https://localhost:3000.
4. Navigate to the cluster you want to connect and use the [management.sh utility](../admin-guide/command-line.md#connection-options) to override the Control Center URI:

   ```bash
   ${GG_ROOT}/bin/management.sh --uri https://localhost:3000
   ```
5. If you have used a self-signed certificate in Control Center, make sure that this certificate is present in truststore used by the Control Center agent at the cluster side. You can import the self-signed certificate into separate truststore file and expose it to the Control Center:

   ```bash
   ${GG_ROOT}/bin/management.sh --uri https://localhost:3000 --management-truststore /path/to/truststore.jks --management-truststore-password changeit
   ```

### Configuring SSL Without Management Script

If `management.sh` is not used, Control Center settings can be provided at JVM startup using system properties.

- To configure the Control Center Agent endpoint, set:

  ```bash
  -Dcontrol.center.agent.uris=https://<host>:<port>
  ```
- To configure SSL truststore and keystore settings, use standard JSSE system properties:

  ```bash
  -Djavax.net.ssl.trustStore=/path/to/truststore.jks
  -Djavax.net.ssl.trustStorePassword=<password>
  -Djavax.net.ssl.keyStore=/path/to/keystore.jks
  -Djavax.net.ssl.keyStorePassword=<password>
  ```

## Next Steps

- [Change Configuration Parameters](../admin-guide/configuration.md) - make sure you [optimize the disk space utilization](../admin-guide/disk-space-optimization.md)
- [Add a License](../getting-started/adding-license.md)
- Connect a [GridGain](../getting-started/connect/connect-gridgain-cluster.md) or [Apache Ignite](../getting-started/connect/connect-ignite-cluster.md) Cluster
