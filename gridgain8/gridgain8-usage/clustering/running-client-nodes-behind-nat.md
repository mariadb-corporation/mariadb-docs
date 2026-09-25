---
description: >-
  Enabling forced client-to-server connections so GridGain server nodes can work
  with client nodes deployed behind a NAT, and the limitations of this mode.
---

# Running Client Nodes Behind NAT

If your client nodes are deployed behind a NAT, the server nodes won't be able to establish connection with the clients because of the limitations of the communication protocol.
This includes deployment cases when client nodes are running in virtual environments (like Kubernetes) and the server nodes are deployed elsewhere.

For cases like this, you need to enable a special mode of communication:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientMode" value="true"/>
    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="forceClientToServerConnections" value="true"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setClientMode(true);
cfg.setCommunicationSpi(new TcpCommunicationSpi().setForceClientToServerConnections(true));
```
{% endtab %}

{% tab title="C#/.NET" %}
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Limitations

* This mode cannot be used when `TcpCommunicationSpi.usePairedConnections = true` is set on either server or client nodes.

* Peer class loading for [continuous queries (transformers and filters)](../continuous-queries.md) does not work when a continuous query is started from a client node `forceClientToServerConnections = true`.
You will need to add the corresponding classes to the classpath of every server node.

* This property can only be used on client nodes. This limitation will be addressed in the future releases.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
