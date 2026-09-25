---
description: >-
  Configure authentication for a GridGain cluster: Ignite passcode, GridGain
  passcode, certificate, JAAS, composite, Control Center OpenID, and LDAP/AD
  authentication.
---

# Authentication

GridGain ships with a simple password-based authentication mechanism that is limited to thin client, JDBC, and ODBC connections.

GridGain Enterprise and Ultimate editions provide a more advanced Authentication and Authorization feature, which can be configured for cluster nodes as well as thin clients/JDBC/ODBC connections. For example, you can use different accounts for server nodes and client nodes and configure different sets of permissions for different clients.

{% hint style="warning" %}
Please do not use Apache Ignite authentication and GridGain authentication together as they have different subsets of users. You cannot add any permissions to the Apache Ignite user using the GridGain authentication functionality, and vice versa.
{% endhint %}

## Ignite Authentication

{% hint style="info" %}
Ignite Authentication is available in all GridGain editions.
However, if you use GridGain Enterprise or Ultimate Edition, we recommend enabling the [GridGain Authentication feature](#gridgain-authentication).
{% endhint %}

You can enable Ignite Authentication by setting the `authenticationEnabled` property to `true` in the node's configuration.
This type of authentication requires [persistent storage](../architecture/storage/native-persistence.md) be enabled for at least one data region.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="dataStorageConfiguration">
        <bean class="org.apache.ignite.configuration.DataStorageConfiguration">
            <property name="defaultDataRegionConfiguration">
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                    <property name="persistenceEnabled" value="true"/>
                </bean>
            </property>
        </bean>
    </property>

   <property name="authenticationEnabled" value="true"/> 

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

// Ignite persistence configuration.
DataStorageConfiguration storageCfg = new DataStorageConfiguration();

// Enabling the persistence.
storageCfg.getDefaultDataRegionConfiguration().setPersistenceEnabled(true);

// Applying settings.
cfg.setDataStorageConfiguration(storageCfg);

// Enable authentication
cfg.setAuthenticationEnabled(true);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
```csharp
var cfg = new IgniteConfiguration
          {
              DataStorageConfiguration = new DataStorageConfiguration
              {
                  DefaultDataRegionConfiguration = new DataRegionConfiguration
                  {
                      PersistenceEnabled = true
                  }
              },
              AuthenticationEnabled = true
          };
          Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

The first node that you start must have authentication enabled.
Upon start-up, GridGain creates a user account with the name "ignite" and password "ignite".
This account is meant to be used to create other user accounts for your needs.
Then simply delete the "ignite" account.

You can manage users using the following SQL commands:

* [CREATE USER](../reference/sql/ddl.md#create-user)
* [ALTER USER](../reference/sql/ddl.md#alter-user)
* [DROP USER](../reference/sql/ddl.md#drop-user)

## GridGain Authentication

GridGain Authentication allows you to control access to the cluster for every entity, including server and client nodes, thin clients, JDBC/ODBC and REST API clients.
The feature also enables you to manage what operations the entities are allowed to perform (authorization).

{% hint style="warning" %}
The GridGain Authentication feature is available only with GridGain Enterprise or Ultimate Edition.
{% endhint %}

How to enable authentication:

1. The first step is to configure an _authenticator_ that verifies the credentials of any entity trying to connect to the cluster (such as server or client nodes, thin clients, etc.).

   GridGain supports several ways to configure an authenticator:

   * [provide a list of users explicitly in the node configuration](#passcode-authentication).
   * Authentication through [Configure Control Center](#control-center-openid-authentication) via OpenID.
   * use a [JAASAuthenticator](#jaas-authentication) that delegates authentication to an externally configured JAAS login module.
   * implement your own `Authenticator`. Refer to the [Authenticator](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/security/Authenticator.html) javadoc.

2. Specify the username and password (of one of the existing users) in every node that connects to the cluster.
This is done by using a security credentials provider.

3. All applications that use thin clients, JDBC/ODBC, or REST API must provide user credentials as well.

Note that all server nodes must have the same authenticator configuration. GridGain verifies that all nodes use the same authenticator on the node start-up.

The following two sections explain how to configure the authenticator.

### Passcode Authentication

The simplest way to configure authentication is to define the list of users in the node configuration.
This approach consists in creating an access-control list with a set of credentials and the permissions attached to them.

In the following example, we define two users: 'server' and 'client'.
The 'server' user is allowed to execute any operation.
The 'client' user can only execute cache read operations.
All server nodes use the 'server' user credentials, and all client nodes use the credentials of the 'client' user.
Refer to the [Authorization and Permissions](authorization-permissions.md) for the full list of supported permissions.

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
<bean class="org.apache.ignite.configuration.IgniteConfiguration" >
    <property name="pluginConfigurations">
        <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
            <property name="authenticator">
                <bean class="org.gridgain.grid.security.passcode.PasscodeAuthenticator">
                    <property name="aclProvider">
                        <bean class="org.gridgain.grid.security.passcode.AuthenticationAclBasicProvider">
                            <constructor-arg>
                                <map>
                                    <!-- server.cred credentials and associated permissions (everything is allowed) -->
                                    <entry key-ref="server.cred" value="{defaultAllow:true}"/>
                                    <!-- client.cred credentials and associated permissions (only cache reads are allowed) -->
                                    <entry key-ref="client.cred" value="{defaultAllow:false, {cache:'*',permissions:['CACHE_READ']}}"/>
                                </map>
                            </constructor-arg>
                        </bean>
                    </property>
                </bean>
            </property>

            <!-- Credentials for the current node. -->
            <property name="securityCredentialsProvider">
                <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
                    <constructor-arg ref="server.cred"/>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Create security credentials objects.
SecurityCredentials serverCreds = new SecurityCredentials("server", "password");
SecurityCredentials clientCreds = new SecurityCredentials("client", "password");

// GridGain plugin configuration.
GridGainConfiguration ggCfg = new GridGainConfiguration();

// we will use simple passcode authentication
PasscodeAuthenticator authenticator = new PasscodeAuthenticator();

// Create a map for the list of credentials and permissions.
Map<SecurityCredentials, String> authMap = new HashMap<>();

// Allow all operations on server nodes.
authMap.put(serverCreds, "{defaultAllow:true}");

// Allow only cache reads on client nodes.
authMap.put(clientCreds, "{defaultAllow:false, {cache:'*', permissions:['CACHE_READ']}}");

authenticator.setAclProvider(new AuthenticationAclBasicProvider(authMap));

ggCfg.setAuthenticator(authenticator);
ggCfg.setSecurityCredentialsProvider(new SecurityCredentialsBasicProvider(serverCreds));

IgniteConfiguration igniteCfg = new IgniteConfiguration();

igniteCfg.setPluginConfigurations(ggCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
```csharp
// Provide security credentials.
SecurityCredentials serverCreds = new SecurityCredentials()
{
    Login = "server",
    Password = "password"
};

SecurityCredentials clientCreds = new SecurityCredentials()
{
    Login = "client",
    Password = "password"
};

// Create dictionary for node and client with their security credentials and permissions.
IDictionary<SecurityCredentials, ISecurityPermissionSet> authDict = new Dictionary<SecurityCredentials, ISecurityPermissionSet>();

// Allow all operations on server nodes.
authDict.Add(serverCreds, new SecurityPermissionSet()
{
    DefaultAllowAll = true
});

// Allow only cache reads on client nodes.
IDictionary<string, ICollection<SecurityPermission>> clientPermissions = new Dictionary<string, ICollection<SecurityPermission>>();
clientPermissions.Add("*", new[]
{
    SecurityPermission.CacheRead
});

authDict.Add(clientCreds, new SecurityPermissionSet()
{
    DefaultAllowAll = false,
    CachePermissions = clientPermissions
});

// GridGain plugin configuration.
var cfg = new IgniteConfiguration
{
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration()
        {
            Authenticator = new PasscodeAuthenticator()
            {
                AclProvider = new AuthenticationAclBasicProvider()
                {
                    Acl = authDict
                }
            }
        }
    }
};
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

Here is the configuration of a client node:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientMode" value="true"/>
    <property name="pluginConfigurations">
        <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
            <property name="securityCredentialsProvider">
                <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
                    <!-- Specify credentials for the current node -->
                    <constructor-arg>
                        <bean class="org.apache.ignite.plugin.security.SecurityCredentials" id="client.cred">
                            <constructor-arg value="client"/>
                            <constructor-arg value="password"/>
                        </bean>
                    </constructor-arg>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
SecurityCredentials clientCreds = new SecurityCredentials("client", "password");

GridGainConfiguration ggCfg = new GridGainConfiguration();

ggCfg.setSecurityCredentialsProvider(new SecurityCredentialsBasicProvider(clientCreds));

IgniteConfiguration igniteCfg = new IgniteConfiguration().setPluginConfigurations(ggCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

### Client Certificate Authentication

If SSL is enabled, you can grant permissions based on fields of the certificate provided by the clients.
When a client connects to the cluster, its certificate is validated against a predefined list of predicates.
Each predicate is associated with a list of permissions. If a predicate matches the client certificate, the client is granted the associated permissions.
Predicates are defined in the form of regular expressions.
If the client's certificate does not match any predicate, the client is rejected.

For example, you can define a list of permissions that are granted only if the client's certificate subject contains "O=CustomerOrganization".

Certificate-based authentication is provided by the [CertificateAuthenticator](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/security/certificate/CertificateAuthenticator.html) class.

In the following example, we configure SSL in the cluster and enable certificate-based client authentication.
Please refer to the [Authorization and Permissions](authorization-permissions.md) for the full list of supported permissions.

{% hint style="warning" %}
`CertificateAuthenticator` grants permissions to thin client subjects only.
To authenticate server and thick node joins, set `alwaysAcceptServerNodes` to `false` and combine this authenticator
with one that handles server node subjects, as shown in [Composite Authentication](#composite-authentication).
{% endhint %}

{% tabs %}
{% tab title="XML" %}
```xml
<!-- This predicate will check X.509 certificate Subject DN against regular expression: -->
<bean class="org.gridgain.grid.security.certificate.SubjectRegexPredicate" id="user.predicate">
    <constructor-arg value=".*\bCN=[a-zA-Z0-9]*\b.*"/>
</bean>

<!-- This predicate will check X.509 certificate Issuer DN against different regular expression: -->
<bean class="org.gridgain.grid.security.certificate.IssuerRegexPredicate" id="devOps.predicate">
    <constructor-arg value="^OU=devOps\b"/>
</bean>
<bean class="org.apache.ignite.configuration.IgniteConfiguration" >
    <property name="pluginConfigurations">
        <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
            <property name="authenticator">
                <bean class="org.gridgain.grid.security.certificate.CertificateAuthenticator">
                    <property name="permissionsJson">
                        <map>
                             <entry key-ref="user.predicate" value="{defaultAllow:false, {cache:'*',permissions:['CACHE_READ']}}"/>
                             <entry key-ref="devOps.predicate" value="{defaultAllow:true}"/>
                        </map>
                    </property>
                </bean>
            </property>
        </bean>
    </property>

    <!-- General SSL certificate for inter-node authentication. -->
    <property name="sslContextFactory">
        <bean class="org.apache.ignite.ssl.SslContextFactory">
            <property name="keyStoreType" value="PKCS12"/>
            <property name="keyStoreFilePath" value="keystore/node.p12"/>
            <property name="keyStorePassword" value="123456"/>
            <property name="trustStoreType" value="PKCS12"/>
            <property name="trustStoreFilePath" value="keystore/trust.p12"/>
            <property name="trustStorePassword" value="123456"/>
         </bean>
    </property>

    <!-- Secure and enable client certificate checking for JDBC/ODBC and thin clients. -->
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="sslEnabled" value="true"/>
            <property name="sslClientAuth" value="true"/>
            <property name="useIgniteSslContextFactory" value="false"/>
            <property name="sslContextFactory">
                <bean class="org.apache.ignite.ssl.SslContextFactory">
                    <property name="keyStoreType" value="PKCS12"/>
                    <property name="keyStoreFilePath" value="keystore/node.p12"/>
                    <property name="keyStorePassword" value="123456"/>
                    <property name="trustStoreType" value="PKCS12"/>
                    <property name="trustStoreFilePath" value="keystore/client-trust.p12"/>
                    <property name="trustStorePassword" value="123456"/>
                </bean>
            </property>
        </bean>
    </property>

    <!-- Secure and enable client certificate validation for control.(sh,bat). -->
    <property name="connectorConfiguration">
        <bean class="org.apache.ignite.configuration.ConnectorConfiguration">
            <property name="sslEnabled" value="true"/>
            <property name="sslClientAuth" value="true"/>

            <!-- Secure and enable client certificate validation for HTTPS REST. -->
            <property name="jettyPath" value="jetty-ssl-client-auth.xml"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// We will use certificate authentication.
CertificateAuthenticator authenticator = new CertificateAuthenticator();

// Create a map for the list of credentials and permissions.
Map<IgnitePredicate<Certificate[]>, SecurityPermissionSet> authMap = new HashMap<>();

SecurityBasicPermissionSet permissions = new SecurityBasicPermissionSet();
permissions.setDefaultAllowAll(false);
permissions.setCachePermissions(new HashMap<String, Collection<SecurityPermission>>() {
    {
        put("*", Arrays.asList(SecurityPermission.CACHE_READ));
    }
});

// This predicate will check X.509 certificate Subject DN against a regular expression:
authMap.put(new SubjectRegexPredicate(".*\\bCN=[a-zA-Z0-9]*\\b.*"), permissions);

// This predicate will check X.509 certificate Issuer DN against a different regular expression:
authMap.put(new IssuerRegexPredicate("^OU=devOps\\b"), new AllowAllPermissionSet());

authenticator.setPermissions(authMap);

// GridGain plugin configuration.
GridGainConfiguration ggCfg = new GridGainConfiguration();
ggCfg.setAuthenticator(authenticator);

IgniteConfiguration igniteCfg = new IgniteConfiguration();

igniteCfg.setPluginConfigurations(ggCfg);

// General SSL certificate for inter-node authentication.
SslContextFactory factory = new SslContextFactory();
factory.setKeyStoreType("PKCS12");
factory.setKeyStoreFilePath("keystore/node.p12");
factory.setKeyStorePassword("123456".toCharArray());
factory.setTrustStoreType("PKCS12");
factory.setTrustStoreFilePath("keystore/trust.p12");
factory.setTrustStorePassword("123456".toCharArray());
igniteCfg.setSslContextFactory(factory);

// Secure and enable client certificate validation for JDBC/ODBC and thin clients.
SslContextFactory clientFactory = new SslContextFactory();
clientFactory.setKeyStoreType("PKCS12");
clientFactory.setKeyStoreFilePath("keystore/node.p12");
clientFactory.setKeyStorePassword("123456".toCharArray());
clientFactory.setTrustStoreType("PKCS12");
clientFactory.setTrustStoreFilePath("keystore/client-trust.p12");
clientFactory.setTrustStorePassword("123456".toCharArray());

ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration();
clientConnectorCfg.setSslEnabled(true);
clientConnectorCfg.setSslClientAuth(true);
clientConnectorCfg.setUseIgniteSslContextFactory(false);
clientConnectorCfg.setSslContextFactory(clientFactory);
igniteCfg.setClientConnectorConfiguration(clientConnectorCfg);

// Secure control.(sh,bat) connection and enable client certificate validation.
ConnectorConfiguration connectorCfg = new ConnectorConfiguration();
connectorCfg.setSslEnabled(true);
connectorCfg.setSslClientAuth(true);

// Secure REST and enable client certificate validation.
//connectorCfg.setJettyPath("jetty-ssl-client-auth.xml");

igniteCfg.setConnectorConfiguration(connectorCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}

{% tab title="Jetty Configuration" %}
```xml
<!DOCTYPE Configure PUBLIC "-//Jetty//Configure//EN" "http://www.eclipse.org/jetty/configure.dtd">
<Configure id="Server" class="org.eclipse.jetty.server.Server">
    <New id="httpsCfg" class="org.eclipse.jetty.server.HttpConfiguration">
        <Set name="secureScheme">https</Set>
        <Set name="securePort"><SystemProperty name="IGNITE_JETTY_PORT" default="8443"/></Set>
        <Call name="addCustomizer">
            <Arg><New class="org.eclipse.jetty.server.SecureRequestCustomizer"/></Arg>
        </Call>
    </New>

    <New id="sslContextFactory" class="org.eclipse.jetty.util.ssl.SslContextFactory$Server">
        <Set name="keyStorePath"><SystemProperty
                name="IGNITE_HOME" default="${IGNITE_HOME}"/>keystore/node.p12</Set>
        <Set name="keyStorePassword">123456</Set>
        <Set name="keyManagerPassword">123456</Set>
        <Set name="trustStorePath"><SystemProperty
                name="IGNITE_HOME" default="${IGNITE_HOME}"/>keystore/trust-both.p12</Set>
        <Set name="trustStorePassword">123456</Set>
        <!-- This setting is necessary for client certificate authentication: -->
        <Set name="needClientAuth">true</Set>
    </New>

    <Call name="addConnector">
        <Arg>
            <New class="org.eclipse.jetty.server.ServerConnector">
                <Arg name="server">
                    <Ref refid="Server"/>
                </Arg>
                <Arg name="factories">
                    <Array type="org.eclipse.jetty.server.ConnectionFactory">
                        <Item>
                            <New class="org.eclipse.jetty.server.SslConnectionFactory">
                                <Arg><Ref refid="sslContextFactory"/></Arg>
                                <Arg>http/1.1</Arg>
                            </New>
                        </Item>
                        <!-- This section is necessary for client certificate authentication: -->
                        <Item>
                            <New class="org.eclipse.jetty.server.HttpConnectionFactory">
                                <Arg><Ref refid="httpsCfg"/></Arg>
                            </New>
                        </Item>
                    </Array>
                </Arg>
                <Set name="host"><SystemProperty name="IGNITE_JETTY_HOST" default="localhost"/></Set>
                <Set name="port"><SystemProperty name="IGNITE_JETTY_PORT" default="8443"/></Set>
            </New>
        </Arg>
    </Call>

    <Set name="handler">
        <New id="Handlers" class="org.eclipse.jetty.server.handler.HandlerCollection">
            <Set name="handlers">
                <Array type="org.eclipse.jetty.server.Handler">
                    <Item>
                        <New id="Contexts" class="org.eclipse.jetty.server.handler.ContextHandlerCollection"/>
                    </Item>
                </Array>
            </Set>
        </New>
    </Set>
</Configure>
```
{% endtab %}
{% endtabs %}

Client configuration only requires enabling SSL with an appropriate certificate:

* [control.(sh|bat)](../reference/cli-tool/README.md)
* [JDBC]({connectors}/sql/jdbc/jdbc-driver#using-ssl)
* [REST](../reference/rest-api/README.md)
* [ODBC]({connectors}/sql/odbc/connection-string-dsn)
* [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients)

### JAAS Authentication

The JAAS authenticator uses Java Authentication and Authorization Service login modules for user authentication.
The configuration of the login module is specified via the  `-Djava.security.auth.login.config=/my/path/jaas.config` system property.
GridGain reads the entry named `GridJaasLoginContext` from that file.
Set the `loginContextName` property of the authenticator to read a different entry.
Refer to the [JAAS Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASRefGuide.html) for details.

To enable JAAS authentication, use the following configuration example:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.plugin.security.SecurityCredentials" id="server.cred">
    <constructor-arg value="server"/>
    <constructor-arg value="password"/>
</bean>
<bean class="org.apache.ignite.configuration.IgniteConfiguration" >
    <property name="pluginConfigurations">
        <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
            <property name="authenticator">
                <bean class="org.gridgain.grid.security.jaas.JaasAuthenticator"/>
            </property>

            <!-- Credentials for the current node. -->
            <property name="securityCredentialsProvider">
                <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
                    <constructor-arg ref="server.cred"/>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
GridGainConfiguration ggCfg = new GridGainConfiguration();

ggCfg.setAuthenticator(new JaasAuthenticator());
        
//security credentials provider for the node.  "myUser" must be authenticated by whatever mechanism you use in the jaas configuration. Otherwise, the node will not start  
ggCfg.setSecurityCredentialsProvider(new SecurityCredentialsBasicProvider(new SecurityCredentials("myUser", "password")));

IgniteConfiguration igniteCfg = new IgniteConfiguration().setPluginConfigurations(ggCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

`securityCredentialsProvider` is a server property that enables the authentication server to provide credentials to other servers.

You can use JAAS authenticator to configure [LDAP and AD Authentication](#ldap-and-ad-authentication).

### Composite Authentication

The composite authenticator holds a list of other authenticators, including [custom authenticators](custom-authenticators.md).
Every subject is offered to each authenticator in list order.
The first authenticator that accepts the subject type and authenticates the subject decides its permissions.

The following example authenticates thin clients by certificate and server nodes join by credentials.
`alwaysAcceptServerNodes` is `false`, which makes the certificate authenticator decline node subjects and leaves them to [JAAS](#jaas-authentication).

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.plugin.security.SecurityCredentials" id="server.cred">
    <constructor-arg value="server"/>
    <constructor-arg value="password"/>
</bean>

<bean id="grid.custom.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="pluginConfigurations">
         <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
           <property name="authenticator">
             <bean class="org.gridgain.grid.security.composite.CompositeAuthenticator">
               <property name="authenticators">
                 <!-- The certificate authenticator comes first and therefore claims thin clients. -->
                 <list>

                   <!-- Thin clients are authenticated by certificate. -->
                   <bean class="org.gridgain.grid.security.certificate.CertificateAuthenticator">
                     <!-- Decline node subjects and leave them to the JAAS authenticator below. -->
                     <property name="alwaysAcceptServerNodes" value="false"/>
                     <property name="permissionsJson">
                       <map>
                         <entry>
                           <key>
                             <bean class="org.gridgain.grid.security.certificate.SubjectRegexPredicate">
                               <constructor-arg type="java.lang.String" value=".*\bCN=client\b.*"/>
                             </bean>
                           </key>
                           <value>{defaultAllow:true}</value>
                         </entry>
                       </map>
                     </property>
                   </bean>

                   <!--
                       No properties are needed here. The login modules come from the jaas.config entry
                       named GridJaasLoginContext, which is the default value of loginContextName.
                   -->
                   <bean class="org.gridgain.grid.security.jaas.JaasAuthenticator"/>

                 </list>
               </property>
             </bean>
          </property>

          <!-- Credentials that this node presents when it joins the cluster. -->
          <property name="securityCredentialsProvider">
            <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
              <constructor-arg ref="server.cred"/>
            </bean>
          </property>
         </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Thin clients are authenticated by certificate.
CertificateAuthenticator certificateAuth = new CertificateAuthenticator();
certificateAuth.setPermissionsJson(
    Collections.singletonMap(new SubjectRegexPredicate(".*\\bCN=client\\b.*"), "{defaultAllow:true}"));

// Decline node subjects and leave them to the JAAS authenticator.
certificateAuth.setAlwaysAcceptServerNodes(false);

// No properties are needed here. The login modules come from the jaas.config entry named
// GridJaasLoginContext, which is the default value of loginContextName.
JaasAuthenticator jaasAuth = new JaasAuthenticator();

// The certificate authenticator comes first and therefore claims thin clients.
CompositeAuthenticator<Authenticator> auth = new CompositeAuthenticator<>();
auth.setAuthenticators(Arrays.asList(certificateAuth, jaasAuth));

GridGainConfiguration ggCfg = new GridGainConfiguration();
ggCfg.setAuthenticator(auth);

// Credentials that this node presents when it joins the cluster.
ggCfg.setSecurityCredentialsProvider(
    new SecurityCredentialsBasicProvider(new SecurityCredentials("server", "password")));

IgniteConfiguration igniteCfg = new IgniteConfiguration().setPluginConfigurations(ggCfg);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title=".NET/C#" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

Client configuration in these scenarios should be configured for the authenticator you intend to use for the specific client.

## Control Center OpenID Authentication

{% hint style="info" %}
This authenticator is designed to work with [Control Center]({tools}/control-center) and is part of Control Center Agent [optional module](../gridgain8-usage/setup.md#enabling-modules).
{% endhint %}

The OpenID Authenticator allows users who logged in to Control Center via OpenID Connect to work with the cluster under the same user.

The specific OpenID configuration required depends on the OpenID provider.

OpenID Authentication is only used by Control Center to work with the cluster. A different authentication method must also be configured for managing authentication on the GridGain cluster.

The example below sets up the cluster for working with [PingOne](https://admin.pingone.com/) OpenID Connect provider with `gg-role` set to `claimName`:

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
                                <property name="userInfoUrl" value="[issuer.url]/userinfo"/>
                                <!-- Set claim name explicitly. If not specified, claim name is set to gg-role. -->
                                <property name="claimName" value="gg-role"/>
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

// Set claim name explicitly. If not specified, claim name is set to gg-role.
openIdAuth.setClaimName("my-role");
openIdAuth.setPermissionsJson(F.asMap(userCred2, jsonSpec2));

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
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

## LDAP and AD Authentication

Permissions can be assigned from permission strings in LDAP or AD records, or by looking up a role defined in the server configuration. JAAS uses the `authzIdentity` configuration value as a query to look up the identity to assign an authenticated user. This identity may be interpreted as a role name or as a permission string. GridGain first searches the map in the `JaasBasicPermissionsProvider` constructor arguments for a key, and then assigns the permissions associated with that map key. If the role map lookup fails, GridGain defaults to using the `authzIdentity` result as a permission string for the authenticated user.

### Permissions Granted Directly from LDAP or AD

To enable LDAP authentication, follow this procedure:

1. Configure the JAAS authenticator as explained in [JAAS Authentication](#jaas-authentication) section.
2. Create a config file for the [LdapLoginModule](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/module/LdapLoginModule.html).
   Below is an example of such a file:

   {% code title="jaas.config" %}
   ```xml
   GridJaasLoginContext {
       com.sun.security.auth.module.LdapLoginModule REQUIRED
       userProvider="ldap://serverName/ou=People,dc=nodomain"
       userFilter="uid={USERNAME}"
       authzIdentity="{<ATTR_NAME_OF_GRIDGAIN_PERMISSIONS>}"
       useSSL=false
       debug=false;
   };
   ```
   {% endcode %}

   Here `<ATTR_NAME_OF_GRIDGAIN_PERMISSIONS>` is the attribute name of the user’s LDAP entry that contains GridGain permissions in a [specific format](authorization-permissions.md).
   The following example defines a set of permissions for executing tasks and operations on caches.
   See [Authorization and Permissions](authorization-permissions.md) for the full list of available permissions.

   ```json
   {
       {
           "cache":"partitioned",
           "permissions":["CACHE_PUT", "CACHE_REMOVE", "CACHE_READ"]
       },
       {
           "cache":"*",
           "permissions":["CACHE_READ"]
       },
       {
           "task":"org.mytasks.*",
           "permissions":["TASK_EXECUTE"]
       },
       "defaultAllow":"false"
   }
   ```

3. Start all server nodes with the following system property:

   ```shell
   -Djava.security.auth.login.config=/my/path/jaas.config
   ```

When started with this configuration file, the node loads the list of users and permissions from the provided LDAP server.

### Role-based Authentication with Active Directory

It is often required to authenticate GridGain users based on their AD role (i.e., the authentication/authorization group they belong to). Typical requirements for a GridGain cluster running within an Active Directory domain would be as follows:

* Every node or client application has to authenticate itself with the domain providing correct credentials of one of the user accounts.
* Access to the cluster has to be restricted based on groups; i.e., a user can be granted a certain set of permissions if and only if that user is a member of a specific group.

#### Active Directory Settings

1. Define requirements and create Active Directory groups and users to be used for access control. For example:
   * Read-only users - can read from any cache in the cluster, but can't do updates
   * Read-write users - can both read and update data in caches
   * Superusers - have full access to all cluster functions.
2. Assign users to the groups.

On the cluster side, you need to separately configure JAAS and GridGain. The JAAS part defines how you interact with Active Directory. The GridGain part provides the actual permissions for the different groups and ties everything together.

#### Cluster Configuration - JAAS

GridGain assumes that every user has a special attribute in LDAP to store GridGain permissions as a JSON string (name of the attribute is provided to [JAAS](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASRefGuide.html) via the `authzIdentity` parameter). This does not work with the typical Active Directory structure. You want to assign permissions based on groups and roles rather than store them directly in LDAP.

Specify the `userFilter` parameter to search for the user entry that is included in a particular group. Filter conditions like `memberOf=GROUP_NAME` mimic the "contains" operation and return `true` if one of the items in the `memberOf` collection equals the provided name.

Apply the above approach to every group one-by-one. In JAAS terms, you create multiple login modules, one for each group. Here is the full configuration:

```json
GridJaasLoginContext {
    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://18.218.245.71:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_CacheReadOnlyUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_CacheReadOnlyUsers";

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://18.218.245.71:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_CacheReadWriteUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_CacheReadWriteUsers";

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://18.218.245.71:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_MonitoringUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_MonitoringUsers";

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://18.218.245.71:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_SuperUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_SuperUsers";
};
```

The above defines four LDAP login modules, each marked as `SUFFICIENT`. This means that if at least one module is successful, the user is authenticated. Two common parameters are self-explanatory — `userProvider` and `authIdentity`. The `userFilter` and `authzIdentity` parameters are unique for every module, and are used to identify which group the user is part of (if any).

For every module, JAAS will go through the following process:

1. Connect to the LDAP server and authenticate with the provided username and password.
2. Use the `userFilter` search string to look for the user entry based on the username and the group name the current module is responsible for.
3. If the above user entry exists (i.e., the user is included in the group), create a principal with the name provided in the `authzIdentity` parameter, and stop the process with success.
4. If the above user entry can't be found, move on to the next module (or fail if there are no modules left).

As a result, a successfully authenticated user is created with a principal holding the group name. This name is then passed to GridGain's permissions provider.

{% hint style="info" %}
If you want to assign a user to multiple AD groups, convert all login modules in the above configuration from `SUFFICIENT` to `OPTIONAL`. This instructs JAAS to not stop after the first successful module, but rather continue going through the list and collect all authorization identities applicable to the user. GridGain then merges all the relevant permissions together and provides the expected user access behavior. This option is available starting from GridGain 8.7.8.
{% endhint %}

#### Cluster Configuration - GridGain

In the GridGain configuration, enable `JaasAuthenticator` and use the permission provider to specify the mapping between the possible group names and the corresponding permissions. For the latter, use `JaasBasicPermissionsProvider`, which GridGain includes out-of-the-box.

For the four groups created earlier, the XML configuration looks like this:

```xml
<bean class="org.gridgain.grid.security.jaas.JaasAuthenticator">
    <property name="permissionsProvider">
        <bean class="org.gridgain.grid.security.jaas.JaasBasicPermissionsProvider">
            <constructor-arg>
                <map>
                    <entry key="GG_CacheReadOnlyUsers">
                        <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                            <property name="defaultAllowAll" value="false"/>
                            <property name="cachePermissions">
                                <map>
                                    <entry key="*">
                                        <list>
                                            <value>CACHE_READ</value>
                                        </list>
                                    </entry>
                                </map>
                            </property>
                        </bean>
                    </entry>

                    <entry key="GG_CacheReadWriteUsers">
                        <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                            <property name="defaultAllowAll" value="false"/>
                            <property name="cachePermissions">
                                <map>
                                    <entry key="*">
                                        <list>
                                            <value>CACHE_READ</value>
                                            <value>CACHE_PUT</value>
                                            <value>CACHE_REMOVE</value>
                                        </list>
                                    </entry>
                                </map>
                            </property>
                        </bean>
                    </entry>

                    <entry key="GG_MonitoringUsers">
                        <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                            <property name="defaultAllowAll" value="false"/>
                            <property name="cachePermissions">
                                <map>
                                    <entry key="*">
                                        <list>
                                            <value>ADMIN_VIEW</value>
                                            <value>ADMIN_CACHE</value>
                                            <value>ADMIN_QUERY</value>
                                            <value>ADMIN_OPS</value>
                                        </list>
                                    </entry>
                                </map>
                            </property>
                        </bean>
                    </entry>

                    <entry key="GG_SuperUsers">
                        <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                            <property name="defaultAllowAll" value="true"/>
                        </bean>
                    </entry>
                </map>
            </constructor-arg>
        </bean>
    </property>
</bean>
```

In the above configuration, you set [permissions](authorization-permissions.md#supported-permissions) for every group. For example, users included in GG_CacheReadOnlyUsers will have access to all caches, but will only be able to read the data.

#### Example

A basic example that demonstrates role/group-based authentication for AD users.

GridGain server node configuration (`server.xml`):

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="cacheConfiguration">
            <bean class="org.apache.ignite.configuration.CacheConfiguration">
                <property name="name" value="TestCache"/>
            </bean>
        </property>

        <property name="pluginConfigurations">
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <property name="authenticator">
                    <bean class="org.gridgain.grid.security.jaas.JaasAuthenticator">
                        <property name="permissionsProvider">
                            <bean class="org.gridgain.grid.security.jaas.JaasBasicPermissionsProvider">
                                <constructor-arg>
                                    <map>
                                        <entry key="GG_CacheReadOnlyUsers">
                                            <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                                                <property name="defaultAllowAll" value="false"/>
                                                <property name="cachePermissions">
                                                    <map>
                                                        <entry key="*">
                                                            <list>
                                                                <value>CACHE_READ</value>
                                                            </list>
                                                        </entry>
                                                    </map>
                                                </property>
                                            </bean>
                                        </entry>

                                        <entry key="GG_CacheReadWriteUsers">
                                            <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                                                <property name="defaultAllowAll" value="false"/>
                                                <property name="cachePermissions">
                                                    <map>
                                                        <entry key="*">
                                                            <list>
                                                                <value>CACHE_READ</value>
                                                                <value>CACHE_PUT</value>
                                                                <value>CACHE_REMOVE</value>
                                                            </list>
                                                        </entry>
                                                    </map>
                                                </property>
                                            </bean>
                                        </entry>

                                        <entry key="GG_MonitoringUsers">
                                            <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                                                <property name="defaultAllowAll" value="false"/>
                                                <property name="cachePermissions">
                                                    <map>
                                                        <entry key="*">
                                                            <list>
                                                                <value>ADMIN_VIEW</value>
                                                                <value>ADMIN_CACHE</value>
                                                                <value>ADMIN_QUERY</value>
                                                                <value>ADMIN_OPS</value>
                                                            </list>
                                                        </entry>
                                                    </map>
                                                </property>
                                            </bean>
                                        </entry>

                                        <entry key="GG_SuperUsers">
                                            <bean class="org.apache.ignite.plugin.security.SecurityBasicPermissionSet">
                                                <property name="defaultAllowAll" value="true"/>
                                            </bean>
                                        </entry>
                                    </map>
                                </constructor-arg>
                            </bean>
                        </property>
                    </bean>
                </property>

                <property name="securityCredentialsProvider">
                    <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
                        <constructor-arg>
                            <bean class="org.apache.ignite.plugin.security.SecurityCredentials">
                                <property name="login" value="GG_ServerAccount"/>
                                <property name="password" value="VeryStrongPassword123"/>
                            </bean>
                        </constructor-arg>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>127.0.0.1:47500..47509</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```

GridGain client node configuration (`client.xml`):

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="clientMode" value="true"/>

        <property name="pluginConfigurations">
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <property name="securityCredentialsProvider">
                    <bean class="org.apache.ignite.plugin.security.SecurityCredentialsBasicProvider">
                        <constructor-arg>
                            <bean class="org.apache.ignite.plugin.security.SecurityCredentials">
                                <property name="login" value="user1"/>
                                <property name="password" value="p@ssw0rd"/>
                            </bean>
                        </constructor-arg>
                    </bean>
                </property>
            </bean>
        </property>

        <property name="discoverySpi">
            <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                <property name="ipFinder">
                    <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                        <property name="addresses">
                            <list>
                                <value>127.0.0.1:47500..47509</value>
                            </list>
                        </property>
                    </bean>
                </property>
            </bean>
        </property>
    </bean>
</beans>
```

JAAS configuration (`jaas.config`):

```json
GridJaasLoginContext {
    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://3.15.156.212:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_CacheReadOnlyUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_CacheReadOnlyUsers"
    useSSL=false
    debug=false;

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://3.15.156.212:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_CacheReadWriteUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_CacheReadWriteUsers"
    useSSL=false
    debug=false;

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://3.15.156.212:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_MonitoringUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_MonitoringUsers"
    useSSL=false
    debug=false;

    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
    userProvider="ldap://3.15.156.212:389/CN=Users,DC=gridfoo,DC=com"
    authIdentity="{USERNAME}@gridfoo.com"
    userFilter="(&(sAMAccountName={USERNAME})(memberOf=CN=GG_SuperUsers,CN=Users,DC=gridfoo,DC=com))"
    authzIdentity="GG_SuperUsers"
    useSSL=false
    debug=false;
};
```

The server application (`Server.java`):

```java
import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.events.EventType;
import org.apache.ignite.plugin.security.SecuritySubject;
import org.gridgain.grid.GridGain;

public class Server {
    public static void main(String[] args) {
        Ignite ignite = Ignition.start("server.xml");

        ignite.events().localListen(event -> {
            System.out.println("Authenticated subjects:");

            GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

            for (SecuritySubject subject : gg.security().authenticatedSubjects())
                System.out.println("    " + subject.login() + ": " + subject.permissions());

            return true;
        },
        EventType.EVT_NODE_JOINED);

        IgniteCache<Integer, Integer> cache = ignite.cache("TestCache");

        for (int i = 0; i < 10; i++)
            cache.put(i, i);
    }
}
```

The above application uses a special user account called `GG_ServerAccount`, which is a member of the `GG_SuperUsers` group. This means that it has full access to all APIs and cluster functions. This is a general practice: although server nodes have to authenticate in the same way as clients, there is typically no need to put restrictions on them.

The client application (`Client.java`):

```java
import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;

public class Client {
    public static void main(String[] args) {
        try (Ignite ignite = Ignition.start("client.xml")) {
            IgniteCache<Integer, Integer> cache = ignite.cache("TestCache");

            System.out.println("Cache value for key 5: " + cache.get(5));

            cache.put(5, 100);
        }
    }
}
```

The above application authenticates with the read-only account, which is created at the very beginning. Therefore, this application is only able to read the data, but not update it. Indeed, when trying to execute a cache PUT operation, it fails with an authorization error:

```shell
org.apache.ignite.plugin.security.SecurityException: Authorization failed [perm=CACHE_PUT, name=TestCache, subject=SecuritySubjectAdapter [id=60c0c45e-69a1-498f-aa9d-5aeb1c78125d, subjType=REMOTE_NODE, addr=/0:0:0:0:0:0:0:1:0, permissions=SecurityBasicPermissionSet [cachePermissions=LinkedHashMap {*=ArrayList [CACHE_READ]}, taskPermissions=HashMap {}, servicePermissions=HashMap {}, systemPermissions=null, dfltAllowAll=false], login=user1]]
```

In addition, the server is configured to print out a list of currently authenticated users every time a new node joins the topology. This way, you can confirm that everything is configured correctly. Here is the output after both server and client nodes are up:

```shell
Authenticated subjects:
    GG_ServerAccount: SecurityBasicPermissionSet [cachePermissions=HashMap {}, taskPermissions=HashMap {}, servicePermissions=HashMap {}, systemPermissions=null, dfltAllowAll=true]
    user1: SecurityBasicPermissionSet [cachePermissions=LinkedHashMap {*=ArrayList [CACHE_READ]}, taskPermissions=HashMap {}, servicePermissions=HashMap {}, systemPermissions=null, dfltAllowAll=false]
```

The example above results in a user running under the server account with all the possible permissions — that is the server node. The second user is the client, which has the `CACHE_READ` permission only.

## Supplying Credentials in Clients

When authentication is configured in the cluster, all client applications must provide user credentials. Refer to the following pages for the information about specific clients:

* [Thin clients]({connectors}/thin-clients/getting-started-with-thin-clients#authentication)
* [JDBC driver]({connectors}/sql/jdbc/jdbc-driver#parameters)
* [ODBC driver]({connectors}/sql/odbc/connection-string-dsn#supported-arguments)
* [REST API](../reference/rest-api/README.md#security)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
