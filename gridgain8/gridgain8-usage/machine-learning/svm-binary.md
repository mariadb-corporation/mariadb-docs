---
description: >-
  How the linear SVM binary classification algorithm works in GridGain Machine Learning, including the model and trainer parameters.
---

# SVM Binary Classification

Support Vector Machines (SVMs) are supervised learning models with associated learning algorithms that analyze data used for classification and regression analysis.

Given a set of training examples, each marked as belonging to one or the other of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-probabilistic binary linear classifier.

Only Linear SVM is supported in the Apache Ignite Machine Learning module. For more information look at [SVM in Wikipedia](https://en.wikipedia.org/wiki/Support_vector_machine).

## Model

A Model in the case of SVM is represented by the class SVMLinearBinaryClassificationModel. It enables a prediction to be made for a given vector of features, in the following way:

{% code title="Java" %}
```java
SVMLinearBinaryClassificationModel model = ...;

double prediction = model.predict(observation);
```
{% endcode %}

Presently Ignite supports the following parameters for `SVMLinearBinaryClassificationModel`:

- `isKeepingRawLabels` - controls the output label format: -1 and +1 for false value and raw distances from the separating hyperplane (default value: `false`)
- `threshold` - a threshold to assign +1 label to the observation if the raw value is more than this threshold (default value: `0.0`)

{% code title="Java" %}
```java
SVMLinearBinaryClassificationModel model = ...;

double prediction = model
  .withRawLabels(true)
  .withThreshold(5)
  .predict(observation);
```
{% endcode %}

## Trainer

Base class for a soft-margin SVM linear classification trainer based on the communication-efficient distributed dual coordinate ascent algorithm (CoCoA) with hinge-loss function. This trainer takes input as a Labeled Dataset with -1 and +1 labels for two classes and makes binary classification.

The paper about this algorithm could be found here [https://arxiv.org/abs/1409.1458](https://arxiv.org/abs/1409.1458).

Presently, Ignite supports the following parameters for `SVMLinearBinaryClassificationTrainer`:

- `amountOfIterations` - amount of outer SDCA algorithm iterations. (default value: `200`)
- `amountOfLocIterations` - amount of local SDCA algorithm iterations. (default value: `100`)
- `lambda` - regularization parameter (default value: `0.4`)

{% code title="Java" %}
```java
// Set up the trainer
SVMLinearBinaryClassificationTrainer trainer = new SVMLinearBinaryClassificationTrainer()
  .withAmountOfIterations(AMOUNT_OF_ITERATIONS)
  .withAmountOfLocIterations(AMOUNT_OF_LOC_ITERATIONS)
  .withLambda(LAMBDA);

// Build the model
SVMLinearBinaryClassificationModel mdl = trainer.fit(
  datasetBuilder,
  featureExtractor,
  labelExtractor
);
```
{% endcode %}

## Example

An example of the SVM Linear Classifier is included in the GridGain distribution package.

The training dataset is the subset of the Iris dataset (classes with labels 1 and 2, which are presented linear separable two-classes dataset) which could be loaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
