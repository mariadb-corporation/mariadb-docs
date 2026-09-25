---
hidden: true
description: >-
  How to use the GridGain ML Python API (ggml) for regression, classification, clustering, preprocessing, model selection, inference, and storage.
---

# Using Python ML

## Cache API

With the GridGain ML Python API you can load data into a cache using an `int` as a key and a `NumPy array` as a value.

{% code title="Python" %}
```python
with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)
```
{% endcode %}

## Regression

Modeling the relationship between a scalar dependent variable y and one or more explanatory variables (or independent variables) denoted x.

Applicability: drug response, stock prices, supermarket revenue.

## Linear Regression

GridGain supports the ordinary least squares Linear Regression algorithm — one of the most basic and powerful machine learning algorithms.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.regression import LinearRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_regression
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import rmse_score
from ggml.regression import LinearRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = LinearRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))
```
{% endcode %}

## Decision Tree Regression

Decision trees are a simple yet powerful model in supervised machine learning. The main idea is to split a feature space into regions so that the value in each region varies slightly. The measure of the values’ variation in a region is called the impurity of the region.

GridGain provides an implementation of the algorithm optimized for data stored in rows.

Splits are performed recursively and every region created from a split can be split further. Therefore, the whole process can be described by a binary tree, where each node is a particular region and its children are the regions derived from it by another split.

The split process stops when either the algorithm has reached the configured maximal depth, or splitting of any region has not resulted in significant impurity loss. Prediction of a value for point s from S is a traversal of the tree down to the node that corresponds to the region containing s and getting back a value associated with this leaf.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.regression import DecisionTreeRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_regression
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import rmse_score
from ggml.regression import DecisionTreeRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = DecisionTreeRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))
```
{% endcode %}

## KNN Regression

The GridGain Machine Learning component provides two versions of the widely used k-NN (k-nearest neighbors) algorithm: one for classification tasks and the other for regression tasks.

The k-NN algorithm is a non-parametric method whose input consists of the k-closest training examples in the feature space. Each training example has a property value in a numerical form associated with the given training example.

The k-NN algorithm uses all training sets to predict a property value for the given test sample. This predicted property value is an average of the values of its k nearest neighbors. If k is 1, then the test sample is simply assigned to the property value of a single nearest neighbor.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.regression import KNNRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = KNNRegressionTrainer()
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_regression
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import rmse_score
from ggml.regression import KNNRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = KNNRegressionTrainer()
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))
```
{% endcode %}

## Random Forest Regression

Random forest is an ensemble learning method used to solve any classification and regression problem. Random forest training builds a model composition (ensemble) of one type using some of the aggregation algorithms from several models. Each model is trained on a part of the training dataset. The part is defined according to bagging and feature subspace methods.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.regression import RandomForestRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = RandomForestRegressionTrainer(features=100)
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_regression
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import rmse_score
from ggml.regression import RandomForestRegressionTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_regression())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = RandomForestRegressionTrainer(features=100)
    model = trainer.fit(train_cache)
    print(rmse_score(test_cache, model))
```
{% endcode %}

## MLP Regression

Multiplayer Perceptron (MLP) is the basic form of neural network. It consists of one input layer and 0 or more transformation layers. Each transformation layer has associated weights, activator, and optionally biases. The set of all weights and biases of MLP is the set of MLP parameters.

One of the popular methods of supervised model training is batch training. In this approach, training is done in iterations; during each iteration we extract a subpart (batch) of labeled data (data consisting of input of approximated function and corresponding values of this function which are often called "ground truth") on which we train and update model parameters using this subpart. Updates are made to minimize loss function on batches.

GridGain MLPTrainer is used for distributed batch training, which works in a way similar to map-reduce. Iterations are performed per node resulting in a distributed gradient. Each global iteration consists of several parallel iterations which in turn consist of several local steps. Each local iteration is executed by its own worker and performs the specified number of local steps (called the synchronization period) on a subset of the local data to compute its update of model parameters. Then all of the updates are accumulated on the node that started training, and are transformed to a global update which is sent back to all workers. This process continues until stop criteria is reached.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.regression import MLPArchitecture
from ggml.regression import MLPRegressionTrainer

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = MLPRegressionTrainer(MLPArchitecture(input_size=100).with_layer(neurons=1, activator='linear'))
model = trainer.fit(x_train, y_train)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

## Classification

Identifying to which category a new observation belongs, on the basis of a training set of data.

Applicability: spam detection, image recognition, credit scoring, disease identification.

## Decision Tree Classification

Decision trees are a simple yet powerful model in supervised machine learning. The main idea is to split a feature space into regions such as that the value in each region varies a little. The measure of the values’ variation in a region is called the impurity of the region.

GridGain provides an implementation of the algorithm optimized for data stored in rows.

Splits are done recursively and every region created from a split can be split further. Therefore, the whole process can be described by a binary tree, where each node is a particular region and its children are the regions derived from it by another split.

The split process stops when either the algorithm has reached the configured maximal depth, or splitting of any region has not resulted in significant impurity loss. Prediction of a value for point s from S is a traversal of the tree down to the node that corresponds to the region containing s and getting back a value associated with this leaf.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import DecisionTreeClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import DecisionTreeClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = DecisionTreeClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## ANN Classification

ANN Classification is an ANN algorithm trainer used to solve multi-class classification tasks. This trainer is based on the ACD strategy and KMeans clustering algorithm to find centroids.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import ANNClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = ANNClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import ANNClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = ANNClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## KNN Classification

The GridGain Machine Learning component provides two versions of the widely used k-NN (k-nearest neighbors) algorithm: one for classification tasks and the other for regression tasks.

The k-NN algorithm is a non-parametric method whose input consists of the k-closest training examples in the feature space. Each training example has a property value in a numerical form associated with the given training example.

The k-NN algorithm uses all training sets to predict a property value for the given test sample. This predicted property value is an average of the values of its k nearest neighbors. If k is 1, then the test sample is simply assigned to the property value of a single nearest neighbor.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import KNNClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = KNNClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import KNNClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = KNNClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## LogReg Classification

Binary Logistic Regression is a special type of regression where a binary response variable is related to a set of explanatory variables, which can be discrete and/or continuous. The important point to note here is that in linear regression, the expected values of the response variable are modeled based on a combination of values taken by the predictors. In logistic regression, the Probability or Odds of the response taking a particular value is modeled based on the combination of values taken by the predictors. In the GridGain ML module it is implemented via `LogisticRegressionModel`, which solves the binary classification problem.

For binary classification problems, the algorithm outputs a binary logistic regression model.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import LogRegClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LogRegClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import LogRegClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = LogRegClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## SVM Classification

Support Vector Machines (SVMs) are supervised learning models with associated learning algorithms that analyze data used for classification and regression analysis.

Given a set of training examples, each marked as belonging to one or the other of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-probabilistic binary linear classifier.

Only Linear SVM is supported in the GridGain Machine Learning module.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import SVMClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = SVMClassificationTrainer()
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import SVMClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = SVMClassificationTrainer()
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## Random Forest Classification

Random forest is an ensemble learning method used to solve any classification and regression problem. Random forest training builds a model composition (ensemble) of one type using some of the aggregation algorithms from several models. Each model is trained on a part of the training dataset. The part is defined according to bagging and feature subspace methods.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.classification import RandomForestClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = RandomForestClassificationTrainer(features=20)
model = trainer.fit(x_train, y_train)

accuracy_score(y_test, model.predict(x_test))
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split
from ggml.metrics import accuracy_score
from ggml.classification import RandomForestClassificationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    trainer = RandomForestClassificationTrainer(features=20)
    model = trainer.fit(train_cache)
    print(accuracy_score(test_cache, model))
```
{% endcode %}

## MLP Classification

Multiplayer Perceptron (MLP) is the basic form of neural network. It consists of one input layer and 0 or more transformation layers. Each transformation layer has associated weights, activator, and optionally biases. The set of all weights and biases of MLP is the set of MLP parameters.

One of the popular methods of supervised model training is batch training. In this approach, training is done in iterations; during each iteration we extract a subpart (batch) of labeled data (data consisting of input of approximated function and corresponding values of this function which are often called ‘ground truth’) on which we train and update model parameters using this subpart. Updates are made to minimize loss function on batches.

GridGain MLPTrainer is used for distributed batch training, which works in a map-reduce way. Each iteration (let’s call it global iteration) consists of several parallel iterations which in turn consist of several local steps. Each local iteration is executed by its own worker and performs the specified number of local steps (called synchronization period) to compute its update of model parameters. Then all updates are accumulated on the node that started training, and are transformed to global update which is sent back to all workers. This process continues until the stop criteria is reached.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ggml.regression import MLPArchitecture
from ggml.regression import MLPRegressionTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

def encode_label(x):
    if x:
        return [0, 1]
    else:
        return [1, 0]

def decode_label(x):
    if x[0] > x[1]:
        return 0
    else:
        return 1

trainer = MLPRegressionTrainer(MLPArchitecture(input_size=20).with_layer(neurons=2, activator='sigmoid'))
model = trainer.fit(x_train, [encode_label(x) for x in y_train])

accuracy_score(y_test, [decode_label(x) for x in model.predict(x_test)])
```
{% endcode %}

## Clustering

Grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters).

Applicability: customer segmentation, grouping experiment outcomes, grouping of shopping items.

## KMeans Clustering

The GridGain Machine Learning component provides a K-Means clustering algorithm implementation. K-Means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.

The model holds a vector of k centers and one of the distance metrics provided by the ML framework such as Euclidean, Hamming, or Manhattan.

KMeans is a unsupervised learning algorithm. It solves the clustering task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters).

KMeans is a parametrized iterative algorithm which calculates the new means to be the centroids of the observations in the clusters on each iteration.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_blobs
from ggml.clustering import KMeansClusteringTrainer

x, y = make_blobs(
    n_samples=2000,
    n_features=2,
    cluster_std=1.0,
    centers=[(-3, -3), (0, 0), (3, 3)]
)

trainer = KMeansClusteringTrainer(amount_of_clusters=3)
model = trainer.fit(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_blobs
from ggml.core import Ignite
from ggml.clustering import KMeansClusteringTrainer

with Ignite("example-ignite.xml") as ignite:
    x, y = make_blobs(
        n_samples=2000,
        n_features=2,
        cluster_std=1.0,
        centers=[(-3, -3), (0, 0), (3, 3)]
    )
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack((x, y))):
        cache.put(i, row)

    trainer = KMeansClusteringTrainer(amount_of_clusters=3)
    model = trainer.fit(x)
```
{% endcode %}

## GMM Clustering

A Gaussian mixture model is a probabilistic model that assumes all the data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters.

This algorithm represents a soft clustering model where each cluster is a Gaussian distribution
with its own mean value and covariation matrix. Such a model can predict a cluster using the maximum likelihood principle.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_blobs
from ggml.clustering import GMMClusteringTrainer

x, y = make_blobs(
    n_samples=2000,
    n_features=2,
    cluster_std=1.0,
    centers=[(-3, -3), (0, 0), (3, 3)]
)

trainer = GMMClusteringTrainer(
    count_of_components=3,
    max_count_of_clusters=3
)
model = trainer.fit(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_blobs
from ggml.core import Ignite
from ggml.clustering import GMMClusteringTrainer

with Ignite("example-ignite.xml") as ignite:
    x, y = make_blobs(
        n_samples=2000,
        n_features=2,
        cluster_std=1.0,
        centers=[(-3, -3), (0, 0), (3, 3)]
    )
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack((x, y))):
        cache.put(i, row)

    trainer = GMMClusteringTrainer(
        count_of_components=3,
        max_count_of_clusters=3
    )
    model = trainer.fit(x)
```
{% endcode %}

## Preprocessing

Preprocessing is required to transform raw data stored in an Ignite cache to the dataset of feature vectors suitable for further use in a machine learning pipeline.

This section covers algorithms for working with features, roughly divided into the following groups:

- Extracting features from “raw” data
- Scaling features
- Converting features
- Modifying features

{% hint style="info" %}
Usually preprocessing starts with label and feature extraction from raw data. It can be combined with other preprocessing stages.
{% endhint %}

## Normalization Preprocessing

The usual flow is to extract features from Ignite, transform the features, and then normalize them.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import NormalizationTrainer

x, y = make_classification()
normalizer = NormalizationTrainer().fit(x)
normalizer.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import NormalizationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)
    normalizer = NormalizationTrainer().fit(cache)
    cache_transformed = cache.transform(normalizer)
    head = cache_transformed.head()
head
```
{% endcode %}

## Binarization Preprocessing

Binarization is the process of thresholding numerical features to binary (0/1) features. Feature values greater than the threshold are binarized to 1.0; values equal to or less than the threshold are binarized to 0.0.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import BinarizationTrainer

x, y = make_classification()
binarizer = BinarizationTrainer(threshold=0.5).fit([[]])
binarizer.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import BinarizationTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)
    binarizer = BinarizationTrainer().fit(cache)
    cache_transformed = cache.transform(binarizer)
    head = cache_transformed.head()
head
```
{% endcode %}

## Imputing Preprocessing

The Imputer preprocessor completes missing values in a dataset, either using the mean or another statistic of the column in which the missing values are located. The missing values should be presented as Double.NaN. The input dataset column should be of type Double. Currently, the Imputer preprocessor does not support categorical features and may possibly create incorrect values for columns containing categorical features.

During the training phase, the Imputer Trainer collects statistics about the preprocessing dataset. In the preprocessing phase it changes the data according to the collected statistics.

The Imputer Trainer contains only one parameter: `imputingStgy` that is presented as enum `ImputingStrategy` with two available values (NOTE: future releases may support more values):

- MEAN: The default strategy. If this strategy is chosen, then replace missing values using the mean for the numeric features along the axis.
- MOST_FREQUENT: If this strategy is chosen, then replace missing values using the most frequent value along the axis.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import ImputerTrainer

x = [[None, 1, 1], [2, None, 2]]
imputer = ImputerTrainer().fit(x)
imputer.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import ImputerTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate([[None, 1, 1, 0], [2, None, 2, 0]]):
        cache.put(i, row)
    imputer = ImputerTrainer().fit(cache)
    cache_transformed = cache.transform(imputer)
    head = cache_transformed.head()
head
```
{% endcode %}

## One-Hot-Encoding Preprocessing

One-hot encoding maps a categorical feature, represented as a label index (Double or String value), to a binary vector with at most a single one-value indicating the presence of a specific feature value from among the set of all feature values.

This preprocessor can transform multiple columns in which indices are handled during the training process. These indexes could be defined via the `encoded_features` parameter.

{% hint style="info" %}
- Each one-hot encoded binary vector adds its cells to the end of the current feature vector.
- This preprocessor always creates a separate column for NULL values.
- The index value associated with NULL will be located in a binary vector according to the frequency of NULL values.
{% endhint %}

`StringEncoderPreprocessor` and `OneHotEncoderPreprocessor` use the same `EncoderTraining` to collect data about categorical features during the training phase.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import EncoderTrainer

x = [[1, 2, 0], [2, 1, 0]]
encoder = EncoderTrainer(encoded_features=[0, 1]).fit(x)
encoder.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import EncoderTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate([[1, 2, 0], [2, 1, 0]]):
        cache.put(i, row)
    encoder = EncoderTrainer(encoded_features=[0, 1]).fit(cache)
    cache_transformed = cache.transform(encoder)
    head = cache_transformed.head()
head
```
{% endcode %}

## MinMax Scaling Preprocessing

The MinMax Scaler transforms the given dataset, rescaling each feature to a specific range. `MinMaxScalerTrainer` computes summary statistics on a data set and produces a `MinMaxScalerPreprocessor`. The preprocessor can then transform each feature individually such that it is in the given range.

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import MinMaxScalerTrainer

x, y = make_classification()
scaler = MinMaxScalerTrainer().fit(x)
scaler.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import MinMaxScalerTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)
    scaler = MinMaxScalerTrainer().fit(cache)
    cache_transformed = cache.transform(scaler)
    head = cache_transformed.head()
head
```
{% endcode %}

## MaxAbs Scaling Preprocessing

The MaxAbs Scaler transforms the given dataset, rescaling each feature to the range [-1, 1] by dividing through the maximum absolute value in each feature. `MaxAbsScalerTrainer` computes summary statistics on a data set and produces a `MaxAbsScalerPreprocessor`. To see how the `MaxAbsScalerPreprocessor` can be used in practice, try this tutorial example:

With local data:

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from ggml.preprocessing import MaxAbsScalerTrainer

x, y = make_classification()
scaler = MaxAbsScalerTrainer().fit(x)
scaler.transform(x)
```
{% endcode %}

With data stored in distributed cache:

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.preprocessing import MaxAbsScalerTrainer

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)
    scaler = MaxAbsScalerTrainer().fit(cache)
    cache_transformed = cache.transform(scaler)
    head = cache_transformed.head()
head
```
{% endcode %}

## Model Selection

Model selection is a set of tools that provides the ability to prepare and test models efficiently. Use it to split data based on training and test data as well as perform cross validation.

## Test/Train Splitting

Data splitting that splits data stored in cache into two parts: the training part that should be used to train the model, and the test part that should be used to estimate model quality.

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.model_selection import train_test_split

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache")
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    train_cache, test_cache = train_test_split(cache)

    dataset_1 = test_cache.head()
    dataset_2 = train_cache.head()
```
{% endcode %}

## Cross Validation

Cross validation functionality in GridGain is represented by the `CrossValidation` class. This is a calculator that uses the following parameters: the type of model, type of label, and key-value types of data. After instantiation (the constructor does not accept any additional parameters) we can use a score method to perform cross validation.

Let’s imagine that we have a trainer and a training set, and we want to perform cross validation using accuracy as a metric and using 4 folds.

{% code title="Python" %}
```python
import numpy as np
from sklearn.datasets import make_classification
from ggml.core import Ignite
from ggml.classification import DecisionTreeClassificationTrainer
from ggml.model_selection import cross_val_score

with Ignite("example-ignite.xml") as ignite:
    cache = ignite.create_cache("my-cache", parts=1)
    for i, row in enumerate(np.column_stack(make_classification())):
        cache.put(i, row)

    trainer = DecisionTreeClassificationTrainer()
    score = cross_val_score(trainer, cache)
score
```
{% endcode %}

## Inference

GridGain ML provides the ability to distribute inference workload within a cluster. This means that inference is performed not on a single node, but on several nodes within a cluster and so that makes it linearly scalable.

## Distributed Inference

{% code title="Python" %}
```python
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from ggml.core import Ignite
from ggml.inference import IgniteDistributedModel
from ggml.classification import DecisionTreeClassificationTrainer

x, y = make_classification()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = DecisionTreeClassificationTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite.xml") as ignite:
    with IgniteDistributedModel(ignite, model) as ignite_distr_mdl:
        print(accuracy_score(
            y_test,
            ignite_distr_mdl.predict(x_test)
        ))
```
{% endcode %}

## Model Storage

GridGain ML provides the ability to save and read models. Models can be saved using the local file system or using IGFS (distributed file system supplied as part of GridGain).

Using local file system:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.core import Ignite
from ggml.regression import LinearRegressionTrainer
from ggml.storage import save_model
from ggml.storage import read_model

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite.xml") as ignite:
    save_model(model, 'test.mdl', ignite)
    model = read_model('test.mdl', ignite)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

Using IGFS file system:

{% code title="Python" %}
```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from ggml.core import Ignite
from ggml.regression import LinearRegressionTrainer
from ggml.storage import save_model
from ggml.storage import read_model

x, y = make_regression()
x_train, x_test, y_train, y_test = train_test_split(x, y)

trainer = LinearRegressionTrainer()
model = trainer.fit(x_train, y_train)

with Ignite("example-ignite-ml.xml") as ignite:
    save_model(model, 'igfs:///test.mdl', ignite)
    model = read_model('igfs:///test.mdl', ignite)

r2_score(y_test, model.predict(x_test))
```
{% endcode %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
