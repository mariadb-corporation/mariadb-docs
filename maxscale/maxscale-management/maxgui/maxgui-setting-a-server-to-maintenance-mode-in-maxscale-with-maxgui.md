# Setting a Server to Maintenance Mode in MaxScale with MaxGUI

## Overview

When using MaxScale, it is often necessary to temporarily remove a server from the load balancing pool without actually shutting down the server. This is usually needed to perform maintenance on the server, such as when upgrading the server's software or when performing schema upgrades.

MaxScale allows users to set servers to "maintenance mode", which prevents MaxScale from routing traffic to the server and prevents it from being elected as the new primary server during failover or switchover.

MaxGUI is a graphical utility that can perform administrative tasks using MaxScale's [MaxScale's REST API](../../reference/maxscale-rest-api/). It is available starting in [MaxScale 2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/maxscale/old-releases/2.5). It can be used to set a server to maintenance mode.

## Setting a Server to Maintenance Mode

1. [Configure MaxScale for MaxGUI](configuring-maxscale-for-maxgui.md).
2. Visit MaxGUI in your web browser.
   For example, if you are accessing it from local host with the default port, then visit this address: [127.0.0.1:8989](https://127.0.0.1:8989)
3. Enter your username and password to log in.
4. On the dashboard, the "Servers" tab is shown by default.
5. Click the server that you want to set to maintenance mode. This will bring up a page for the specific server.
6. Click the gear icon at the top left corner of the page next to the server name. This will show some options in a popup.
7. Click the pause icon. This will open a popup window.
8. Click the "Maintain" button.
   If the specified server is a primary server, then MaxScale will allow open transactions to complete before closing any connections.

## Forcing a Server to Maintenance Mode

1. [Configure MaxScale for MaxGUI](configuring-maxscale-for-maxgui.md)
2. Visit MaxGUI in your web browser.
   For example, if you are accessing it from local host with the default port, then visit this address: [127.0.0.1:8989](https://127.0.0.1:8989)
3. Enter your user and password to login.
4. On the dashboard, the "Servers" tab is shown by default.
5. Click the server that you want to set to maintenance mode. This will bring up a page for the specific server.
6. Click the gear icon at the top left corner of the page next to the server name. This will show some options in a popup.
7. Click the pause icon. This will open a popup window.
8. Check the "Force closing" checkbox.
9. Click the "Maintain" button.
   When the "Force closing" checkbox is specified, MaxScale immediately close all connections, even if the server is a primary server that has open transactions.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
