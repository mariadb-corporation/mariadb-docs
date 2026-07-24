---
description: >-
  Use Keepalived to coordinate multiple MaxScales. This guide explains how to use
  Keepalived to control which MaxScale is active and which is passive.
---

# Using Keepalived with MariaDB MaxScale

## Introduction

Using a single MaxScale in a production environment forms a single point of
failure. You can mitigate this issue by using multiple
MaxScales with similar configurations. With multiple MaxScales, one MaxScale
should control the server cluster, i.e. run cluster manipulation commands such
as [failover](../reference/maxscale-monitors/mariadb-monitor.md#auto_failover).

MariaDB recommends using
[cooperative monitoring](../reference/maxscale-monitors/mariadb-monitor.md#cooperative-monitoring)
to achieve this. Cooperative monitoring uses locks on the backend servers to
ensure that the different MaxScale instances agree on the primary MaxScale and
also on the primary server of the cluster. Only the primary MaxScale can perform
cluster manipulation operations. Cooperative monitoring only affects MaxScale
itself; it does not control which MaxScale the application talks to. Both
MaxScales process queries equally. The application can utilize multiple
MaxScales with a connector that supports connection failover, e.g.
[Connector/J](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/failover-and-high-availability-with-mariadb-connector-j-for-2x-driver)

The setup described above is not applicable to all situations:

1. Application uses a connector that does not support multiple addresses.
2. The MaxScales have a predefined hierarchy, where one is the primary and the
other is the backup. The backup should only be in control when the primary
MaxScale is down.
3. Only one MaxScale should handle client queries, and that
MaxScale should also manage the backend server cluster.

Item 1 requires that the MaxScales share a single address, and the ownership of
the address needs to be managed. Item 2 requires manual, or at least external
management of the MaxScales. Item 3 requires both.

A load balancer can achieve the single shared network address for the MaxScales,
but that would just introduce another single point of failure, which we would
prefer to avoid.

The manual management is readily available by disabling cooperative monitoring
and using the
[passive-setting](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive).

In this guide, we show how to automate the management of multiple MaxScales with
[Keepalived](https://www.keepalived.org/) when cooperative monitoring is not an
option.

## Introduction to Keepalived

[Keepalived](https://www.keepalived.org/) is a routing software for load
balancing and high-availability. It has several applications, but for this
tutorial the goal is to set up a simple IP failover between two machines running
MaxScale. If the main MaxScale fails, the backup MaxScale takes over. During the
transition, existing client connections to MaxScale break. New connections go
to the backup MaxScale. If the main MaxScale comes back online, it regains
control. The Keepalived settings used in this tutorial follow the example given
in [this blog post](https://www.redhat.com/en/blog/keepalived-basics).

In this setup, two MaxScales monitor one database cluster. Both MaxScales are in
the same LAN and share the same
[virtual IP](https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol).
Both hosts running MaxScale also run Keepalived. Clients connect to the virtual
IP (VIP), which is claimed by the current main MaxScale. The database servers
would usually be running in the same LAN, although they could be
outside as well.

Once configured and running, the different Keepalived nodes continuously
broadcast their status to the network and listen for each other. If a node does
not receive a status message from another node with a higher priority than
itself, it will transition to *master* state and claim the VIP. Conversely, if a
current master node hears from another node with a higher priority, it
relinquishes the VIP and changes to *backup* state. Any connections to the
previous master node will break when a node transition takes place.

Normally, MaxScale has no knowledge of this even happening. Both MaxScales are
running normally, monitoring the backend servers and listening for client
connections. Since clients are connecting through the VIP, only the machine
claiming the VIP will receive incoming connections. The connections between
MaxScale and the backends use real addresses and are unaffected by the VIP.

## MaxScale Configuration

MaxScale does not require any specific configuration to work with Keepalived in
this simple setup. The MaxScale configurations should be similar if not totally
identical on both hosts. Specifically, both instances should have the same
services, monitors and listeners so they appear identical to client
applications. The
[configuration synchronization](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#configuration-synchronization)
feature can help.

If you are not using configuration synchronization, you can set the
service-level setting `version_string` to different values on the MaxScale
nodes: its value is sent to any connecting clients, which helps identify the
MaxScale nodes.

```
[Read-Write Service]
type=service
router=readwritesplit
version_string=PrimaryMaxScale
...
```

## Keepalived Configuration

Keepalived requires specific setups on both machines. On the primary host, the
`/etc/keepalived/keepalived.conf`-file should be as follows.

```
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 150
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass mypass
    }
    virtual_ipaddress {
        192.168.1.123
    }
}
```

The *state* defines the initial state. It's value should be either *MASTER* or
*BACKUP*. *virtual_router_id* and *auth_pass* must be identical on all
hosts. *interface* defines the network interface used. This depends on the
system, but often the correct value is eth0, enp0s12f3 or similar. *priority*
defines the priority between different Keepalived instances. The instances
should have different values of priority. In this example, the backup host(s)
could have priority 149, 148 and so on. The instance with the highest priority
claims the VIP. *advert_int* is the interval between the advertisements a host
sends to signal its existence to other Keepalived hosts. One second is a
reasonable value.

*virtual_ipaddress* (VIP) is the IP the different Keepalived hosts try to claim
and must be identical between the hosts. The VIP must be in the local network
address space and unclaimed by any other machine in the LAN.

An example `keepalived.conf`-file for a backup host is shown below.

```
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass mypass
    }
    virtual_ipaddress {
        192.168.1.123
    }
}
```

## Run Keepalived

Start Keepalived with `sudo systemctl start keepalived`, then print its log. On
the master instance, the log should contain the following:

```
$ sudo systemctl status keepalived -n 30
● keepalived.service - LVS and VRRP High Availability Monitor
<snip>
May 06 07:24:42 maxscale Keepalived_vrrp[139892]: (VI_1) removing VIPs.
May 06 07:24:42 maxscale Keepalived_vrrp[139892]: (VI_1) Entering BACKUP STATE (init)
May 06 07:24:42 maxscale Keepalived_vrrp[139892]: VRRP sockpool: [ifindex(  2), family(IPv4), proto(112), fd(11,12)]
May 06 07:24:42 maxscale systemd[1]: Started LVS and VRRP High Availability Monitor.
May 06 07:24:45 maxscale Keepalived_vrrp[139892]: (VI_1) Receive advertisement timeout
May 06 07:24:45 maxscale Keepalived_vrrp[139892]: (VI_1) Entering MASTER STATE
May 06 07:24:45 maxscale Keepalived_vrrp[139892]: (VI_1) setting VIPs.
<snip>
```

## MaxScale health check

So far, none of this tutorial has been MaxScale-specific and the health of the
MaxScale-process has been ignored. To ensure that MaxScale is running on the
current master node, set a check script. Keepalived runs the script regularly
and if the script returns an error value, Keepalived assumes that the node has
failed, enters backup state, stops broadcasting its state and relinquishes the
VIP. Backup node then performs the opposite steps, claiming the VIP.

To define a health check script, modify the configuration as follows. The
example is for the master node. See
[this blog post](https://www.redhat.com/en/blog/advanced-keepalived) or
[Keepalived documentation](https://www.keepalived.org/manpage.html) for more
information. The config assumes the script is in file
`/etc/keepalived/is_maxscale_running`. Remember to make the script file
executable.

```
global_defs {
    script_user myuser # replace with a valid username that should run scripts
    enable_script_security
}

vrrp_script check_maxscale {
    script "/etc/keepalived/is_maxscale_running"
    interval 2 # check every 2 seconds
    timeout 3 # fails the script if it runs for too long
    fall 2 # require 2 failures for KO
    rise 2 # require 2 successes for OK
}

vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 150 # remember to alter this for the backup nodes
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass mypass
    }
    virtual_ipaddress {
        192.168.1.123
    }
    track_script {
        check_maxscale
    }
}
```

An example script is below. The script tests that the REST-API of the locally
running MaxScale responds. You can make the script as complicated as you like:
it could check the REST-API output for expected elements, check that backend
servers are in expected states, or that the local machine is responsive. If you
have the changed the REST-API default credentials, write the correct ones to the
curl-command.

```
#!/bin/bash
curl -sS http://admin:mariadb@127.0.0.1:8989/v1/maxscale/
```

An alternative script is below; it checks the `threads`-entrypoint, which
fetches statistics from every routing thread. The example only fetches the
`stats.state`-field to minimize load on the MaxScale REST-API. If any of
the routing threads are stuck, this request would time out.

```
#!/bin/bash
curl -sS "http://admin:mariadb@127.0.0.1:8989/v1/maxscale/threads?fields[threads]=stats/state"
```

When MaxScale is running, the log should show the script succeeding:

```
$sudo service keepalived status -n 30
<snip>
May 06 13:41:43 maxscale Keepalived_vrrp[151535]: Script `check_maxscale` now returning 0 May 06 13:41:45
maxscale Keepalived_vrrp[151535]: VRRP_Script(check_maxscale) succeeded
May 06 13:41:45 maxscale Keepalived_vrrp[151535]: (VI_1) Entering BACKUP STATE
May 06 13:41:49 maxscale Keepalived_vrrp[151535]: (VI_1) Receive advertisement timeout
May 06 13:41:49 maxscale Keepalived_vrrp[151535]: (VI_1) Entering MASTER STATE
May 06 13:41:49 maxscale Keepalived_vrrp[151535]: (VI_1) setting VIPs.
```

### SELinux

On systems with SELinux, the health check script may fail even when MaxScale is
running. A likely cause for this is SELinux preventing the script from making a
network connection when running under Keepalived. You can confirm this by
running the script manually in the shell. If the script returns 0, yet
Keepalived log shows the script failing, SELinux is likely the cause. Solve
this issue by giving the script file the *keepalived_unconfined_script_exec_t*
type. This also applies to the notify script explained in the next section.

```
sudo semanage fcontext -a -t keepalived_unconfined_script_exec_t "/etc/keepalived/is_maxscale_running"
sudo restorecon -v /etc/keepalived/is_maxscale_running
```

## Alter MaxScale settings depending on node status

When running a setup with multiple MaxScales, only one MaxScale (running on the
node with Keepalived master state) should be allowed to modify the cluster at
any given time. MaxScale does not know its Keepalived state, but Keepalived can
be configured to run a *notify script* whenever its state changes. Add the
following line to the Keepalived configuration file, under the
`vrrp_instance VI_1`-section:

```
notify /etc/keepalived/update_maxscale_mode
```

Keepalived calls the script with three parameters. Only the third parameter,
STATE, is relevant in our example case. Write the following script to the file
`/etc/keepalived/update_maxscale_mode` and make the file executable.

```
#!/bin/bash

TYPE=$1
NAME=$2
STATE=$3

OUTFILE=/home/myuser/status.log

case $STATE in
  "MASTER")
    echo "Setting this MaxScale node to active mode." >> $OUTFILE
    maxctrl alter maxscale passive false
    exit 0
    ;;
  "BACKUP")
    echo "Setting this MaxScale node to passive mode." >> $OUTFILE
    maxctrl alter maxscale passive true
    exit 0
    ;;
  "FAULT")
    echo "MaxScale status check failed. Setting this MaxScale node to passive mode." >> $OUTFILE
    # The following will likely fail since MaxScale is down.
    maxctrl alter maxscale passive true
    exit 0
    ;;
  "STOP")
    echo "Keepalived stopping. Setting this MaxScale node to passive mode." >> $OUTFILE
    maxctrl alter maxscale passive true
    exit 0
    ;;
  *)
    echo "Unknown state: $STATE." >> $OUTFILE
    exit 1
    ;;
esac
```

The script looks at the Keepalived state and uses MaxCtrl to set MaxScale to
passive mode whenever Keepalived is not in master state. A passive MaxScale
behaves similar to an active one with the exception that it won't perform
failover, switchover or rejoin. Even manual versions of these commands will
fail. The script also logs the current state to a text file.

If all nodes have a similar notify scripts, only one MaxScale should ever be in
active mode. Check the mode of a MaxScale instance with MaxCtrl, as shown
below. The example shows output when MaxScale is active.

```
[vagrant@maxscale ~]$ maxctrl show maxscale | grep passive
│              │     "passive": false,                                        │
```

## Cooperative monitoring and passive-mode

[MariaDB Monitor cooperative monitoring](../reference/maxscale-monitors/mariadb-monitor.md#cooperative-monitoring)
should generally not be combined with the
[passive-setting](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#passive).

The passive MaxScale will monitor and claim the MariaDB Server locks (if
possible) just like an active MaxScale would, it just won't perform failover or
other operations. This is so that in the case the active MaxScale goes down, the
passive MaxScale can still select a primary server, mark it as one and route
queries to the cluster. This works even when there is no DBA or Keepalived
to turn the MaxScale active.

The above logic does not work with Keepalived: Once the main MaxScale comes back
and regains the Keepalived master state, it can no longer claim the locks as
they are still taken by the other MaxScale. This means neither MaxScale will
perform failover, although query routing will still work. This issue can be
mitigated by calling the *release-locks*-command in the notify script when
turning a MaxScale passive:

```
  "BACKUP")
    echo "Setting this MaxScale node to passive mode." >> $OUTFILE
    maxctrl alter maxscale passive true
    maxctrl call command mariadbmon release-locks MyMonitor
    exit 0
    ;;
```

This solution has its issues: Keepalived usually starts in the backup state,
then transitions quickly to master state if possible. Calling *release-locks*
prevents the monitor from acquiring locks for one minute, meaning that for some
time, the active MaxScale node will not hold the locks even if they are
unclaimed. The cluster will remain unusable until one MaxScale claims the locks.
