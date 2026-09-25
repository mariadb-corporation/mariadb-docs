---
description: >-
  GridGain supports automatic job failover, rerouting failed jobs to available nodes according to the configured failover SPI.
---

# Fault Tolerance

GridGain supports automatic job failover. In case of a node crash, jobs are automatically transferred to other available nodes for re-execution. As long as there is at least one node standing, no job is ever lost.

The global failover strategy is controlled by the `IgniteConfiguration.failoverSpi` property.

Available implementations:

- `AlwaysFailoverSpi` — This implementation always reroutes a failed job to another node, and is used by default.

  When a job from a compute task fails, an attempt is made to reroute the failed job to a node that has not executed any other job from the same task. If no such node is available, then an attempt is made to reroute the failed job to one of the nodes that may be running other jobs from the same task. If none of the above attempts succeeds, then the job is not failed over.

  {% tabs %}
  {% tab title="XML" %}
  ```xml
  <bean class="org.apache.ignite.configuration.IgniteConfiguration">

      <property name="failoverSpi">
          <bean class="org.apache.ignite.spi.failover.always.AlwaysFailoverSpi">
              <property name="maximumFailoverAttempts" value="5"/>
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
  ```
  {% endtab %}
  {% tab title="Java" %}
  ```java
  AlwaysFailoverSpi failSpi = new AlwaysFailoverSpi();

  // Override maximum failover attempts.
  failSpi.setMaximumFailoverAttempts(5);

  // Override the default failover SPI.
  IgniteConfiguration cfg = new IgniteConfiguration().setFailoverSpi(failSpi);

  // Start a node.
  Ignite ignite = Ignition.start(cfg);
  ```
  {% endtab %}
  {% tab title="C#/.NET" %}
  unsupported
  {% endtab %}
  {% tab title="C++" %}
  unsupported
  {% endtab %}
  {% endtabs %}

- `NeverFailoverSpi` — This implementation never fails over failed jobs.

  {% tabs %}
  {% tab title="XML" %}
  ```xml
  <bean class="org.apache.ignite.configuration.IgniteConfiguration">
          
      <property name="failoverSpi">
          <bean class="org.apache.ignite.spi.failover.never.NeverFailoverSpi"/>
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
  ```
  {% endtab %}
  {% tab title="Java" %}
  ```java
  NeverFailoverSpi failSpi = new NeverFailoverSpi();

  IgniteConfiguration cfg = new IgniteConfiguration();

  // Override the default failover SPI.
  cfg.setFailoverSpi(failSpi);

  // Start a node.
  Ignite ignite = Ignition.start(cfg);
  ```
  {% endtab %}
  {% tab title="C#/.NET" %}
  unsupported
  {% endtab %}
  {% tab title="C++" %}
  unsupported
  {% endtab %}
  {% endtabs %}

- `JobStealingFailoverSpi` — This implementation must be used only if you want to enable [job stealing](load-balancing.md#job-stealing).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
