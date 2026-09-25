---
description: >-
  How gradient boosting (GDB) works in GridGain Machine Learning, including the model, trainer parameters, and convergence checkers.
---

# Gradient Boosting

Gradient boosting is a machine learning technique that produces a prediction model in the form of an [ensemble](https://en.wikipedia.org/wiki/Ensemble_learning) of weak prediction models. A gradient boosting algorithm tries to solve the minimization error problem on learning samples in a functional space where each function is a model. Each model in this composition tries to predict a gradient of error for points in a feature space and these predictions will be summed with some weight to model an answer. This algorithm may be used for regression and classification problems. For more information please see [Wikipedia](https://en.wikipedia.org/wiki/Gradient_boosting).

In Ignite ML there is an implementation of a general GDB algorithm and GDB-on-trees algorithm. General GDB (`GDBRegressionTrainer` and `GDBBinaryClassifierTrainer`) allows any trainer for training each model in composition. GDB on trees uses some optimizations specific for trees, such as indexes, for avoiding sorting during the decision tree build phase.

## Model

Apache Ignite ML purposes all implementations of the GDB algorithm to use GDBModel, wrapping ModelsComposition for representing the composition of a few models. ModelsComposition implements a common Model interface and can be used as follows:

{% code title="Java" %}
```java
GDBModel model = ...;
double prediction = model.apply(featureVector);
```
{% endcode %}

GDBModel uses `WeightedPredictionsAggregator` as the model answer reducer. This aggregator computes an answer of a meta-model, since "result = bias + p1w1 + p2w2 + ..." where:

- `pi` - answer of i-th model.
- `wi` - weight of model in composition.

GDB uses the mean value of labels for the bias-parameter in the aggregator.

## Trainer

Training of GDB is represented by `GDBRegressionTrainer`, `GDBBinaryClassificationTrainer`, `GDBRegressionOnTreesTrainer`, and `GDBBinaryClassificationOnTreesTrainer` for general GDB and GDB on trees respectively. All trainers have the following parameters:

- `gradStepSize` - sets the constant weight of each model in composition; in future versions of Ignite ML this parameter may be computed dynamically.
- `cntOfIterations` - sets the maximum of models in the composition after training.
- `checkConvergenceFactory` - sets factory for construction of convergence checker used for preventing overfitting and learning of many useless models while training.

For classifier trainers there is addition parameter:

- `loss` - sets loss computer on some learning example from a training dataset.

There are several factories for convergence checkers:

- `ConvergenceCheckerStubFactory` creates a checker that always returns false for a convergence check. So in this case, model composition size will have cntOfIterations models.
- `MeanAbsValueConvergenceCheckerFactory` creates a checker that compute a mean value of the absolute gradient values on each example from a dataset and returns true if this it is less than the used-defined threshold.
- `MedianOfMedianConvergenceCheckerFactory` creates a checker that computes the median of median absolute gradient values on each data partition. This method is less sensitive for anomalies in the learning dataset, but GDB may converge longer.

Example of training:

{% code title="Java" %}
```java
// Set up trainer
GDBTrainer trainer = new GDBBinaryClassifierOnTreesTrainer(
  learningRate, countOfIterations, new LogLoss()
).withCheckConvergenceStgyFactory(new MedianOfMedianConvergenceCheckFactory(precision));

// Build the model
GDBModel mdl = trainer.fit(
  datasetBuilder,
  featureExtractor,
  labelExtractor
);
```
{% endcode %}

## Example

To see how GDB Classifier can be used in practice, try this [example](https://github.com/apache/ignite-extensions/tree/master/modules/ml-ext/examples/src/main/java/org/apache/ignite/examples/ml/tree/boosting/GDBOnTreesClassificationTrainerExample.java), available on GitHub and delivered with every Apache Ignite distribution.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
