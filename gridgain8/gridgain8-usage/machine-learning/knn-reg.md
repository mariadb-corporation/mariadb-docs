---
description: >-
  How the k-NN (k-nearest neighbors) regression algorithm works in GridGain Machine Learning, including its parameters and an example.
---

# k-NN Regression

The Apache Ignite Machine Learning component provides two versions of the widely used k-NN (k-nearest neighbors) algorithm - one for classification tasks and the other for regression tasks.

This documentation reviews k-NN as a solution for the regression tasks.

## Model description

The k-NN algorithm is a non-parametric method whose input consists of the k-closest training examples in the feature space. Each training example has a property value in a numerical form associated with the given training example.

The k-NN algorithm uses all training sets to predict a property value for the given test sample.
This predicted property value is an average of the values of its `k` nearest neighbors. If `k` is `1`, then the test sample is simply assigned to the property value of a single nearest neighbor.

Presently, Ignite supports a few parameters for the k-NN regression algorithm:

- `k` - a number of nearest neighbors.
- `distanceMeasure` - one of the distance metrics provided by the ML framework such as Euclidean, Hamming, or Manhattan.
- `KNNStrategy` - could be SIMPLE or WEIGHTED (it enables a weighted k-NN algorithm),
- `datasetBuilder` - helps to get access to the training set of objects for which the class is already known.

{% code title="Java" %}
```java
// Create trainer
KNNRegressionTrainer trainer = new KNNRegressionTrainer();

// Train model.
KNNRegressionModel knnMdl = (KNNRegressionModel) trainer.fit(
      datasetBuilder,
      (k, v) -> Arrays.copyOfRange(v, 1, v.length),
      (k, v) -> v[0])
  .withK(5)
  .withDistanceMeasure(new ManhattanDistance())
  .withStrategy(KNNStrategy.WEIGHTED);

// Make a prediction.
double prediction = knnMdl.apply(vectorizedData);
```
{% endcode %}

## Example

An example of the k-NN regression is included in the GridGain distribution package.

The training dataset is the Computer Hardware Data Set which can be loaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Computer+Hardware).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
