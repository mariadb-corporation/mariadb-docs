---
description: >-
  Deploy machine learning models to a GridGain 9 cluster and run inference
  predictions using the GridGain ML engine.
---

# Machine Learning

GridGain 9 can host machine learning models on the cluster and run inference close to your data. The ML engine uses [Deep Java Library (DJL)](https://djl.ai/) as its inference runtime and supports PyTorch, TensorFlow, and ONNX Runtime models.

The pages in this section walk you through a complete example and describe model deployment and prediction options in detail:

- [Get Started With GridGain ML](get-started-with-gridgain-ml.md) — a working example of deploying and using a sentiment analysis model.
- [GridGain ML Model Deployment and Running Predictions](model-deployment-and-predictions.md) — model formats, deployment methods, prediction types, and advanced usage.

{% columns %}
{% column %}
{% content-ref url="get-started-with-gridgain-ml.md" %}
[Get Started with GridGain ML](get-started-with-gridgain-ml.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A complete, working example of deploying and using a sentiment analysis model with the GridGain 9 machine learning engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="model-deployment-and-predictions.md" %}
[Model Deployment and Predictions](model-deployment-and-predictions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy machine learning models to a GridGain 9 cluster and run simple, batch, SQL-based, and colocated predictions, including advanced custom translators and compute jobs.
{% endcolumn %}
{% endcolumns %}
