---
description: >-
  Secure the JMX server that GridGain nodes start, by disabling remote JMX or
  enabling password authentication and SSL.
---

# Securing JMX

## Enabling JMX Security

When a GridGain node is started using the `ignite.[sh|bat]` script, it automatically starts a JMX server and allows remote connections from monitoring tools like VisualVM. While this gives good monitoring capabilities (e.g., exposes all metrics via MX beans), it's not secure.

If you don't need to connect to nodes via JMX, you can simply disable it via the `-nojmx` command line argument:

```shell
./ignite.sh -nojmx
```

In this case you should see a line like this in the log:

```shell
[18:45:20,178][INFO][main][IgniteKernal] Remote Management [restart: on, REST: on, JMX (remote: off)]
```

Here, `JMX (remote: off)` indicates that JMX is disabled.

If you still need JMX connectivity, it can be secured with login/password authentication and/or SSL.

{% hint style="info" %}
Refer to the [official JMX documentation](https://docs.oracle.com/en/java/javase/11/management/monitoring-and-management-using-jmx-technology.html#GUID-D4CBA2D6-2E24-4856-A7D8-62B3DFFB76EA) for the information on.
{% endhint %}

To enable simple file-based authentication, you need to do the following:

1. Go to the `JRE_HOME/lib/management` folder and rename the `jmxremote.password.template` file to `jmxremote.password`.
2. Open the `jmxremote.password` file in any editor and uncomment last two lines (you can also change the passwords if you want):

   ```text
   monitorRole  QED
   controlRole  R&D
   ```

3. Change permissions of the `jmxremote.password` file so that only the user can read and write it:

   ```shell
   chmod 600 jmxremote.password
   ```

4. Start a GridGain node with JMX authentication enabled:

   ```shell
   ./ignite.sh -J-Dcom.sun.management.jmxremote.authenticate=true
   ```

   You should see this line in the log:

   ```shell
   [18:13:46,747][INFO][main][IgniteKernal] Remote Management [restart: on, REST: on, JMX (remote: on, port: 49115, auth: on, ssl: off)]
   ```

Authentication is now enabled. If you try to connect to port 49115 using VisualVM or any other tool, you will be asked for a username and password.

{% hint style="info" %}
You may be required to have root access to execute some of the above commands.
{% endhint %}

## Advanced Authentication Techniques

File-based authentication as described above doesn't provide enough security in most cases and is suitable only during the development process. When running in production, you should consider using SSL and secure authentication protocols (like LDAP). For more information and details refer to this [Oracle documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
