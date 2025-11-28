# ERD Designer

Enterprise manager provides a visual interface for creating entity relationship diagrams (ERD) and for observing existing database schemas, so you can quickly understand table relationships, identify dependencies, and visually assess the impact of schema changes before implementation.

This procedure outlines the steps required to access and utilize the ERD Designer within the Workspace section of Enterprise Manager UI. 

1.  From the main Workspace screen, click the "Run Queries" card.\


    <figure><img src="../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  In the "Connect to..." dialog, select your target server, enter your credentials, and click Connect.\


    <figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Upon successful connection, the main ERD worksheet will appear.\


    <figure><img src="../../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

## **Creating ERD diagram**

{% stepper %}
{% step %}
### Initiate generation

1. From the ERD Worksheet\
   On ERD Designer worksheet, click **Generate ERD**

<figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

2. From the Query Editor\
   In the **Query Editor**, right-click on a schema name in the **Schemas Sidebar** and select the **"Generate ERD"** option.

<figure><img src="../../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Select schema, and tables

A dialog will appear. Choose the specific schema you want to visualize. You may select which tables within that schema to include in the diagram.

<figure><img src="../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Visualize

Click the Visualize button to generate and display the ERD on the worksheet canvas.

<figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

## ERD Worksheet Features

The core of the designer is a visual canvas where you can build and manage your database structures.

<figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### **Model Tables, Indexes, and Relationships**

You can graphically manage all core MariaDB schema objects.

<figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

#### **Create New Tables**

Use the toolbar or right-click on the canvas to add new table entities to your diagram.

#### **Edit Entities**

Double-click any table to open the **Entity Editor** at the bottom of the screen. 

<figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

Here, you can define and modify columns (including data types and `NOT NULL` constraints), indexes, and foreign keys through an intuitive interface.

#### **Draw Foreign Keys**

To create a new relationship, simply click the connection point on a column in one table and drag it to the column it references in another table.

#### **Auto Layout**

For large or complex schemas, the diagram can become cluttered. Use the **Auto Arrange Entities** feature, typically found in the top toolbar, to automatically rearrange the tables and relationships into a clean, organized, and easily navigable diagram.

### Working with the ERD Worksheet

The ERD worksheet provides several tools and shortcuts to streamline your workflow.

#### **Managing Foreign Keys**

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Right-click on a relationship link between two tables to open a context menu with quick actions, such as editing or removing the foreign key, toggling the relationship type (e.g., one-to-one vs. one-to-many), and changing `NOT NULL` constraints.

#### **Exporting Your Model**

Once your design is complete, you can export it for documentation or deployment. The export options, found in the toolbar or by right-clicking the canvas, include the following:

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

* **Export as SQL Script:** Generates the `CREATE TABLE` and `ALTER TABLE` statements for your entire diagram.
* **Export as JPEG:** Creates an image of your diagram for use in presentations or other documents.
* **Copy script to clipboard:** A quick way to get the SQL for pasting elsewhere.

#### **Applying Changes to a Database**

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Click the **"Apply Script"** button (▶) in the toolbar to execute the generated SQL against your connected database. This allows you to deploy your new or modified schema directly from the designer.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
