---
description: >-
  GridGain 8.9.18 is a release fully dedicated to bringing vector search to your
  GridGain caches.
hidden: true
---

# GridGain 8.9.18 Release Notes

## Overview

GridGain 8.9.18 is a release fully dedicated to bringing vector search to your GridGain caches.

## Changes in Behavior

### Required Library for Java 8 Support

{% hint style="danger" %}
This change may cause issues during upgrade to this version if you are using Java 8.
{% endhint %}

Starting with this release, GridGain uses Lucene 9 by default. As Lucene 9 requires Java 11, it will be impossible to run GridGain on Java 8 with default configuration.

To continue using Java 8, replace the `{GRIDGAIN_HOME}/libs/ignite-lucene-9` folder with `{GRIDGAIN_HOME}/libs/optional/ignite-lucene-8`.

### Support for Full Text Search in Java 8

With this release, full text search is again supported when running Java 8.

## New Features

### Composite Authenticator

This release provides support for composite authenticator. You can use this authenticator to provide multiple ways of [authentication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) to the cluster.

The example below shows how you can configure composite authenticator:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.plugin.security.SecurityCredentials" id="server.cred">
    <constructor-arg value="server"/>
    <constructor-arg value="password"/>
</bean>

<bean class="org.apache.ignite.plugin.security.SecurityCredentials" id="client.cred">
    <constructor-arg value="client"/>
    <constructor-arg value="password"/>
</bean>

<bean id="grid.custom.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="pluginConfigurations">
         <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
           <property name="authenticator">
             <bean class="org.gridgain.grid.security.composite.CompositeAuthenticator">
               <property name="authenticators">
                 <list>

                   <bean class="org.gridgain.grid.security.passcode.PasscodeAuthenticator">
                     <property name="aclProvider">
                       <bean class="org.gridgain.grid.security.passcode.AuthenticationAclBasicProvider">
                         <constructor-arg>
                           <map>
                             <entry>
                               <key><ref bean="server.cred"/></key>
                               <value>{defaultAllow:false}</value>
                             </entry>
                             <entry>
                               <key><ref bean="client.cred"/></key>
							   <value>{defaultAllow:true}</value>
                             </entry>
                           </map>
                         </constructor-arg>
                       </bean>
                     </property>
                   </bean>

                   <bean class="org.gridgain.grid.security.certificate.CertificateAuthenticator">
                     <property name="permissionsJson">
                       <map>
                         <entry>
                           <key>
                             <bean class="org.gridgain.grid.security.certificate.SubjectRegexPredicate">
                               <constructor-arg type="java.lang.String" value="CN=client\\b.*"/>
                             </bean>
                           </key>
                           <value>{defaultAllow:true}</value>
                         </entry>
                       </map>
                     </property>
                   </bean>

                 </list>
               </property>
             </bean>
          </property>
         </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Configure passcode authentication.
SecurityCredentials serverCreds = new SecurityCredentials("server", "password");
SecurityCredentials clientCreds = new SecurityCredentials("client", "password");
GridPasscodeAuthenticator passcodeAuth = new GridPasscodeAuthenticator();
passcodeAuth.setAclProvider(new GridAuthenticationAclBasicProvider(
    F.asMap(serverCreds, "{defaultAllow:true}", clientCreds, "{defaultAllow:false}")));

// Configure certificate authentication.
CertificateAuthenticator certificateAuth = new CertificateAuthenticator();
certificateAuth.setPermissionsJson(
    F.asMap(new SubjectRegexPredicate("CN=client\\b.*"), "{defaultAllow:true}")
);

// Create a composite authenticator using both passcode and certificate authentication.
CompositeAuthenticator auth = new CompositeAuthenticator();
auth.setAuthenticators(F.asList(passcodeAuth, certificateAuth));


// Override default authentication.
GridPluginConfiguration pluginCfg = new GridPluginConfiguration();
pluginCfg.setAuthenticator(auth);

IgniteConfiguration igniteCfg = new IgniteConfiguration();
igniteCfg.setPluginConfigurations(igniteCfg);

// Start GridGain.
Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For more information on configuring composite authentication, see [Composite Authentication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication#composite-authentication)

### OpenID Authenticator

{% hint style="info" %}
This authenticator is designed to work with [Control Center](https://www.gridgain.com/docs/control-center/latest/overview) and is part of Control Center Agent [optional module](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/setup#enabling-modules).
{% endhint %}

With this release, you can configure OpenID authenticator on the cluster for working with Control Center. When configured, and a user logged in to Control Center via OpenID, the same Open ID Connect session will be used to authenticate user on the cluster.

The example below shows how to configure GridGain to support OpenID authentication:

{% tabs %}
{% tab title="XML" %}
```xml
<!-- Credentials for the current node. -->
<bean id="node.cred" class="org.apache.ignite.plugin.security.SecurityCredentials">
    <constructor-arg value="admin"/>
    <constructor-arg value="admin_password"/>
</bean>

<!-- Control Center user credentials. -->
<bean id="cc_login.user.cred" class="org.apache.ignite.plugin.security.SecurityCredentials">
    <constructor-arg value="cc_password"/>
    <constructor-arg value="default"/>
</bean>

<bean class="org.apache.ignite.configuration.IgniteConfiguration" >
    <property name="pluginConfigurations">
        <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
            <property name="authenticator">
                <bean class="org.gridgain.grid.security.composite.CompositeAuthenticator">
                    <property name="authenticators">
                        <list>
                            <bean class="org.gridgain.grid.security.passcode.PasscodeAuthenticator">
                                <!-- Set acl provider. -->
                                <property name="aclProvider">
                                    <bean class="org.gridgain.grid.security.passcode.AuthenticationAclBasicProvider">
                                        <constructor-arg>
                                            <map>
                                                <entry key-ref="node.cred" value="{defaultAllow:true}"/>
                                                <entry key-ref="cc_login.user.cred" value="{defaultAllow:true, {cache:'allow_cache', permissions:[CACHE_READ, CACHE_PUT, CACHE_REMOVE]},{cache:'deny_cache', permissions:[]}}"/>
                                            </map>
                                        </constructor-arg>
                                    </bean>
                                </property>
                            </bean>
                            <bean class="org.gridgain.grid.security.oidc.OpenIdAuthenticator">
                                <property name="userInfoUrl" value="https://auth.pingone.eu/f2c121ce-02a3-34ab-a164-5d96c93b1886/as/userinfo"/>
                                <property name="permissionsJson">
                                    <map>
                                        <entry key="admin" value="{defaultAllow:true}"/>
                                        <entry key="read" value="{defaultAllow:false,{cache:'*',permissions:[CACHE_READ]}}"/>
                                    </map>
                                </property>
                            </bean>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Set the passcode auth for the cluster.
GridPasscodeAuthenticator passcodeAuth = new GridPasscodeAuthenticator();
passcodeAuth.setAclProvider(new GridAuthenticationAclBasicProvider(
    F.asMap(userCred1, jsonSpec1)));

// Set up OpenID authenticator for Control Center.
OpenIdAuthenticator openIdAuth = new OpenIdAuthenticator();
openIdAuth.setUserInfoUrl("https://auth.example.com/userinfo");
openIdAuth.setPermissionsJson(F.asMap(userCred2, jsonSpec1));

// Set up composite authenticator with passcode and OpenID authenticators.
CompositeAuthenticator auth = new CompositeAuthenticator();
auth.setAuthenticators(F.asList(passcodeAuth, openIdAuth));

// Override default authentication.
IgniteConfiguration igniteCfg = new IgniteConfiguration();
GridPluginConfiguration gCfg = new GridPluginConfiguration();
gCfg.setAuthenticator(auth);
igniteCfg.setPluginConfigurations(gCfg);

// Start GridGain.
Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For more information on configuring OpenID authentication, see [Control Center OpenID Authentication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication#control-center-openid-authentication).

## Known Issues

### Snapshot Compression Requires Extra Space

Due to changes in release 8.9.18 compression is only started after the snapshot data is fully gathered. This means that to create a snapshot GridGain needs as much free space as the size of the data that will be compressed.

The extra space is only required to start the snapshot process, the snapshots will be compressed correctly if the space is available.

{% hint style="info" %}
Caches that use [Transparent Data Encryption](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/tde) are not affected.
{% endhint %}

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-42301 | Modules and Packaging | Fixed a CVE that allowed RCE on GridGain nodes under specific conditions. |
| GG-42254 | Cluster Storage Engine | Some logs that were moved to information level were moved back to debug level. |
| GG-42092 | Cluster SQL Engine | DISABLE_CREATE_LUCENE_INDEX_FOR_STRING system property is no longer supported. |
| GG-41844 | Platforms & Thin Clients | ODBC logs now include operation timeout. |
| GG-41610 | Cluster Storage Engine | Improved eviction log debug messages. |
| GG-41256 | Cluster Affinity and Baseline Topology | Changing baseline will not activate cluster that is currently in read-only mode. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-42607 | General | Updated netty-handler from version 4.1.115.Final to version to 4.1.119.Final. |
| GG-42604 | General | Updated json-smart from version 2.5.0 to version to 2.5.2. |
| GG-42316 | Cluster SQL Engine | You can now use fulltext search when running GridGain on Java 8. |
| GG-41949 | Cluster Security | Added support for composite authenticator. |
| GG-41208 | Cluster Storage Engine | Some previously suppressed messages are now logged during snapshotting process. |
| GG-41006 | Modules and Packaging | GridGain-specific errors now use GG prefix instead of IGN. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-42181 | Snapshots and Recovery | Fixed DR counters issue that could happen when restoring snapshot with empty partitions. |
| GG-39695* | Cluster Data Snapshots and Recovery | Snapshot create command now supports parallelism options. *See known issues |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-42020 | Control Center Agent | Added support for a new OpenID authenticator. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Migrating from GridGain 8.9.17 or Earlier With Java 8

Starting GridGain 8.9.18, GridGain uses Lucene 9 by default. As Lucene 9 requires Java 11, it will be impossible to run GridGain on Java 8 with default configuration.

To continue using Java 8 when migrating to GridGain 8.9.18 or later, replace the `{GRIDGAIN_HOME}/libs/ignite-lucene-9` folder with `{GRIDGAIN_HOME}/libs/optional/ignite-lucene-8`.

### Migrating From GridGain 8.9.0

GridGain 8.9.1 introduced a large number of changes in default configuration values. Your setup may be affected if you are using default configuration.

When migrating to GridGain 8.10, make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="danger" %}
Rolling upgrade is only possible if all nodes in the cluster have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. This change affects the service framework used by GridGain, and different framework versions are not compatible. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Migrating From GridGain 8.X

When migrating from GridGain 8.8 to GridGain 8.9, no special actions are required for core functionality migration. By using [rolling upgrades](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/rolling-upgrades), you can update from any GridGain version listed below. You may need to perform minor configuration changes to ensure stability post migration.

{% hint style="info" %}
While updates from GridGain 8.7.X and earlier 8.8.X versions are possible, they may require additional actions to your configuration and  depending on cumulative changes in the version.
{% endhint %}

- If you are using GridGain Enterprise or Ultimate, the `COPY` command was reworked as described in the COPY Command Changes section. The syntax for working with CSV remains the same, but the path is now calculated on the **node** and the client. This change does not affect GridGain Community edition.

  To disable this behavior and use the old copy command, pass the `disabledFeatures=SERVER_BULK_LOAD` parameter in the JDBC connection command:

  ```
  jdbc:ignite:thin://127.0.0.1/?disabledFeatures=SERVER_BULK_LOAD
  ```

- If you are using one of the optional modules listed in the Removed Modules section, they will continue to work, but compatibility and stability on GridGain 8.9 is not guaranteed. Consider using the alternatives:
  - Visor CMD and GUI can be replaced by [GridGain Control Center](https://www.gridgain.com/docs/control-center/latest/overview#system-requirements).
  - The spark module can be replaced by the Spark [Ignite Extension](https://github.com/apache/ignite-extensions).
- If you are using default values in your configuration, you may need to set them manually to keep you cluster working the same way as in previous versions. Make sure to check [Changed Default Values in GridGain 8.9.1 and Later](#changed-default-values-in-gridgain-8.9.1-and-later) section for any parameters you need to change.

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.8.4`, `8.8.13`, `8.8.18`, `8.8.22`, `8.8.24`, `8.8.27`, `8.8.37`, `8.8.39`, `8.8.43`, `8.8.44`, `8.9.0`, `8.9.1`, `8.9.5`, `8.9.9`, `8.9.12`, `8.9.13`, `8.9.14`, `8.9.15`, `8.9.16`, `8.9.16-p1`, `8.9.17`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`

### Known Limitations

#### Java 8 Support in GridGain 8.9.18 and Later

Starting GridGain 8.9.18, GridGain uses Lucene 9 by default. As Lucene 9 requires Java 11, it will be impossible to run GridGain on Java 8 with default configuration.

We recommend switching to Java 11 or later before updating to GridGain 8.9.18 or later.

To continue using Java 8, replace the `{GRIDGAIN_HOME}/libs/ignite-lucene-9` folder with `{GRIDGAIN_HOME}/libs/optional/ignite-lucene-8`.

#### Unsupported Features When Using Java 8 in GridGain 8.9.17

In GridGain 8.9.17, full text search is not supported when GridGain is running on Java 8. The new vector search feature requires using Java 11.

Additionally, GridGain 8.9.16 or earlier automatically created full text indexes for caches with string values, which may cause issues for working with the cache while using Java 8. To avoid this behavior, set the `sql.disableCreateLuceneIndexForStringValueType` property to `true`. If such index is already built for a cache with persistence, contact our support team for assistance with removing it.

We recommend switching to Java 11 or later before updating to GridGain 8.9.17 if you plan to use these features.

#### Changed Permissions for Control Center Agent in GridGain 8.9.4 and Later

GridGain 8.9.4 introduced stricter permissions checking for Control Center Agent. When running secured clusters, some actions that previously were available without permissions, will now require additional permissions.

Before updating, make sure to provide the [required permissions](https://www.gridgain.com/docs/control-center/latest/gg8/auth/authorization-permissions), otherwise some actions may become unavailable.

#### New TRACING_CONFIGURATION_UPDATE Permission in GridGain 8.9.2 and Later

GridGain 8.9.2 introduced the `TRACING_CONFIGURATION_UPDATE` [permission](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authorization-permissions). If you were using security on a cluster before updating to this version, make sure that you provide the permissions to control utilities or users who need to update cluster permissions. Otherwise, they will not be able to update

#### Changed Default Values in GridGain 8.9.1 and Later

{% hint style="danger" %}
The change to `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` prevents rolling upgrade from earlier versions to GridGain 8.9.1 unless the value is manually configured to be `false`. For more information on changing service processor implementation, see [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation.
{% endhint %}

If you are updating from GridGain 8.8.X or 8.9.0, a large number of default values have been changed.

These changes may affect the stability or performance of your cluster if you are using default values.

We recommend checking the list below to make sure the changes do not have an adverse effect, and setting the value manually if necessary.

- Service processor now use event-driven implementation by default. You can keep the old behavior by setting the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLE` property to `false`. Make sure that all nodes in the cluster are set to the same value. See [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation for more information.
- Data region metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataRegionConfiguration.metricsEnabled` value to `false`.
- Data storage metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataStorageConfiguration.metricsEnabled` value to `false`.
- `TcpCommunicationSpi` communication protocol now has a limit of 4096 messages for the outgoing messages queue by default.
- Atomic operations are now not allowed in transactions by default. You can keep the old behavior by setting the `IGNITE_ALLOW_ATOMIC_OPS_IN_TX` value to `true`.
- Logs are now in verbose mode by default. You can use the `-q` command line argument in the `ignite.sh` script to keep current log behavior.
- SQL queries are now loaded lazily by default. This reduces memory consumption on medium and large queries and potentially improves garbage collection performance. You can keep the old behavior by setting the `SqlFieldsQuery.setLazy(false)`.
- Cache entries are now read from primary partitions by default, even if an entry is available on the node in a backup partition. This may have a minor performance impact, but significantly increases cluster stability. You can keep the old behavior by setting the `readFromBackup` property to `true`.
- Partition map exchange transactions now time out after 1 minute instead of 0 (infinite) by default. You can keep the old timeout by setting the `TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE` setting to 0.
- Data streamer now overwrites entries by default. You can keep the old behavior by setting the `stmr.allowOverwrite` property to `false`.
- TCP discovery now uses static IP finder `TcpDiscoveryVmIpFinder` by default. To keep the old behavior, set the IP finder to use [multicast IP finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/tcp-ip-discovery#multicast-ip-finder).
- Checkpointing process now starts upon reaching 75% of `minWalArchiveSize` instead of 25%. You can keep the old behavior by setting the `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` system variable to `0.25`.
