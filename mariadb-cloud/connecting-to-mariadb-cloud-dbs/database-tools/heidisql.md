# HeidiSQL

## Steps

1. Open HeidiSQL and create a new session.
2. Choose **MySQL** as the connection type.
3. Enter the MariaDB Cloud credentials including hostname, port, username, and password.
4. If SSL is enabled, go to the **SSL** tab.
5. Check **Use SSL**.
6. Test the connection and click **Open**.

![heidi](https://github.com/user-attachments/assets/37685278-b228-4387-9d48-8673d1d39e2d)

{% hint style="info" %}
Ensure your HeidiSQL client is up to date.
{% endhint %}

For more information on HeidiSQL, see [this page]({server}/clients-and-utilities/graphical-and-enhanced-clients/heidisql). 

{% hint style="warning" %}
Using updated drivers on new MariaDB versions is essential as out of date drivers will return "Authentication failed" errors. It may be nessecary to manually install new drivers on Windows.
{% endhint %}
