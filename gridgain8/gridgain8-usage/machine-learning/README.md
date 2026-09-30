---
description: >-
  Overview of the GridGain Machine Learning module and the algorithms it provides.
---

# Machine Learning

GridGain Machine Learning is a set of simple, scalable, and efficient tools that let you build predictive machine learning models directly on data stored across the cluster. This section describes the available algorithms, preprocessing tools, and model management capabilities.

{% columns %}
{% column %}
{% content-ref url="ml.md" %}
[Machine Learning](ml.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to GridGain Machine Learning, its zero-ETL and fault-tolerant design, the supported algorithm families, and how to get started.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="preprocessing.md" %}
[Preprocessing](preprocessing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The preprocessing algorithms available in GridGain Machine Learning, including normalization, binarization, imputing, encoders, and scalers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="part-based-dataset.md" %}
[Partition Based Dataset](part-based-dataset.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the partition-based dataset abstraction underpins GridGain Machine Learning algorithms with zero-ETL, fault-tolerant, MapReduce-style computation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="line-reg.md" %}
[Linear Regression](line-reg.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the ordinary least squares Linear Regression algorithm works in GridGain Machine Learning, with the LSQR and SGD trainers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="k-means.md" %}
[K-Means Clustering](k-means.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the K-Means clustering algorithm works in GridGain Machine Learning, including the model and trainer parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="genetic-alg.md" %}
[Genetic Algorithms](genetic-alg.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to solve optimization problems with Genetic Algorithms in GridGain Machine Learning, with a HelloWorld example and Apache Zeppelin integration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ml-percep.md" %}
[Multilayer Perceptron](ml-percep.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the Multilayer Perceptron (MLP) neural network works in GridGain Machine Learning, including the model and distributed batch training.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="decision-trees.md" %}
[Decision Trees](decision-trees.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How decision tree classification and regression work in GridGain Machine Learning, including the model, trainers, and examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="knn-class.md" %}
[k-NN Classification](knn-class.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the k-NN (k-nearest neighbors) classification algorithm works in GridGain Machine Learning, including its parameters and an example.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="knn-reg.md" %}
[k-NN Regression](knn-reg.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the k-NN (k-nearest neighbors) regression algorithm works in GridGain Machine Learning, including its parameters and an example.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="svm-binary.md" %}
[SVM Binary Classification](svm-binary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the linear SVM binary classification algorithm works in GridGain Machine Learning, including the model and trainer parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="svm-multi.md" %}
[SVM Multi-class Classification](svm-multi.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the linear SVM multi-class classification algorithm works in GridGain Machine Learning, using a one-versus-all approach.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="model-cross.md" %}
[Model Cross Validation](model-cross.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How model cross validation works in GridGain Machine Learning, using the CrossValidation class and k-fold validation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="log-reg.md" %}
[Logistic Regression](log-reg.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How binary and multi-class Logistic Regression work in GridGain Machine Learning, including the model, its parameters, and the trainer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="random-forest.md" %}
[Random Forest](random-forest.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the Random Forest ensemble algorithm works in GridGain Machine Learning, including aggregators, the model, and trainer parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="grad-boost.md" %}
[Gradient Boosting](grad-boost.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How gradient boosting (GDB) works in GridGain Machine Learning, including the model, trainer parameters, and convergence checkers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ann.md" %}
[ANN (Approximate Nearest Neighbor)](ann.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the Approximate Nearest Neighbor (ANN) classification algorithm works in GridGain Machine Learning, including its model and trainer parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="model-updating.md" %}
[Model Updating](model-updating.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How online and batch online model updating works per algorithm in GridGain Machine Learning, using an already trained model as a starting point.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="model-importing.md" %}
[Model Importing](model-importing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to import pre-trained Machine Learning models from Apache Spark ML and XGBoost into GridGain for distributed inference.
{% endcolumn %}
{% endcolumns %}
