---
description: >-
  Specific considerations and steps for running MariaDB Docker containers on
  Amazon EC2 instances.
---

# Docker and AWS EC2

This process shows how to deploy MariaDB in a Docker container running on an EC2 instance. First we'll create the EC2 VM, then we'll deploy Docker to it. After that, we'll pull the MariaDB Docker image which we'll use to create a running container with a MariaDB instance. Finally, we'll load a sample database into the MariaDB instance.

### **Create a VM in AWS EC2**

1. Install [MariaDB client](../../../clients-and-utilities/mariadb-client/) on your local machine, either bundled with Maria DB server or standalone.
2. Login to AWS, navigate to [EC2 service home](https://console.aws.amazon.com/ec2/home)
3. Choose Region for EC2 in the upper right corner of the console
4. Launch (1) Instance, giving instance a name (e.g. mrdb-ubuntu-docker-use1) and create or re-use a key pair
5. Choose Ubuntu 22.04 or similar free tier instance
6. Choose hardware, t2.micro or similar free tier instance
7. Create Key Pair with name (e.g. mrdb-docker-aws-pk.pem if using openSSH at the command line, or mrdb- docker-aws-pk..ppk for use with programs like PuTTY.)
8. Create or select a security group where SSH is allowed from anywhere 0.0.0.0/0. If you’d like to make this more secure, it can be restricted to a specific IP address or CIDR block.

```django
{{aws-firewall}}
```

10. Accept remaining instance creation defaults and click “launch instance”.
11. Save the \*.pem or \*.ppk keyfile on your local hard drive when prompted. You will need it later. If you’re on Linux, don’t forget to change permissions on the downloaded \*.pem / \*.ppk key file:

```bash
$ chmod 400 mrdb-docker-pk.pem
```

12. Click into the instance summary (EC2 > Instances > Instance ID) and click on the “security” tab towards the bottom.

```django
{{security-group}}
```

13. In the relevant security group for your instance, Create an inbound rule so that TCP port 3306 is open, allowing external connections to Maria DB (like your local command line client for MariaDB). Double check that port 22 is open while you're there for SSH.

### **Install Docker on the EC2 VM**

For more detailed instructions, refer to [Installing and Using MariaDB via Docker](installing-and-using-mariadb-via-docker.md)

14. Back in the instance summary (EC2 > Instances > Instance ID), copy the public IP (e.g. ww.xx.yyy.zzz)

```django
{{aws-instance-ip}}
```

15. Open terminal window, navigate to the directory with private key (\*.pem or \*.ppk) file and start a SSH remote shell session by typing:

```bash
$ ssh -i mrdb-docker-pk.pem ubuntu@ww.xx.yyy.zzz
```

(switch ww.xx.yyy.zzz for your IP address from step 14).

16. Are you sure you want to continue connecting (yes/no/\[fingerprint])?\
    Say yes
17. Escalate to root

```bash
$ sudo su
```

18. Install Docker

```bash
$ curl -fsSL https://get.docker.com | sudo sh
```

### Pull the Mariadb Docker Image and Create the Container

19. Pull MariaDB Docker image

```bash
$ docker pull mariadb:lts
```

20. Start MDRB docker process at your terminal / command line

```bash
$ docker run --detach --name mariadb-docker -v \Users\YouUID\Documents\YourDirName:/var/lib/mysql:Z -p 3306:3306 -e MARIADB_ROOT_PASSWORD=yoursecurepassword mariadb:lts
```

To ensure persistent storage, use the `-v` flag to mount your chosen directory as `/var/lib/mysql`. For Windows, represent file paths like `C:\Users\YourUID\Documents\YourDirName` accordingly. On Linux, use absolute file paths. Always replace the root password with a secure one, especially outside of development environments.

21. Shell into container

```bash
$ docker exec -it mariadb-docker bash
```

22. Login to MRDB inside container using the root password specified in step 20.

```bash
$ mariadb -pyoursecurepassword
```

23. Setup admin account with permission for remote connection, configure access control

```sql
MariaDB [(none)]> CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';

MariaDB [(none)]> GRANT ALL ON *.* to 'admin'@'%' WITH GRANT OPTION;

MariaDB [(none)]> SHOW GRANTS FOR admin;
```

Obviously replace these passwords with something that is a bit more secure than you see in this example for anything other than development purposes.

24. Setup service account for your app with permission for remote connection, configure access control

```sql
MariaDB [(none)]> CREATE USER 'yourappname'@'%' IDENTIFIED BY 'yoursecurepassword';

MariaDB [(none)]> GRANT INSERT, UPDATE, DELETE ON *.* to 'yourappname'@'%';

MariaDB [(none)]> SHOW GRANTS FOR yourappname;
```

Obviously replace these passwords with something that is a bit more secure than you see in this example for anything other than development purposes.

25. Load up your database from your preexisting SQL script that contains [CREATE DATABASE](../../../reference/sql-statements/data-definition/create/create-database.md); [USE DATABASE](../../../reference/sql-statements/administrative-sql-statements/use-database.md); and [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statements.

Open a new terminal window (not your SSH session) and navigate to the directory containing your database creation script, for example, `init.sql`. Then, enter the command:

```bash
$ mariadb --host=ww.xx.yyy.zzz --port=3306 --user=admin --password=admin -e “SOURCE init.sql”
```

(switch ww.xx.yyy.zzz for your IP address from step 14).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
