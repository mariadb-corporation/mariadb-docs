# Removing a Server using MaxCtrl

When operating MariaDB MaxScale in dynamic environments—such as Kubernetes, where nodes are frequently provisioned and deleted—it is critical to cleanly remove decommissioned servers from your MaxScale configuration. To delete a server using `maxctrl`, one has to unlink the server from any services or monitors beforehand. This step-by-step guide walks you through the safe removal process, following the recommended teardown sequence: Listener ➔ Service ➔ Monitor ➔ Server.

{% hint style="danger" %}
**Fast Track - Force Server Removal**

While we may remove a server with the `--force` method, please use this approach with caution. If you are scripting this for Kubernetes or need to quickly remove a node, you can bypass the manual unlinking steps by using the `--force` option.

The `--force` option will automatically remove the server from monitors and services before destroying it.

Bypassing the manual unlinking steps may abruptly terminate active database sessions. Only use this if traffic has already been safely drained from the node at the orchestration layer.

```bash
maxctrl destroy server mariadbgalera3 --force
```
{% endhint %}

{% stepper %}
{% step %}
### Destroy the Listener (If Applicable)

If your setup utilizes a dedicated listener that must be removed alongside the server, you must destroy the listener first.

* Destroying a listener closes the listening socket, opening it up for immediate reuse.
* If two arguments are given and they are a service and a listener, the listener is only destroyed if it is for the given service.

```bash
maxctrl destroy listener \
   Round-Robin-Service \
   Round-Robin-Listener
```
{% endstep %}

{% step %}
### Unlink the Server from the Service

Next, the server object for the node must be unlinked from the service.

* This command unlinks targets from a service, removing them from the list of available targets for that service.
* Unlink the server object from the service using the `unlink service` command.

```bash
maxctrl unlink service \
   Round-Robin-Service \
   mariadbgalera3
```

* Confirm that the server object was properly unlinked from the service

```bash
maxctrl show services
```
{% endstep %}

{% step %}
### Unlink the Server from the Monitor

The server object for the node must now be unlinked from its health monitor.

* This command unlinks servers from a monitor, removing them from the list of monitored servers.
* Unlink a server object from the monitor using the `unlink monitor` command.

```bash
maxctrl unlink monitor \
   MariaDB-Monitor \
   mariadbgalera3
```

* Confirm that the server object was properly unlinked from the monitor

```bash
maxctrl show monitors
```
{% endstep %}

{% step %}
### Destroy the Server in MaxScale

Finally, the server object for the node must be removed from MaxScale.

* The server must be unlinked from all services and monitor before it can be destroyed.
* Remove the server object using the `destroy server` command.

```bash
maxctrl destroy server \
   mariadbgalera3
```

* Confirm that the server object was properly removed

```bash
maxctrl show servers
```


{% endstep %}
{% endstepper %}
