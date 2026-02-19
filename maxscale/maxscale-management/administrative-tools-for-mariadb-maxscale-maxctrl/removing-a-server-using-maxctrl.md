# Removing a Server using MaxCtrl

To safely remove a server node from MaxScale—especially in dynamic environments like Kubernetes where nodes are automatically provisioned or deleted—perform the following procedure. This procedure follows the recommended sequence: listener -> service -> monitor -> server.

{% hint style="info" %}
&#x20;**Fast Track - Force Server Removal**

If you are scripting this for Kubernetes or need to quickly remove a node, you can bypass the manual unlinking steps by using the `--force` option.

The `--force` option will automatically remove the server from monitors and services before destroying it.

```bash
maxctrl destroy server mariadbgalera3 --force
```
{% endhint %}

### Destroying the Listener in MaxScale

If your setup utilizes a dedicated listener that must be removed alongside the server, you must destroy the listener first:

* Destroying a listener closes the listening socket, opening it up for immediate reuse.
* If two arguments are given and they are a service and a listener, the listener is only destroyed if it is for the given service.

```bash
maxctrl destroy listener \
   Round-Robin-Service \
   Round-Robin-Listener
```

### Unlinking from Service in MaxScale

The server object for the node must be unlinked from the service:

* This command unlinks targets from a service, removing them from the list of available targets for that service.
* Unlink the server object from the service using the `unlink service` command.
* As the first argument, provide the name of the service.
* As the second argument, provide the name of the server.

```bash
maxctrl unlink service \
   Round-Robin-Service \
   mariadbgalera3
```

### Checking the Service in MaxScale

To confirm that the server object was properly unlinked from the service, the service should be checked:

* Show the services using the `show services` command, like this:

```bash
maxctrl show services
```

### Unlinking from Monitor in MaxScale

The server object for the node must be unlinked from the monitor:

* This command unlinks servers from a monitor, removing them from the list of monitored servers.
* Unlink a server object from the monitor using the `unlink monitor` command.
* As the first argument, provide the name of the monitor.
* As the second argument, provide the name of the server.

```bash
maxctrl unlink monitor \
   MariaDB-Monitor \
   mariadbgalera3
```

### Checking the Monitor in MaxScale

To confirm that the server object was properly unlinked from the monitor, the monitor should be checked:

* Show the monitors using the `show monitors` command, like this:

```bash
maxctrl show monitors
```

### Removing the Server from MaxScale

The server object for the node must also be removed from MaxScale:

* The server must be unlinked from all services and monitor before it can be destroyed.
* Remove the server object using the `destroy server` command.
* As the first argument, provide the name for the server.

```bash
maxctrl destroy server \
   mariadbgalera3
```

### Checking the Server in MaxScale

To confirm that the server object was properly removed, the server objects should be checked:

* Show the server objects using the `show servers` command, like this:

```bash
maxctrl show servers
```
