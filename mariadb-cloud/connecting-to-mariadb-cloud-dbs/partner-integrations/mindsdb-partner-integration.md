# MindsDB Partner Integration

With the partnership between MariaDB and [MindsDB](https://mindsdb.com/), end-to-end machine learning is available to database services in MariaDB Cloud:

* MindsDB provides in-database machine learning, so you can make predictions in the database itself
* Organizations that leverage Machine Learning (ML) and Artificial Intelligence (AI) notice enhanced business efficiency and process improvement
* The partnership between MariaDB and MindsDB enables data teams to gain the benefits of machine learning quickly and easily by reducing the complexity of AI projects and providing easy-to-use machine learning tools

This page shows how to quickly build a machine learning project with the MindsDB Machine Learning platform and a database service in MariaDB Cloud.

This page includes links to MindsDB documentation and interfaces.

For additional information about MindsDB, see "[MindsDB: AI Tables Use Cases](https://mindsdb.com/machine-learning-use-cases)".

### Why MindsDB and MariaDB Cloud?

Organizations that leverage Machine Learning (ML) and Artificial Intelligence (AI) notice enhanced business efficiency and process improvement, but [the vast majority of data science projects never make it into production](https://venturebeat.com/ai/why-do-87-of-data-science-projects-never-make-it-into-production/). The partnership between MariaDB and MindsDB enables data teams to gain the benefits of machine learning quickly and easily by reducing the complexity of AI projects and providing easy-to-use machine learning tools.

MindsDB models explore MariaDB Cloud data interactively and iteratively while leveraging the cloud to speed up customers' execution of digital transformation journeys.

MariaDB Cloud is a database-as-a-service (DBaaS) enabling you to deploy and manage MariaDB Enterprise Server, Serverless Analytics, or ColumnStore analytical databases with only a few clicks. SkySQL combines automation with human expertise to support and manage mission-critical deployments.

When MindsDB is used with MariaDB Cloud, end-to-end machine learning is available to database services in MariaDB Cloud. MindsDB augments SQL code, so users can create, train, and auto-deploy machine learning models as if they were database tables.

Given the exponential growth of data, machine learning in MariaDB Cloud speeds up decision-making by asking predictive questions in the database itself to get the essential answers you need.

### Setup Procedure

1. [Register for MariaDB Cloud and MindsDB](mindsdb-partner-integration.md#step-1-register-for-mariadb-cloud-and-mindsdb)
2. [Connect MariaDB Cloud and MindsDB](mindsdb-partner-integration.md#step-2-connect-mariadb-cloud-and-mindsdb)
3. [Create machine learning models](mindsdb-partner-integration.md#step-3-create-machine-learning-models)
4. [Flow data into MariaDB Cloud](mindsdb-partner-integration.md#step-4-flow-data-into-mariadb-cloud)

### Step 1: Register for MariaDB Cloud and MindsDB

Before using MariaDB Cloud and MindsDB, both services require an account.

#### Register for MariaDB Cloud

MariaDB Cloud requires a [MariaDB ID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/mariadb-id-sign-up) account.

For the full procedure that shows how to quickly create a MariaDB ID account and launch a database service in MariaDB Cloud, see "[Quickstart](../../Quickstart/)".

#### Register for MindsDB

MindsDB requires a MindsDB Cloud account.

Providing your details, such as name, email address, and password, click Create Account.

Now you are redirected to the MindsDB Cloud Editor and ready to connect your database.

### Step 2: Connect MariaDB Cloud and MindsDB

To connect a database service in MariaDB Cloud to MindsDB, perform the following steps:

1.  Create a database service in MariaDB Cloud.

    For the full procedure that shows how to quickly create a MariaDB ID account and launch a database service in MariaDB Cloud, see "[Quickstart](../../Quickstart/)".
2.  Connect to the database service in MariaDB Cloud using a supported client.

    For information about which clients are supported and how to connect, see "[Connecting](../)".
3. Login to your MindsDB Cloud account.
4.  In the MindsDB Cloud Editor, execute a `CREATE DATABASE` statement to connect your MindsDB account to the the database service in MariaDB Cloud.

    ```sql
    CREATE DATABASE mariadb_cloud
    WITH ENGINE = "mariadb",
    PARAMETERS = {
      "user": "MARIADB_CLOUD_USER",
      "password": "MARIADB_CLOUD_PASSWORD",
      "host": "MARIADB_CLOUD_HOST",
      "port": "MARIDB_CLOUD_PORT",
      "ssl-ca": {"url": "MARIADB_CLOUD_CA_PATH"},
      "database": "SKYSQL_DB"
    };
    ```

    Replace the placeholders in the `CREATE DATABASE` statement above with your own [connection parameters](../#connecting-using-the-mariadb-client).

For the full instructions that show how to connect MindsDB with MariaDB SkySQL, see "[MindsDB: MariaDB SkySQL Setup Guide with MindsDB](https://docs.mindsdb.com/connect/connect-mariadb-skysql)" in the Learning Hub of the MindsDB Cloud Editor.

### Step 3: Create machine learning models

The machine learning models must be created.

MindsDB provides several sample data sets for you to start with:

* **Home Rentals**: Contains property details and predicts the rental price for new properties given their attributes.
* **House Sales**: A more advanced time-series problem, where, you train an ML model to predict future events based on historical data. The demo data set is a pre-processed version of the House Property Sales [Kaggle competition](https://www.kaggle.com/datasets/htagholdings/property-sales), which tracks quarterly moving averages of house sales aggregated by type (house or unit) and the number of bedrooms (between 1 and 5) in each listing.
* **Computer Sales**: Another time-series example, where you predict an average number of transistors for new CPU releases per month. This example showcases some data transformation techniques used before training the ML model.

MindsDB provides the sample data sets in a read-only database service in MariaDB Cloud. To access the sample data sets, use a `CREATE DATABASE` statement with the following connection parameters:

```sql
CREATE DATABASE skysql
WITH ENGINE = "mariadb",
PARAMETERS = {
  "user": "DB00007539",
  "password": "[DaS3I8g527n41637sFM|XtjjX",
  "host": "mindsdbtest.mdb0002956.db1.skysql.net",
  "port": "5001",
  "ssl-ca": {"url": "https://mindsdb-web-builds.s3.amazonaws.com/aws_skysql_chain.pem"},
  "database": "mindsdb_data"
};
```

#### Sample Data Set: Home Rentals

Follow this example to get a basic understanding of how machine learning works using MindsDB and MariaDB Cloud integration.

Once you have successfully connected to the demo database, start by viewing the data:

```
SELECT *
FROM skysql.home_rentals
LIMIT 5;
```

On execution, you get:

| `number_of_rooms` | `number_of_bathrooms` | `sqft` | `location` | `days_on_market` | `neighborhood` | `rental_price` |
| ----------------- | --------------------- | ------ | ---------- | ---------------- | -------------- | -------------- |
| 0                 | 1                     | 484    | great      | 10               | south\_side    | 2271           |
| 1                 | 1                     | 674    | good       | 1                | downtown       | 2167           |
| 1                 | 1                     | 554    | poor       | 19               | westbrae       | 1883           |
| 0                 | 1                     | 529    | great      | 3                | south\_side    | 2431           |
| 3                 | 2                     | 1219   | great      | 3                | south\_side    | 5510           |

You can now create and train a machine learning model. For that, you should use the `CREATE PREDICTOR` syntax and specify what query to train FROM (i.e., the home\_rentals table) and what you want to PREDICT:

```sql
CREATE PREDICTOR mindsdb.home_rentals_skysql_demo
FROM skysql
      (SELECT * FROM home_rentals)
PREDICT rental_price;
```

It may take a couple of minutes for the training to complete. To check the status of your predictor, run the command below.

```sql
SELECT *
FROM mindsdb.predictors
WHERE name='home_rentals_skysql_demo';
```

In this guide, you let the AutoML figure out the model parameters, and you can use [`DESCRIBE`](https://docs.mindsdb.com/sql/api/describe) commands to see how this model was built. On the other hand, the [`USING`](https://docs.mindsdb.com/sql/create/predictor#create-predictor-with-the-using-statement) syntax will give you full control over building your next model, but it will not be covered in this tutorial.

```sql
DESCRIBE mindsdb.home_rentals_skysql_demo;
DESCRIBE mindsdb.home_rentals_skysql_demo.features;
DESCRIBE mindsdb.home_rentals_skysql_demo.model;
DESCRIBE mindsdb.home_rentals_skysql_demo.ensemble;
```

Now, you are ready to make predictions by querying the model as if it were a database table. Start by querying predictions one by one, providing the details of a property in the `WHERE` clause.

```sql
SELECT rental_price,
    rental_price_explain
FROM mindsdb.home_rentals_skysql_demo
WHERE sqft = 823
AND location='good'
AND neighborhood='downtown'
AND days_on_market=10;
```

On execution, you get:

| `rental_price` | `rental_price_explain`                                                                                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 3166           | `{"predicted_value": 3166, "confidence": 0.99, "anomaly": null, "truth": null, "confidence_lower_bound": 2997, "confidence_upper_bound": 3335}` |

You can also make bulk predictions by joining the data table with the model table, which is more practical in most cases.

```sql
SELECT t.number_of_rooms, t.number_of_bathrooms, t.sqft,
       t.location, t.days_on_market,
       t.rental_price AS real_price,
       m.rental_price AS predicted_price
FROM skysql.home_rentals AS t
JOIN mindsdb.home_rentals_skysql_demo AS m
LIMIT 5;
```

On execution, you get:

| `number_of_rooms` | `number_of_bathrooms` | `sqft` | `location` | `days_on_market` | `real_price` | `predicted_price` |
| ----------------- | --------------------- | ------ | ---------- | ---------------- | ------------ | ----------------- |
| 0                 | 1                     | 484    | great      | 10               | 2271         | 2264              |
| 1                 | 1                     | 674    | good       | 1                | 2167         | 2175              |
| 1                 | 1                     | 554    | poor       | 19               | 1883         | 1915              |
| 0                 | 1                     | 529    | great      | 3                | 2431         | 2423              |
| 3                 | 2                     | 1219   | great      | 3                | 5510         | 5503              |

MindsDB provides rich SQL syntax for machine learning. There are various commands to accomplish tasks, such as [creating](https://docs.mindsdb.com/sql/create/predictor), [retraining](https://docs.mindsdb.com/sql/api/retrain), or [dropping](https://docs.mindsdb.com/sql/api/drop) a model, [creating or dropping a database](https://docs.mindsdb.com/sql/create/databases), tuning a model, and more. You can find an extensive description of these commands in the [SQL API section of the MindsDB docs](https://docs.mindsdb.com/sql/table-structure).

Let's move on to the next example.

#### Sample Data Set: House Sales

With this data set, you can explore a more advanced time-series problem and train an ML model to predict future events based on historical data. You will see some unique ML syntax for time-series models and how to build a multivariate model grouped by several attributes.

This data set is available inside the MariaDB Cloud database instance you have already connected to, so you can view the `house_sales` table immediately:

```sql
SELECT *
FROM skysql.house_sales
LIMIT 5;
```

On execution, you get:

| `saledate` | `ma`   | `type` | `bedrooms` |
| ---------- | ------ | ------ | ---------- |
| 2007-09-30 | 441854 | house  | 2          |
| 2007-12-31 | 441854 | house  | 2          |
| 2008-03-31 | 441854 | house  | 2          |
| 2008-06-30 | 441854 | house  | 2          |
| 2008-09-30 | 451583 | house  | 2          |

Now, let's specify the column to be forecasted, that is, the `MA` column, which is a moving average of the historical median price for house sales. However, looking at the data, you can see several entries for the same date. It depends on two factors: how many bedrooms the properties have (between 1 and 5), and whether properties are "houses" or "units". This means that you can have up to ten different groupings here. Let's look at the query for one of them:

```sql
SELECT saledate, ma, type, bedrooms
FROM skysql.home_rentals
WHERE type='house'
AND bedrooms=3;
```

Usually, you would need to generate forecasts to predict the behavior of this and the other series for the next year. With the classical ML approach, you need to train a separate model for each series.

But MindsDB makes it simple so that you don't need to repeat the predictor creation process for every group there is. Instead, you can just group for both columns, and the predictor learns from all series individually and as a whole and enables all forecasts! Here's how you can train such a predictor for multivariate time-series data:

```sql
CREATE PREDICTOR mindsdb.house_sales_predictor
FROM skysql
  (SELECT * FROM house_sales)
PREDICT ma
ORDER BY saledate
GROUP BY bedrooms, type
WINDOW 8
HORIZON 4;
```

Please note that the `house_sales` table stores quarterly sales. Thus, the last eight rows are used to get data from the past two years for making predictions (WINDOW 8). And to predict values for the next year, define the next four rows as predictions (HORIZON 4).

To check the status of your predictor, run the command below.

```sql
SELECT *
FROM mindsdb.predictors
WHERE name='house_sales_predictor';
```

Once the predictor's status is complete, you can start making predictions.

```sql
SELECT m.saledate AS date,
       m.MA AS forecast,
       MA_explain
FROM mindsdb.house_sales_predictor AS m
JOIN skysql.house_sales AS t
WHERE t.saledate > LATEST
AND t.type = 'house'
AND t.bedrooms = 2
LIMIT 4;
```

On execution, you get:

| `date`     | `forecast`        | `MA_explain`                                                                                                                                                                              |
| ---------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2019-12-31 | 441413.5849598734 | `{"predicted_value": 441413.5849598734, "confidence": 0.99, "anomaly": true, "truth": null, "confidence_lower_bound": 440046.28237074096, "confidence_upper_bound": 442780.88754900586}`  |
| 2020-04-01 | 443292.5194586229 | `{"predicted_value": 443292.5194586229, "confidence": 0.9991, "anomaly": null, "truth": null, "confidence_lower_bound": 427609.3325864327, "confidence_upper_bound": 458975.7063308131}`  |
| 2020-07-02 | 443292.5194585953 | `{"predicted_value": 443292.5194585953, "confidence": 0.9991, "anomaly": null, "truth": null, "confidence_lower_bound": 424501.59192981094, "confidence_upper_bound": 462083.4469873797}` |
| 2020-10-02 | 443292.5194585953 | `{"predicted_value": 443292.5194585953, "confidence": 0.9991, "anomaly": null, "truth": null, "confidence_lower_bound": 424501.59192981094, "confidence_upper_bound": 462083.4469873797}` |

Now, try changing the type to unit or bedrooms to any number between 1 to 5, and check how the forecast varies. This is because MindsDB recognizes each grouping as being its own different time series.

Let's move to the final example before looking at how to insert your predictions back into the SkySQL database.

#### Sample Data Set: Computer Sales

With this data set, you will see some data transformation techniques used before training an ML model. First, you create a view from the raw data and then create an ML model from that view.

Let's start by viewing the data:

```sql
SELECT *
FROM skysql.chip_dataset
LIMIT 3;
```

On execution, you get:

| `product`            | `type` | `release_date` | `process_size_mm` | `tdp_w` | `die_size_mm2` | `transistors_million` | `freq_mhz` | `foundry` | `vendor` |
| -------------------- | ------ | -------------- | ----------------- | ------- | -------------- | --------------------- | ---------- | --------- | -------- |
| AMD Athlon 64 3500+  | CPU    | 20 02 2007     | 65.0              | 45.0    | 77.0           | 122.0                 | 2200       | Unknown   | AMD      |
| AMD Athlon 200GE     | CPU    | 6 09 2018      | 14.0              | 35.0    | 192.0          | 4800.0                | 3200       | Unknown   | AMD      |
| Intel Core i5-1145G7 | CPU    | 2 09 2020      | 10.0              | 28.0    |                |                       | 2600       | Intel     | Intel    |

Let's transform our data by creating a view based on the above table.

```sql
CREATE VIEW moore_law (
SELECT YEAR(release_date)+'-'+MONTH(release_date) AS release_month,
      ROUND(AVG(transistors_million),2) AS mm_transistors
FROM skysql.chip_dataset
WHERE release_date!='NaT' and transistors_million!=''
GROUP BY YEAR(release_date), MONTH(release_date)
ORDER BY release_date
);
```

To check what's in the view, run this command:

```sql
SELECT *
FROM views.moore_law
LIMIT 3;
```

On execution, you get:

| `release_month` | `mm_transistors` |
| --------------- | ---------------- |
| 2000-3          | 34.5             |
| 2000-4          | 28               |
| 2000-6          | 29.53            |

Now you have a table that lists the average number of transistors available each month. Let's create a predictor to predict the mm\_transistors value using the data from the past 12 months and making predictions for the next 60 months.

```sql
CREATE PREDICTOR transistor_model
FROM views
  (SELECT * FROM moore_law)
PREDICT mm_transistors
ORDER BY release_month
WINDOW 12
HORIZON 60;
```

To check the status of your predictor, run the command below.

```sql
SELECT *
FROM mindsdb.predictors
WHERE name='transistor_model';
```

Once the training is complete, check the predictions.

```sql
SELECT m.release_month,
       m.mm_transistors AS forecast,
       mm_transistors_explain
FROM mindsdb.transistor_model AS m
JOIN views.moore_law AS t
WHERE t.release_month > LATEST
LIMIT 3;
```

On execution, you get:

| `release_month` | `forecast`         | `mm_transistors_explain`                                                                                                                                                                  |
| --------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2021-05-08      | 24090.65847928779  | `{"predicted_value": 24090.65847928779, "confidence": 0.99, "anomaly": true, "truth": null, "confidence_lower_bound": 23921.736345569123, "confidence_upper_bound": 24259.58061300646}`   |
| 2021-06-08      | 13761.411603853063 | `{"predicted_value": 13761.411603853063, "confidence": 0.99, "anomaly": null, "truth": null, "confidence_lower_bound": 13557.587970477267, "confidence_upper_bound": 13965.235237228859}` |
| 2021-07-09      | 7759.162632011563  | `{"predicted_value": 7759.162632011563, "confidence": 0.99, "anomaly": null, "truth": null, "confidence_lower_bound": 7548.124764220142, "confidence_upper_bound": 7970.200499802983}`    |

Let's look at how to make use of the predictions and insert them back into the SkySQL database.

#### How to Make Use of the Predictions

Now you know how to build and query models via SQL, as shown in the examples above. And here's how you can make use of predictions for your applications and analytical workloads.

* You can get predictive data into your custom apps by querying MindsDB directly using the `SELECT` statements, as shown in the examples.
* Or you can also write back prediction data into your database table for further processing and analysis. An easy way is to use the `INSERT INTO` statement that takes the query and inserts its output into your table. Please refer to the next section for more details.
* Finally, you can connect your BI tool to visualize the forecasts. It is helpful, especially in the case of multivariate time series predictions.

### Step 4: Flow data into MariaDB Cloud

You can use the `INSERT INTO` statement to write predictions back to the database. But before you run it, make sure to create an appropriate table in your personal MariaDB Cloud instance to store your predictions.

```sql
INSERT INTO my_mariadb_cloud_db.my_predictions_table (
SELECT t.number_of_rooms, t.number_of_bathrooms, t.sqft,
       t.location, t.days_on_market,
       t.rental_price AS real_price,
       m.rental_price AS predicted_price
FROM skysql.home_rentals AS t
JOIN mindsdb.home_rentals_skysql_demo AS m
LIMIT 5
);
```

Note: Please [connect your own MariaDB Cloud database](https://docs.mindsdb.com/connect/connect-mariadb-skysql), and change parameters my\_mariadb\_cloud\_db and my\_predictions\_table to your own values.

For more examples on the `INSERT INTO` statement, visit the [MindsDB doc page here](https://docs.mindsdb.com/sql/api/insert).

### Next Steps

* [MindsDB: Feature Engineering in MindsDB](https://docs.mindsdb.com/sql/feature-eng)
* [MindsDB: MindsDB and MLflow](https://docs.mindsdb.com/custom-model/mlflow)
* [Slack: MindsDB Community](https://mindsdbcommunity.slack.com/signup#/domain-signup)
