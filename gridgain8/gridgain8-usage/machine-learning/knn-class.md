---
description: >-
  How the k-NN (k-nearest neighbors) classification algorithm works in GridGain Machine Learning, including its parameters and an example.
---

# k-NN Classification

The Apache Ignite Machine Learning component provides two versions of the widely used k-NN (k-nearest neighbors) algorithm - one for classification tasks and the other for regression tasks.

This documentation reviews k-NN as a solution for classification tasks.

## Model description

The k-NN algorithm is a non-parametric method whose input consists of the k-closest training examples in the feature space.

Also, k-NN classification's output represents a class membership. An object is classified by the majority votes of its neighbors. The object is assigned to a particular class that is most common among its `k` nearest neighbors. `k` is a positive integer, typically small. There is a special case when `k` is `1`, then the object is simply assigned to the class of that single nearest neighbor.

Presently, Ignite supports a few parameters for k-NN classification algorithm:

- `k` - a number of nearest neighbors.
- `distanceMeasure` - one of the distance metrics provided by the ML framework such as Euclidean, Hamming, or Manhattan.
- `KNNStrategy` - could be SIMPLE or WEIGHTED (it enables a weighted k-NN algorithm).
- `dataCache` - holds a training set of objects for which the class is already known.

{% code title="Java" %}
```java
// Create trainer
KNNClassificationTrainer trainer = new KNNClassificationTrainer();

// Train model.
KNNClassificationModel knnMdl = trainer.fit(
    ignite,
    dataCache,
    (k, v) -> Arrays.copyOfRange(v, 0, v.length - 1),
    (k, v) -> v[2]
)
  .withK(3)
  .withDistanceMeasure(new EuclideanDistance())
  .withStrategy(KNNStrategy.SIMPLE);

// Make a prediction.
double prediction = knnMdl.apply(vectorizedData);
```
{% endcode %}

## Example

An example of kNN Classification is included in the GridGain distribution package.

The training dataset is the Iris dataset which can be loaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
