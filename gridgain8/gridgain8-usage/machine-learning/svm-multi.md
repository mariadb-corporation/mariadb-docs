---
description: >-
  How the linear SVM multi-class classification algorithm works in GridGain Machine Learning, using a one-versus-all approach.
---

# SVM Multi-class Classification

Multiclass SVM aims to assign labels to instances by using support vector machines, where the labels are drawn from a finite set of several elements.

The implemented approach for doing so is to reduce the single multiclass problem into multiple binary classification problems via one-versus-all.

The one-versus-all approach is the process of building binary classifiers which distinguish between one of the labels and the rest.

## Model

The model keeps the pairs `<ClassLabel, SVMLinearBinaryClassificationModel>` and it enables a prediction to be made for a given vector of features, in the following way:

{% code title="Java" %}
```java
SVMLinearMultiClassClassificationModel model = ...;

double prediction = model.predict(observation);
```
{% endcode %}

## Trainer

Presently, Ignite supports the following parameters for `SVMLinearMultiClassClassificationTrainer`:

- `amountOfIterations` - amount of outer SDCA algorithm iterations. (default value: `200`)
- `amountOfLocIterations` - amount of local SDCA algorithm iterations. (default value: `100`)
- `lambda` - regularization parameter (default value: `0.4`)

All properties will be propagated for each pair one-versus-all `SVMLinearBinaryClassificationTrainer`.

{% code title="Java" %}
```java
// Set up the trainer
SVMLinearMultiClassClassificationTrainer trainer = new SVMLinearMultiClassClassificationTrainer()
  .withAmountOfIterations(AMOUNT_OF_ITERATIONS)
  .withAmountOfLocIterations(AMOUNT_OF_LOC_ITERATIONS)
  .withLambda(LAMBDA);

// Build the model
SVMLinearMultiClassClassificationModel mdl = trainer.fit(
  datasetBuilder,
  featureExtractor,
  labelExtractor
);
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
