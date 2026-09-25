---
description: >-
  How model cross validation works in GridGain Machine Learning, using the CrossValidation class and k-fold validation.
---

# Model Cross Validation

## Overview

It is not good practice to learn the parameters of a prediction function and validate it on the same data. This leads to overfitting. To avoid this problem, one of the most efficient solutions is to save part of the training data as a validation set. However, by partitioning the available data and excluding one or more parts from the training set, we significantly reduce the number of samples which can be used for learning the model and the results can depend on a particular random choice for the pair of (train, validation) sets.

A solution to this problem is a procedure called cross-validation. In the basic approach, called k-fold CV, the training set is split into k smaller sets and after that the following procedure works: a model is trained using k-1 of the folds (parts) as a training data, the resulting model is validated on the remaining part of the data (it’s used as a test set to compute metrics such as accuracy).

Apache Ignite provides cross validation functionality that allows it to parameterize the trainer to be validated, metrics to be calculated for the model trained on every step and the number of folds training data should be split on.

## Usage

Cross validation functionality in Apache Ignite is represented by the class `CrossValidation`. This is a calculator parameterized by the type of model, type of label and key-value types of data. After instantiation (constructor doesn’t accept any additional parameters) we can use a score method to perform cross validation.

Let’s imagine that we have a trainer, a training set and we want to make cross validation using accuracy as a metric and using 4 folds. Apache Ignite allows us to do this as shown in the following example:

{% code title="Java" %}
```java
CrossValidation<DecisionTreeNode, Double, Integer, LabeledPoint> scoreCalculator = new CrossValidation<>();

double[] scores = scoreCalculator.score(
    trainer,
    new Accuracy<>(),
    ignite,
    trainingSet,
    (k, v) -> VectorUtils.of(v.x, v.y),
    (k, v) -> v.lb,
    4
);
```
{% endcode %}

In this example we specify trainer and metric as parameters, after that we pass common training arguments such as a link to the Ignite instance, cache, feature and label extractors, and finally specify the number of folds.This method returns an array containing metrics for all possible splits of the training set.

## Examples

To see how the Cross Validation can be used in practice, try [this example](https://github.com/apache/ignite-extensions/tree/master/modules/ml-ext/examples/src/main/java/org/apache/ignite/examples/ml/selection/cv/CrossValidationExample.java), and see [step 8 of the ML Tutorial](https://github.com/apache/ignite-extensions/tree/master/modules/ml-ext/examples/src/main/java/org/apache/ignite/examples/ml/tutorial), available on GitHub and delivered with every Apache Ignite distribution.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
