---
description: >-
  Learn how to use dbForge Studio, a GUI tool, to perform backup and restore
  operations for MariaDB databases visually.
---

# Backup and Restore via dbForge Studio

{% hint style="info" %}
dbForge Studio is a proprietary third-party tool, not included with MariaDB Server. Content contributed by devart.
{% endhint %}

In the modern world, data importance is non-negotiable, and keeping data integrity and consistency is the top priority. Data stored in databases is vulnerable to system crashes, hardware problems, security breaches, and other failures causing data loss or corruption. To prevent database damage, it is important to back the data up regularly and implement the data restore policies.\
MariaDB, one of the most popular database management systems, provides several methods to configure routines for backing up and recovering data. The current guideline illustrates both processes performed with the help of dbForge Studio for MySQL which is also a fully-functional [GUI client for MariaDB](https://www.devart.com/dbforge/mysql/studio/mariadb-gui-client.html) that has everything you need to accomplish the database-related tasks on MariaDB.

## Create the backup on MariaDB

dbForge Studio for MySQL and MariaDB has a separate module dedicated to the data backing up and recovering jobs. Let us first look at how set the tool to create a MariaDB backup.\
Launch the Studio and go to **Database > Backup and Restore > Backup Database**. The **Database Backup Wizard** with several pages will appear.\
On the General page, specify the database in question and how to connect to it, then choose where to save the created backup file, and specify its name. There are additional optional settings – you can select to delete old files automatically, zip the output backup file, etc. When done, click **Next**.

![b1](<../../.gitbook/assets/b1 (1).png>)

On the **Backup content** page, select the objects to back up. Click **Next**.

![b2](<../../.gitbook/assets/b2 (1).png>)

The **Options** page. Here you can specify the details of the data backing up process. Plenty of available options allow you to configure this task precisely to meet the specific requirements. When done, click **Next**.

![b3](<../../.gitbook/assets/b3 (1).png>)

The **Errors handling** page. Here you configure how the Studio should handle the errors that might occur during the backing up process. Also, you can set the Studio to write the information about the errors it encountered into the log file.

You can save the project settings to apply them in the future. For this, in the left bottom corner of the Wizard, select one of the saving options: **Save Project** or **Save Command Line**. The latter allows saving settings as a backup script which you can execute from the command line at any time later.

The configuration process is complete. Click Backup to launch the data backing up.

Note: It is not obligatory to go through all the pages of the Wizard. The Backup button is available no matter on which page you are. Thus, you can launch the process of backing the data up whenever you have set everything you needed.

![b4](<../../.gitbook/assets/b4 (1).png>)

After you have clicked **Backup**, dbForge Studio for MySQL starts to create a MariaDB backup.

![b5](<../../.gitbook/assets/b5 (1).png>)

When this is done, you will see the confirmation message. Click **Finish**.

![b6](<../../.gitbook/assets/b6 (1).png>)

Backup and restore policies suggest creating regular backups on a daily, weekly, monthly, quarterly, and yearly basis. Besides, to minimize the consequences of possible data loss, it is highly recommended make a backup before making any changes to a database, such as upgrading, modifying data, redesigning the structure, etc. Simply speaking, you always need a fresh backup to restore the most up-to-date database version.\
To ensure regular backups on schedule, you can use a batch file created with the help of the Studio and **Windows Task Scheduler**, where you need to create and schedule the backup task.

## Restore the backup file on MariaDB

This is an even faster task, done in half as many steps.

The process of data recovery from the backup file is simple. It only takes several clicks:\
Launch dbForge Studio for MySQL and go to **Database > Backup and Restore > Restore Database**. The **Database Restore Wizard** will appear.\
Specify the database name, its connection parameters, and the path to the backup file you want to restore. Then click **Restore**, and the process will start immediately.

![r1](<../../.gitbook/assets/r1 (1).png>)

When the process is complete, click **Finish**.

![r2](<../../.gitbook/assets/r2 (1).png>)

More information about this essential feature is available on the [dedicated backup and restore page](https://www.devart.com/dbforge/mysql/studio/mysql-backup.html) – it explores the routines performed on MySQL, but they fully apply to MariaDB backups. You can use the same IDE and the same workflow.

To test-drive this and other features of the Studio (the IDE includes all the tools necessary for the development, management, and administration of databases on MariaDB), [download dbForge Studio for a free 30-day trial](https://www.devart.com/dbforge/mysql/studio/download.html). dbForge Studio for MySQL and MariaDB boasts truly advanced functionality that will help your teams deliver more value.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
