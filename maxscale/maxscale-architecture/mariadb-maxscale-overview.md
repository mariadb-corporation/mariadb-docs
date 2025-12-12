---
description: >-
  Get a high-level view of MariaDB MaxScale features. Explore how it handles
  load balancing, high availability, and security to optimize your database
  infrastructure.
---

# MariaDB MaxScale Overview

## Overview

MariaDB MaxScale is an advanced proxy, router, and load balancer:

* MaxScale performs automated failover for MariaDB replication. When the primary server fails, MaxScale promotes a replica to be the new primary and redirects the remaining replicas to it.
* MaxScale's ReadWriteSplit router performs query-based load balancing. ReadWriteSplit routes each write statement to the current primary server and load balances read statements by routing them to the replica servers.
* MaxScale's ReadConnRoute router performs connection-based load balancing. ReadConnRoute routes each connection to a single primary or replica node, depending on configuration.
* MaxScale can import data from Kafka and export data into Kafka. MaxScale's KafkaCDC router streams data from MariaDB database products to a Kafka broker. MaxScale's KafkaImporter router streams data from Kafka to MariaDB database products.
* MaxScale provides built-in mechanisms to perform server maintenance without disrupting applications or clients. Servers can be set to maintenance mode using the command-line interface with MaxCtrl, a web browser with MaxGUI, or REST API.
* MaxScale's Cache filter can improve SELECT performance by caching and reusing results.
* Security and traffic controls for database connections and queries can be implemented with MaxScale. MaxScale's QLAfilter can be used to create an audit trail by logging all queries. MaxScale's RegexFilter can also perform audit logging or protect against SQL injection by matching queries against a regular expression and performing various actions on the query, such as logging it, modifying it, or routing it to a specific server.

MariaDB MaxScale can be deployed in the cloud or on-premises.

## Scheduled Releases

MariaDB MaxScale follows the MariaDB Enterprise release schedule, which can be found [here](../../release-notes/enterprise-server/enterprise-server-release-schedule.md).

## Software Releases

The supported MaxScale versions can be found in the latest [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
