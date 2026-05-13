---
description: >-
  Connect to MariaDB Cloud with DBeaver, configuring the JDBC connection URL,
  TLS settings, and credentials in the DBeaver connection wizard.
---

# DBeaver

## Steps

1. Open DBeaver and create a new connection.
2. Select **MariaDB** as the database type.
3. Enter the hostname, port, username, and password provided by your MariaDB Cloud instance.
4. Navigate to the **SSL** tab.
5. Check the **Use SSL** option if SSL is enabled for your MariaDB Cloud instance.
6. Click **Test Connection** to ensure everything is set up correctly.

![image (1)](https://github.com/user-attachments/assets/fead6067-9a5a-4e75-bcf2-2d20e0a4b727)

{% hint style="info" %}
Ensure you are using the latest MariaDB driver in DBeaver to avoid compatibility issues.
{% endhint %}

{% hint style="warning" %}
If you experience connection issues, verify your firewall settings and database credentials.
{% endhint %}

