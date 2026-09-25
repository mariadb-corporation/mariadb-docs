---
description: >-
  How the K-Means clustering algorithm works in GridGain Machine Learning, including the model and trainer parameters.
---

# K-Means Clustering

The Apache Ignite Machine Learning component provides a K-Means clustering algorithm implementation.

## Model

K-Means clustering aims to partition `n` observations into `k` clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.

The model holds a vector of `k` centers and one of the distance metrics provided by the ML framework such as Euclidean, Hamming or Manhattan.

It enables predictions for a given vector of features in the following way:

{% code title="Java" %}
```java
KMeansModel mdl = ...;

double prediction = model.predict(observation);
```
{% endcode %}

## Trainer

KMeans is a unsupervised learning algorithm. It solves a clustering task which is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters).

KMeans is a parametrized iterative algorithm which calculates the new means to be the centroids of the observations in the clusters on each iteration.

Presently, Ignite supports a few parameters for the KMeans classification algorithm:

- `k` - a number of possible clusters
- `maxIterations` - one stop criteria (the other one is epsilon)
- `epsilon` - delta of convergence (delta between old and new centroid's values)
- `distance` - one of the distance metrics provided by the ML framework such as Euclidean, Hamming or Manhattan
- `seed` - one of initialization parameters which helps to reproduce models (trainer has a random initialization step to get the first centroids)

{% code title="Java" %}
```java
// Set up the trainer
KMeansTrainer trainer = new KMeansTrainer()
   .withDistance(new EuclideanDistance())
   .withK(AMOUNT_OF_CLUSTERS)
   .withMaxIterations(MAX_ITERATIONS)
   .withEpsilon(PRECISION);

// Build the model
KMeansModel knnMdl = trainer.fit(
  datasetBuilder,
  featureExtractor,
  labelExtractor
);
```
{% endcode %}

## Example

To see how K-Means clustering can be used in practice, try this example that is available on GitHub and delivered with every Apache Ignite distribution.

The training dataset is the subset of the Iris dataset (classes with labels 1 and 2, which are presented linear separable two-classes dataset) which can be loaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
