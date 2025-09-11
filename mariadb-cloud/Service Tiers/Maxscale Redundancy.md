# MaxScale Redundancy

MariaDB MaxScale serves as the load balancer in certain SkySQL topologies.

SkySQL supports MaxScale Redundancy as an option at time of launch:

- This feature is not enabled by default. By default, topologies that use MaxScale contain only one MaxScale node.

- When MaxScale Redundancy is selected, MaxScale nodes are deployed in a highly available (HA) active-active configuration behind round robin load balancing.

- When MaxScale Redundancy is enabled, MaxScale instance size can be selected.

- MaxScale Redundancy is available to Power Tier customers.

## Compatibility

- Replicated Transactions

## Enable MaxScale Redundancy

1. Launch a SkySQL service:

- Check the "Enable MaxScale Redundancy" checkbox.

- Choose the [MaxScale instance size](<../Reference Guide/Instance Size Choices.md>)
