---
description: >-
  How to import pre-trained Machine Learning models from Apache Spark ML and XGBoost into GridGain for distributed inference.
---

# Model Importing

GridGain supports importing Machine Learning models from external platforms including Apache Spark ML and XGBoost. Working with imported models, you can:

- store imported models in Ignite for further inference,
- use imported models as part of pipelines,
- apply ensembling methods such as boosting, bagging, or stacking to those models.

Also, imported pre-trained models can be updated inside GridGain.

GridGain provides an API for distributed inference for models trained in Apache Spark ML and XGBoost. These models cannot be modified via GridGain. GridGain provides a common API and you just need to use the right parser implementation to work with your specific external lib.

## Model Import from Apache Spark

### Model import from Apache Spark via Parquet files

GridGain supports the following models for import from Apache Spark ML:

- Logistic regression (`org.apache.spark.ml.classification.LogisticRegressionModel`)
- Linear regression (`org.apache.spark.ml.classification.LogisticRegressionModel`)
- Decision tree (`org.apache.spark.ml.classification.DecisionTreeClassificationModel`)
- Support Vector Machine (`org.apache.spark.ml.classification.LinearSVCModel`)
- Random forest (`org.apache.spark.ml.classification.RandomForestClassificationModel`)
- K-Means (`org.apache.spark.ml.clustering.KMeansModel`)
- Decision tree regression (`org.apache.spark.ml.regression.DecisionTreeRegressionModel`)
- Random forest regression (`org.apache.spark.ml.regression.RandomForestRegressionModel`)
- Gradient boosted trees regression (`org.apache.spark.ml.regression.GBTRegressionModel`)
- Gradient boosted trees (`org.apache.spark.ml.classification.GBTClassificationModel`)

This feature works with models saved in `snappy.parquet` files.

Here is an example of importing a model from Apache Spark ML via Apache Parquet:

{% code title="Java" %}
```java
DecisionTreeNode mdl = (DecisionTreeNode)SparkModelParser.parse(
   SPARK_MDL_PATH,
   SupportedSparkModels.DECISION_TREE
);
```
{% endcode %}

You can see more examples of using this API in the examples module in the package: `org.apache.ignite.examples.ml.inference.spark.modelparser`

### Model import from Apache Spark via MLeap

In this mode you cannot update models or pipelines saved with MLeap, but you can import them and perform distributed inference.

For distributed inference, use the `AsyncModelBuilder` interface. Using this interface you can import a model or pipeline for local or distributed inference. For local inference (inference on the same node where you perform import) you can use `ThreadedModelBuilder`. For distributed inference, use the `IgniteDistributedModelBuilder` implementation of the `AsyncModelBuilder` interface.

This is an example of model import in a distributed manner:

{% code title="Java" %}
```java
File mdlRsrc = IgniteUtils.resolveIgnitePath(TEST_MODEL_RES);

ModelReader reader = new FileSystemModelReader(mdlRsrc.getPath());

MLeapModelParser parser = new MLeapModelParser();

AsyncModelBuilder mdlBuilder = new IgniteDistributedModelBuilder(ignite, 4, 4);

Model<NamedVector, Future<Double>> mdl = mdlBuilder.build(reader, parser);
```
{% endcode %}

In this example, we imported a model and deployed 4 instances in our cluster with the limit of maximum model instances per node.

Detailed examples are located in the example module in the package: `org.apache.ignite.examples.ml.mleap`

## Model Import from GXBoost

You can import pre-trained models from XGBoost for local or distributed inference.

{% code title="Java" %}
```java
File mdlRsrc = IgniteUtils.resolveIgnitePath(TEST_MODEL_RES);

ModelReader reader = new FileSystemModelReader(mdlRsrc.getPath());

XGModelParser parser = new XGModelParser();

AsyncModelBuilder mdlBuilder = new IgniteDistributedModelBuilder(ignite, 4, 4);

Model<NamedVector, Future<Double>> mdl = mdlBuilder.build(reader, parser);
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
