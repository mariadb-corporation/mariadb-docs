---
description: >-
  Serve BigQuery ML predictions with sub-millisecond latency by caching them in GridGain 8, using a Google Analytics product recommendation demo as the reference.
---

# How to Cache Machine Learning Predictions With GridGain and BigQuery

## Prerequisites

- A running **GridGain 8** cluster on bare metal or a VM
- Access to [**Google BigQuery**](https://cloud.google.com/bigquery), including a BigQuery ML model whose predictions you want to cache
- **Python** for running the demo project

## Overview

AI-powered predictions need to be delivered in real-time to support operational analytics and user-facing applications. Whether it is product recommendations, risk assessments, or personalized content, users expect immediate responses. Several challenges make this difficult, and prediction caching addresses them by keeping the results of expensive model calls close to the application.

This guide explains what prediction caching is, why GridGain suits the role, and how a Google Analytics product recommendation system uses GridGain as a prediction cache for BigQuery ML models. It references the [demonstration project](https://github.com/GridGain-Demos/prediction_cache_ga), which includes functional sample code and step-by-step instructions for setting up and running the project.

## What is Prediction Caching and why do you Need it?

In today's digital landscape, AI-powered predictions need to be delivered in real-time to support operational analytics and user-facing applications. Whether it is product recommendations, risk assessments, or personalized content, users expect immediate responses. However, several challenges make this difficult.

### Challenges With Online Prediction Access

1. **Slow model execution:**
   - Complex ML models often require significant computation time
   - Multiple feature transformations can add additional latency
   - Resource-intensive preprocessing steps slow down response times
2. **Cost considerations:**
   - Cloud-based ML services charge per prediction
   - High-volume applications can become expensive
   - Redundant predictions waste computational resources

### The Power of Prediction Caching

Prediction caching solves these challenges by:

- **Storing previous results:** Caching predictions for frequently requested inputs
- **Instant retrieval:** Providing sub-millisecond access to cached predictions
- **Cost reduction:** Minimizing expensive model calls

## Why GridGain for Prediction Caching?

GridGain serves as an ideal prediction cache due to its low latency in-memory architecture:

1. **Ultra-low latency:**
   - In-memory storage provides microsecond access times
   - Distributed architecture minimizes network hops
   - Optimized for key-based lookups
   - Local caching reduces latency further
2. **Scalable performance:**
   - Horizontal scaling across commodity hardware
   - Linear performance scaling with added nodes
   - Handles millions of predictions per second
   - Efficient memory utilization
3. **High availability:**
   - Automatic data replication
   - No single point of failure
   - Consistent performance under load

## The Google Analytics Recommendation System: A Real Example

The [demonstration project](https://github.com/GridGain-Demos/prediction_cache_ga) implements a sophisticated product recommendation system that leverages GridGain's capabilities as a prediction cache for BigQuery ML models. This system showcases how GridGain can serve as a high-performance cache for ML predictions in e-commerce applications.

### Under the Hood

1. **Data flow:**
   - Google Analytics data processed in BigQuery
   - Matrix factorization model trained on user-product interactions using BigQuery-ML
   - Predictions exported to GridGain cache
   - Real-time serving through GridGain's in-memory store
2. **Smart caching:**
   - Cache-aside pattern for prediction retrieval
   - Automatic cache population for new predictions
   - Bulk loading support for initial cache warming
3. **Performance:**
   - Sub-millisecond recommendation retrieval
   - Efficient memory utilization
   - Real-time cache updates
4. **Cost optimization:**
   - Reduced BigQuery API calls
   - Minimal model execution overhead

This implementation demonstrates how GridGain's distributed computing capabilities can be leveraged to build a scalable, high-performance prediction cache that provides immediate access to ML model predictions while significantly reducing costs and computational overhead.

## Demonstration Project

A fully functional demo project is available on GitHub in the [Prediction cache demo](https://github.com/GridGain-Demos/prediction_cache_ga) repository. It includes functional sample code, as well as step-by-step instructions on setting up and running the project.

## Related

- [Prediction cache demo](https://github.com/GridGain-Demos/prediction_cache_ga) - The full sample project with setup and run instructions.
- [Google BigQuery](https://cloud.google.com/bigquery) - The data warehouse and BigQuery ML platform used to train and generate predictions.
