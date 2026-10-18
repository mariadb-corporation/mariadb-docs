---
description: >-
  Set up SSL/TLS to secure GridGain node-to-node, thin-client (ODBC/JDBC), and HTTPS REST traffic with a self-signed certificate authority.
---

# How to Configure SSL/TLS/HTTPS Security

## Prerequisites

- A **GridGain 8** cluster
- **OpenSSL** 1.1.1
- **JDK 11** (OpenJDK)
- The Java **keytool** utility

## Overview

GridGain's distributed processing allows fast calculations and data queries by sending data between nodes, thin clients, and other applications connected to the system. However, transmitting data is done in plain text and may not be safe for your organization's most sensitive data. Hence, it is essential to have a data security strategy in place.

This guide explains how to use SSL/TLS protocols to provide a secure connection among all nodes, thin clients, and HTTPs clients.

## Configuration and Preparation

This example uses the following applications:

| Item | Version |
| --- | --- |
| GridGain | 8.7.X |
| Security Protocol Version | TLSv1.2 |
| OpenSSL | 1.1.1 |
| JDK | openjdk version 11 |

The following algorithms may be supported https://docs.oracle.com/en/java/javase/11/docs/specs/security/standard-names.html#sslcontext-algorithms. However, you should check the JAVA release documentation for your implementation to see if these algorithms are supported. By default, JAVA 11 supports the following protocols:

- TLSv1
- TLSv1.1
- TLSv1.2

For this example, assume that by default GridGain supports only these three protocols when started with JAVA 11.

To obtain an SSL certificate from a certificate authority (CA), you need to generate a certificate signing request (CSR). A CSR consists mainly of the public key of a key pair and some additional information. Both of these components are inserted into the certificate when it is signed.

Create a certificate authority to sign certificates for GridGain nodes keys by using the following steps:

1. Generate a CSR and a private key:

   ```bash
   openssl req -new -newkey rsa:2048 -nodes -config ca_key.conf -out ca.csr -keyout ca.key
   ```

   The following options are used here:

   - `-newkey rsa:2048` -  key should be 2048-bit, used algorithm is RSA
   - `-nodes` - private key should *not* be encrypted with a passphrase
   - `-new` - CSR is being generated

   The command will prompt the following questions:

   | Question | Response |
   | --- | --- |
   | Country Name (2 letter code) | The two-letter country code where your company is legally located. |
   | State or Province Name (full name) | The state/province where your company is legally located. |
   | Locality Name (e.g., city) | The city where your company is legally located. |
   | Organization Name (e.g., company) | Your company's legally registered name (e.g., YourCompany, Inc.). |
   | Organizational Unit Name (e.g., section) | The name of your department within the organization. (You can leave this option blank; simply press Enter.) |
   | Common Name (e.g., server FQDN) | The fully-qualified domain name (FQDN) (e.g., www.example.com). |
   | Email Address | Your email address. (You can leave this option blank; simply press Enter.) |
   | A challenge password | Leave this option blank (simply press Enter). |
   | An optional company name | Leave this option blank (simply press Enter). |

   After this command the `ca.csr` and `ca.key` files will be generated.

2. Generate the SSL certificate:

   ```bash
   openssl x509 -trustout -signkey ca.key -req -in ca.csr -out ca.pem
   ```

   The following options are used here:

   - `-x509` - `-req` will create self-signed certificate
   - `-days 365` - certificate will be valid for 365 days
   - `-signkey` - shows which key will be used
   - `-in` - which CSR will be used
   - `-out` - path to the generated certificate

   After this command the `ca.pem` file will be generated. This is the self-sign certificate of the new CA. You can now use it to sign certificates. Note that other applications will not accept such certificates on HTTPS since anybody could have signed it; but it's secure for nodes if you don't lose `ca.key`.

3. Put the generated certificate into a Java key store:

   ```bash
   keytool -deststorepass ${PASS} -noprompt  -import -file ca.pem -alias CertificateAuthority -keystore trust.jks
   ```

   The following options are used here:

   - `-import` - new certificate should be added to keystore
   - `-file` - which certificate should be added to keystore
   - `-keystore` - which keystore will be used
   - `-alias` - some unique name which will be associated with current certificate

   After setting the password, the `trust.jks` file will be generated. Note that every node may have their own primary key, which should be also signed by our CA.

4. Prepare the configuration file (`ca.cnf`):

   ```
   cat << EOF > ca.cnf
   [ ca ]
   default_ca = CertificateAuthority

   [ CertificateAuthority ]
   certificate = ./ca.pem
   database = ./index.txt
   private_key = ./ca.key
   new_certs_dir = ./
   default_md = sha256
   policy = policy_match
   serial = ./serial
   default_days = 365

   [policy_match]
   commonName = supplied
   EOF
   ```

   Here `index.txt`  and `serial` files should be generated:

   ```
   touch index.txt
   echo 01 > serial
   ```

   Now you are ready to configure SSL in the GridGain cluster. Make sure that you have all the following files:

   ```
   ca.conf  ca.csr  ca.key  ca.pem  index.txt  serial  trust.jks
   ```

5. Use the following script to generate the certificates for your GridGain cluster:

   ```bash
   #!/usr/bin/env bash

   set -x

   # Certificates password.
   PASS=qwerty

   # Server.
   SERVER_DN="CN=localhost,OU=ID,O=GG,L=Hursley,S=Hants,C=GB"

   # Client.
   CLIENT_DN="CN=client.com,OU=Qs,O=GG,L=WEWe,S=Asda,C=GB"

   # Cleanup.
   rm -vf node.*
   rm -vf client.*
   rm -vf rest.*
   rm -vf ca.*
   rm -vf in*
   rm -vf seri*
   rm -vf trust*
   rm -vf *pem
   rm -vf *cnf
   rm -vf *conf

   # ca key config.
   cat << EOF > ca_key.conf
   [req]
   prompt                 = no
   distinguished_name     = dn
   req_extensions         = req_ext
   [ dn ]
   countryName            = US
   stateOrProvinceName    = New York
   localityName           = New York
   organizationName       = GridGain
   commonName             = localhost
   organizationalUnitName = IT
   emailAddress           = node@test.local
   [ req_ext ]
   subjectAltName         = @alt_names
   [ alt_names ]
   DNS.1                  = localhost
   EOF

   # ca configuration file
   cat << EOF > ca.cnf
   [ ca ]
   default_ca = CertificateAuthority

   [ CertificateAuthority ]
   certificate = ./ca.pem
   database = ./index.txt
   private_key = ./ca.key
   new_certs_dir = ./
   default_md = sha256
   policy = policy_match
   serial = ./serial
   default_days = 365

   [policy_match]
   commonName = supplied
   EOF

   touch index.txt
   echo 01 > serial

   # Generate CA
   openssl req -new -newkey rsa:2048 -nodes -config ca_key.conf -out ca.csr -keyout ca.key
   openssl x509 -trustout -signkey ca.key -req -in ca.csr -out ca.pem
   keytool -deststorepass ${PASS} -noprompt  -import -file ca.pem -alias CertificateAuthority -keystore trust.jks

   # Generate node certificates
   keytool -genkey -keyalg RSA -keysize 2048 -alias node -deststorepass ${PASS} -keystore node.jks -noprompt \
    -dname ${SERVER_DN} \
    -storepass ${PASS} \
    -keypass ${PASS}
   keytool -deststorepass ${PASS} -certreq -alias node -file node.csr -keystore node.jks
   openssl ca -batch -config ca.cnf -out node.pem -infiles node.csr
   keytool -deststorepass ${PASS} -import -alias ca -keystore node.jks -file ca.pem -noprompt
   keytool -deststorepass ${PASS} -import -alias node -keystore node.jks -file node.pem -noprompt
   keytool -importkeystore -srcstoretype JKS -deststoretype PKCS12 -srckeystore node.jks -destkeystore node.p12 -srcstorepass ${PASS} -deststorepass ${PASS} -srcalias node -destalias node -noprompt
   openssl pkcs12 -in node.p12 -out ca_odbc.pem -passin pass:${PASS} -nodes

   # Generate Client certificates
   keytool -genkey -keyalg RSA -keysize 2048 -alias client -deststorepass ${PASS} -keystore client.jks -noprompt \
    -dname ${CLIENT_DN} \
    -storepass ${PASS} \
    -keypass ${PASS}
   keytool -deststorepass ${PASS} -certreq -alias client -file client.csr -keystore client.jks
   openssl ca -batch -config ca.cnf -out client.pem -infiles client.csr
   keytool -deststorepass ${PASS} -import -alias ca -keystore client.jks -file ca.pem -noprompt
   keytool -deststorepass ${PASS} -import -alias client -keystore client.jks -file client.pem -noprompt
   keytool -importkeystore -srcstoretype JKS -deststoretype PKCS12 -srckeystore client.jks -destkeystore client.p12 -srcstorepass ${PASS} -deststorepass ${PASS} -srcalias client -destalias client -noprompt
   openssl pkcs12 -in client.p12 -out client.pem -passin pass:${PASS} -nodes
   ```

   The script generates the following certificates:

   - `node.jks` - can be used by any cluster node
   - `client.jks` - can also be used by any cluster node, but you will use it for thin connections
   - `client.pem` and `ca_odbc.pem` - can be used for ODBC connection

## SSL/TLS for Thick Nodes

Before configuring GridGain nodes, you must generate the private key for every node. Here is an example of how this can be done for one node:

1. Generate the primary key for a node:

   ```bash
   keytool -genkey -keyalg RSA -keysize 2048 -alias node -deststorepass ${PASS} -keystore node.jks -noprompt \
    -dname ${SERVER_DN} \
    -storepass ${PASS} \
    -keypass ${PASS}
   ```

   This will create the `node.jks` file.

2. Generate the CSR for node:

   ```bash
   keytool -deststorepass ${PASS} -certreq -alias node -file node.csr -keystore node.jks
   ```

   This will create the `node.csr` file.

3. Using the previously created `ca.cnf`, create a signed certificate for the node:

   ```bash
   openssl ca -batch -config ca.cnf -out node.pem -infiles node.csr
   ```

   This will create the `node.pem` certificate.

4. Add both `node.pem` and `ca.pem` certificates to the Java key store:

   ```bash
   keytool -deststorepass ${PASS} -import -alias ca -keystore node.jks -file ca.pem -noprompt
   keytool -deststorepass ${PASS} -import -alias node -keystore node.jks -file node.pem -noprompt
   ```

   After these commands `node.jks` file should be created. Both `node.jks` and `trust.jks` files can now be used to configure the SSL/TLS for GridGain node. Here is the XML configuration file:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="
          http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans.xsd">

       <bean id="grid.cfg"
             class="org.apache.ignite.configuration.IgniteConfiguration">
           <property name="sslContextFactory">
               <bean class="org.apache.ignite.ssl.SslContextFactory">
                   <property name="keyStoreFilePath" value="node.jks"/>
                   <property name="keyStorePassword" value="qwerty"/>
                   <property name="trustStoreFilePath" value="trust.jks"/>
                   <property name="trustStorePassword" value="qwerty"/>
               </bean>
           </property>
           <property name="connectorConfiguration">
               <bean class="org.apache.ignite.configuration.ConnectorConfiguration">
                   <property name="sslEnabled" value="true"/>
                   <property name="sslClientAuth" value="true"/>
                   <property name="jettyPath" value="jetty.xml" />
               </bean>
           </property>
           <property name="clientConnectorConfiguration">
               <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
                   <property name="host" value="127.0.0.1"/>
                   <property name="port" value="11110"/>
                   <property name="portRange" value="10"/>
                   <property name="sslEnabled" value="true"/>
                   <property name="useIgniteSslContextFactory" value="false"/>
                   <property name="sslClientAuth" value="true"/>
                   <property name="sslContextFactory">
                       <bean class="org.apache.ignite.ssl.SslContextFactory">
                           <property name="keyStoreFilePath" value="node.jks"/>
                           <property name="keyStorePassword" value="qwerty"/>
                           <property name="trustStoreFilePath" value="trust.jks"/>
                           <property name="trustStorePassword" value="qwerty"/>
                       </bean>
                   </property>
               </bean>
           </property>
           <property name="discoverySpi">
               <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                   <property name="ipFinder">
                       <bean
                           class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                           <property name="addresses">
                               <list>
                                   <value>127.0.0.1:47500..47510</value>
                               </list>
                           </property>
                       </bean>
                   </property>
               </bean>
           </property>
           <property name="communicationSpi">
               <bean
                   class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
                   <property name="localPort" value="48100"/>
                   <property name="localPortRange" value="10"/>
                   <property name="socketWriteTimeout" value="300000"/>
               </bean>
           </property>
           <property name="pluginConfigurations">
               <bean class="org.gridgain.grid.configuration.GridGainConfiguration"/>
           </property>
       </bean>
   </beans>
   ```

5. Now start the nodes and make sure to add `-Djdk.tls.client.protocols=TLSv1.2` JVM option to tell JVM that you are going to use TLS > 1.2.

Now you can take a look at the logs:

```
[19:02:58] Security status [authentication=off, tls/ssl=on]
```

You can see now that TLS/SSL is working. Note that TLS/SSL does not provide any authorization; it only provides secure messaging between nodes (authentication).

Check what happens if you add a client without correct certificates:

- Client node without SslContextFactory

  ```
  Caused by: class org.apache.ignite.spi.IgniteSpiException: Unable to establish secure connection. Was remote cluster configured with SSL? [rmtAddr=/127.0.0.1:47500, errMsg="Failed to deserialize object with given class loader: sun.misc.Launcher$AppClassLoader@18b4aac2"]
  ```

- Client node with incorrect certificate

  ```
  Server:

  [19:11:19] Failed to initialize connection (missing SSL configuration on remote node?) [rmtAddr=/127.0.0.1]
  [19:16:45] Failed to initialize connection (missing SSL configuration on remote node?) [rmtAddr=/127.0.0.1]

  Client:

  [19:16:59] Failed to connect to any address from IP finder (will retry to join topology every 2000 ms; change 'reconnectDelay' to configure the frequency of retries): [/127.0.0.1:47500, /127.0.0.1:47501, /127.0.0.1:47502, /127.0.0.1:47503, /127.0.0.1:47504, /127.0.0.1:47505, /127.0.0.1:47506, /127.0.0.1:47507, /127.0.0.1:47508, /127.0.0.1:47509]
  ```

When everything is configured correctly, you will see that both nodes have discovered each other:

```
[19:23:32] Ignite node started OK (id=f0969bc7, instance name=client)
[19:23:32] Topology snapshot [ver=2, locNode=f0969bc7, servers=1, clients=1, state=ACTIVE, CPUs=4, offheap=6.4GB, heap=15.0GB]
```

This method can be used by cluster thick nodes and clients (that can use IgniteConfiguration):

- GridGain servers (Java, .Net, C++)
- GridGain clients  (Java, .Net, C++)
- Visor GUI in external mode
- GridGain Jdbc Driver

Following sections describe how to configure SSL/TLS for thin clients (ODBC/JDBC) and HTTP connections (REST).

## SSL/TLS for Thin Clients (ODBC/JDBC)

To use SSL/TLS for communication between your GridGain cluster and thin clients, you will need to configure the `ClientConnectorConfiguration` bean in your nodes' XML configuration, like so:

```xml
<property name="clientConnectorConfiguration">
    <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
        <property name="host" value="127.0.0.1"/>
        <property name="port" value="11110"/>
        <property name="portRange" value="10"/>
        <property name="sslEnabled" value="true"/>
        <property name="useIgniteSslContextFactory" value="false"/>
        <property name="sslClientAuth" value="true"/>
        <property name="sslContextFactory">
            <bean class="org.apache.ignite.ssl.SslContextFactory">
                <property name="keyStoreFilePath" value="node.jks"/>
                <property name="keyStorePassword" value="qwerty"/>
                <property name="trustStoreFilePath" value="trust.jks"/>
                <property name="trustStorePassword" value="qwerty"/>
            </bean>
        </property>
    </bean>
</property>
```

### Thin JDBC Client

GridGain thin JDBC driver allows you to use secure socket communication to provide a secure connection between JDBC driver and GridGain node (includes the initial handshake).

Here is an example of how to create a secure thin JDBC connection:

```java
Ignite ignite = Ignition.start("server.xml");

ignite.cluster().active(true);

// Register JDBC driver.
Class.forName("org.apache.ignite.IgniteJdbcThinDriver");

// Open the JDBC connection.
try (Connection conn = DriverManager.getConnection("jdbc:ignite:thin://127.0.0.1:11110?" +
    "sslMode=require&" +
    "sslClientCertificateKeyStoreUrl=" + pathToClientJks + "&" +
    "sslClientCertificateKeyStorePassword=" + clientPassword + "&" +
    "sslTrustCertificateKeyStoreUrl=" + pathToTrustStoreJks + "&" +
    "sslTrustCertificateKeyStorePassword=" + trustorePassword)) {
    conn.createStatement().executeQuery("select 1");

    System.out.println("Done");
}
catch (SQLException e) {
    e.printStackTrace();
}
```

The following properties are used here:

- `sslMode` - enables SSL connection

  Available modes - `require`: SSL protocol is enabled on the client. Only SSL connection is available. `disable`: SSL protocol is disabled on the client. Only plain connection is supported.
- `sslClientCertificateKeyStoreUrl` - URL of the client key store file
- `sslClientCertificateKeyStorePassword` - client key store password
- `sslTrustCertificateKeyStoreUrl` - URL of the trust store file
- `sslTrustCertificateKeyStorePassword` - trust store password

You can find other JDBC parameters in the documentation here: https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/JDBC/jdbc-driver

### Thin ODBC Client

Since an ODBC connection can't be started with Java, JKS can't be used. In case if you have generated two JKS for server node and client node, then you can prepare the required keys and certificates using the following OpenSSL commands from created files:

- `node.jks` will be used by server node that will be used for ODBC connection
- `client.jks` will be used by ODBC clients..

```bash
# Extracting server certificate into PEM file. This is going to be our CA file for the ODBC client.
keytool -importkeystore -srcstoretype JKS -deststoretype PKCS12 -srckeystore node.jks -destkeystore node.p12 -srcstorepass ${PASS} -deststorepass ${PASS} -srcalias node -destalias node -noprompt
openssl pkcs12 -in node.p12 -out ca_odbc.pem -passin pass:${PASS} -nodes

# Extracting client certificate and key into PEM file. This is going to be our private credentials file for the ODBC client.
keytool -importkeystore -srcstoretype JKS -deststoretype PKCS12 -srckeystore client.jks -destkeystore client.p12 -srcstorepass ${PASS} -deststorepass ${PASS} -srcalias client -destalias client -noprompt
openssl pkcs12 -in client.p12 -out client.pem -passin pass:${PASS} -nodes
```

Now you are ready to make the ODBC connection using following connection string:

```
DRIVER={Apache Ignite};ADDRESS=127.0.0.1:11110;SCHEMA=PUBLIC;SSL_MODE=require;SSL_KEY_FILE=client.pem;SSL_CERT_FILE=client.pem;SSL_CA_FILE=ca_odbc.pem;
```

You can read more about the ODBC connection string and its parameters here: https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/ODBC/connection-string-dsn

## HTTPS for REST

REST can also use a secured connection to cluster. In this case, you will need to set up `-Dhttps.protocols=TLSv1.2` and configure the Jetty https server, as well as perform following additional steps:

1. Prepare the configuration file for generating of the certificates:

   ```
   cat << EOF > rest.conf
   [req]
   prompt                 = no
   distinguished_name     = dn
   req_extensions         = req_ext
   [ dn ]
   countryName            = US
   stateOrProvinceName    = New York
   localityName           = New York
   organizationName       = GridGain
   commonName             = localhost
   organizationalUnitName = IT
   emailAddress           = rest@test.local
   [ req_ext ]
   subjectAltName         = @alt_names
   [ alt_names ]
   DNS.1                  = localhost
   IP.1                   = 127.0.0.1
   EOF
   ```

   It's important to have the same CN (or alt_names) as used in the server. Otherwise, the SSL handshake can fail.

2. Generate the private key and certificate for REST:

   ```
   openssl genrsa -des3 -passout pass:${PASS} -out rest.key 1024
   openssl req -new -passin pass:${PASS} -key rest.key -config rest.conf -out rest.csr
   openssl x509 -req -days 365 -in rest.csr -CA ca.pem -CAkey ca.key -set_serial 01 -extensions req_ext -extfile rest.conf -out rest.crt
   openssl pkcs12 -export -in rest.crt -inkey rest.key -passin pass:${PASS} -certfile rest.crt -out rest.p12 -passout pass:${PASS}
   keytool -importkeystore -srckeystore rest.p12 -srcstoretype PKCS12 -destkeystore rest.jks -deststoretype JKS -noprompt -srcstorepass ${PASS} -deststorepass ${PASS}
   ```

3. Prepare the Jetty configuration file for HTTPS support:

   ```xml
   openssl genrsa -des3 -passout pass:${PASS} -out rest.key 1024
   openssl req -new -passin pass:${PASS} -key rest.key -config rest.conf -out rest.csr
   openssl x509 -req -days 365 -in rest.csr -CA ca.pem -CAkey ca.key -set_serial 01 -extensions req_ext -extfile rest.conf -out rest.crt
   openssl pkcs12 -export -in rest.crt -inkey rest.key -passin pass:${PASS} -certfile rest.crt -out rest.p12 -passout pass:${PASS}
   keytool -importkeystore -srckeystore rest.p12 -srcstoretype PKCS12 -destkeystore rest.jks -deststoretype JKS -noprompt -srcstorepass ${PASS} -deststorepass ${PASS}

   <?xml version="1.0" encoding="UTF-8"?>
   <!--
   Copyright (C) GridGain Systems. All Rights Reserved.
   _________        _____ __________________        _____
   __  ____/___________(_)______  /__  ____/______ ____(_)_______
   _  / __  __  ___/__  / _  __  / _  / __  _  __ `/__  / __  __ \
   /  /_/ /  _  /    _  /  / /_/ /  / /_/ /  / /_/ / _  /  _  / / /
   \____/   /_/     /_/   \_,__/   \____/   \__,_/  /_/   /_/ /_/
   -->
   <!DOCTYPE Configure PUBLIC "-//Jetty//Configure//EN" "http://www.eclipse.org/jetty/configure.dtd">
   <Configure id="Server" class="org.eclipse.jetty.server.Server">
       <Arg name="threadPool">
           <!-- Default queued blocking thread pool -->
           <New class="org.eclipse.jetty.util.thread.QueuedThreadPool">
               <Set name="minThreads">10</Set>
               <Set name="maxThreads">200</Set>
           </New>
       </Arg>
       <New id="httpsCfg" class="org.eclipse.jetty.server.HttpConfiguration">
           <Set name="secureScheme">https</Set>
           <Set name="securePort">
               <SystemProperty name="IGNITE_JETTY_PORT" default="8443" />
           </Set>
           <Set name="sendServerVersion">true</Set>
           <Set name="sendDateHeader">true</Set>
           <Call name="addCustomizer">
               <Arg>
                   <New class="org.eclipse.jetty.server.SecureRequestCustomizer" />
               </Arg>
           </Call>
       </New>
       <New id="sslContextFactory" class="org.eclipse.jetty.util.ssl.SslContextFactory$Server">
           <Set name="keyStorePath">rest.jks</Set>
           <Set name="keyStorePassword">qwerty</Set>
           <Set name="keyManagerPassword">qwerty</Set>
           <Set name="trustStorePath">trust.jks</Set>
           <Set name="trustStorePassword">qwerty</Set>
       </New>
       <Call name="addConnector">
           <Arg>
               <New class="org.eclipse.jetty.server.ServerConnector">
                   <Arg>
                       <Ref refid="Server" />
                   </Arg>
                   <Arg>
                       <Array type="org.eclipse.jetty.server.ConnectionFactory">
                           <Item>
                               <New class="org.eclipse.jetty.server.SslConnectionFactory">
                                   <Arg>
                                       <Ref refid="sslContextFactory" />
                                   </Arg>
                                   <Arg>http/1.1</Arg>
                               </New>
                           </Item>
                           <Item>
                               <New class="org.eclipse.jetty.server.HttpConnectionFactory">
                                   <Arg>
                                       <Ref refid="httpsCfg" />
                                   </Arg>
                               </New>
                           </Item>
                       </Array>
                   </Arg>
                   <!--
                       Note that in order to override local host and port values,
                       system properties must have names IGNITE_JETTY_HOST and
                       IGNITE_JETTY_PORT accordingly.
                   -->
                   <Set name="host">
                       <SystemProperty name="IGNITE_JETTY_HOST" default="0.0.0.0" />
                   </Set>
                   <Set name="port">
                       <SystemProperty name="IGNITE_JETTY_PORT" default="8443" />
                   </Set>
                   <Set name="idleTimeout">30000</Set>
                   <Set name="reuseAddress">true</Set>
               </New>
           </Arg>
       </Call>
       <Set name="handler">
           <New id="Handlers" class="org.eclipse.jetty.server.handler.HandlerCollection">
               <Set name="handlers">
                   <Array type="org.eclipse.jetty.server.Handler">
                       <Item>
                           <New id="Contexts" class="org.eclipse.jetty.server.handler.ContextHandlerCollection" />
                       </Item>
                   </Array>
               </Set>
           </New>
       </Set>
       <Set name="stopAtShutdown">false</Set>
   </Configure>
   ```

4. Add the following dependency to your pom.xml file:

   ```
   <dependency>
       <groupId>org.gridgain</groupId>
       <artifactId>ignite-rest-http</artifactId>
       <version>${ignite.version}</version>
   </dependency>
   ```

5. Add the path for Jetty configuration into `connectorConfiguration`:

   ```xml
   <property name="connectorConfiguration">
       <bean class="org.apache.ignite.configuration.ConnectorConfiguration">
           <property name="sslEnabled" value="true"/>
           <property name="sslClientAuth" value="true"/>
           <property name="jettyPath" value="jetty.xml" />
       </bean>
   </property>
   ```

6. After configuring the HTTPS Jetty web server, you can run the following REST command in your browser:

   ```
   https://localhost:8443/ignite?cmd=version
   ```

   If you see an output similar to the one below, then HTTPS was configured correctly.

   ```
   {"successStatus":0,"error":null,"sessionToken":null,"response":"8.7.X"}
   ```

## Related

- [JDBC driver](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/JDBC/jdbc-driver) - Additional thin JDBC driver parameters.
- [ODBC connection string and DSN](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/SQL/ODBC/connection-string-dsn) - Full ODBC connection string reference.
