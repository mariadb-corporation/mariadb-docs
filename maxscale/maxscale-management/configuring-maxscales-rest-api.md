---
description: >-
  Enable remote management by configuring the MaxScale REST API. Learn to set
  listening ports, bind addresses, and secure administrative traffic with TLS.
---

# Configuring MaxScale's REST API

## Overview

MaxScale's MaxScale's REST API is used by both [MaxCtrl](administrative-tools-for-mariadb-maxscale-maxctrl/) and [MaxGUI](maxgui/).

The REST API is enabled by default. However, the default configuration is not optimal for production systems, because:

* It only allows requests from the local host address by default.
* It does not use TLS by default.
* It used a hard-coded user (admin) and password (mariadb) by default.

## Configuring MaxScale's REST API for Remote Connections

1. [Configure MaxScale's REST API](maxgui/configuring-maxscale-for-maxgui.md) for remote connections by configuring several global parameters in maxscale.cnf.

| Parameter                                                                                           | Description                                                                                                 |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [admin\_host](deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_host) | • This parameter defines the network address that the REST API listens on.• The default value is 127.0.0.1. |
| [admin\_port](deployment/installation-and-configuration/maxscale-configuration-guide.md#admin_port) | • This parameter defines the network port that the REST API listens on.• The default value is 8989.         |

For example:

```
[maxscale]
...
admin_host            = 0.0.0.0
admin_port            = 8443
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
