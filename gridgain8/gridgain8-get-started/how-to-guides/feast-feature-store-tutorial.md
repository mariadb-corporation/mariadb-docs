---
description: >-
  Use GridGain 8 as a low-latency Feast online store for real-time machine learning feature serving, illustrated with a CGM glucose-prediction demo.
---

# How to Build a Machine Learning Feature Store With GridGain and Feast

<!-- TODO (not tested): This AI integration page depends on a third-party tool and was not run against GridGain 8.10. Run it with an 8.10 build and the current tool version, compare the steps and output, fix differences, then delete this comment. -->

## Prerequisites

- A running **GridGain 8** cluster on bare metal or a VM
- [**Feast**](https://feast.dev/), the feature store platform used to store, manage, and serve features
- **Python**, to run the feature engineering and serving code

## Overview

Features are individual measurable properties used as input for machine learning models. Feature engineering and extraction is the process of transforming raw data into formats that best represent the underlying problem to the predictive models. For example, in a CGM (Continuous Glucose Monitoring) system, features might include current glucose levels, time of day, day of week, and historical glucose levels.

Feature serving is the process of making these engineered features available for both training and inference.

[Feast](https://feast.dev/) is a platform that combines feature management capabilities with storage backend integrations. It serves as a centralized repository for storing, managing, and serving features to machine learning models.

This guide explains how GridGain works as a low-latency online feature store for Feast, using a real CGM glucose-prediction system as the example.

### Online vs Offline Feature Stores

Feature stores typically operate in two modes:

1. Offline feature store:
   - Stores historical feature values used for model training
   - Optimized for batch processing
   - Usually implemented using data warehouses or data lakes
2. Online feature store:
   - Serves features in real-time for model inference
   - Requires extremely low latency (milliseconds)
   - Usually implemented using in-memory databases

## Why GridGain for an Online Feature Store?

GridGain serves as an ideal online feature store due to its distributed in-memory architecture:

1. Low-latency access:
   - In-memory data storage provides sub-millisecond access times
   - Critical for real-time feature serving in production environments
   - Enables immediate feature updates and retrieval
2. Horizontal scalability:
   - Distributed architecture allows seamless scaling across clusters
   - Handles growing feature sets and increasing request volumes
   - Maintains performance as demand increases
3. High availability:
   - Built-in data replication ensures fault tolerance
   - Automatic failover capabilities
   - No single point of failure

## The CGM Prediction System: A Real Example

The [demonstration project](https://github.com/GridGain-Demos/ignite_feast_cgm_demo) implements a sophisticated CGM (Continuous Glucose Monitoring) prediction system that leverages GridGain's capabilities as a Feast online store. This system showcases how GridGain can serve as a high-performance backend for real-time feature serving in healthcare applications.

### Glucose Prediction Model

The system includes a pre-trained model (`glucose_prediction_model-v1`) that predicts future glucose levels based on historical data and current readings. Key aspects of the model include:

- Personalized predictions: The model takes into account individual subject data to provide personalized glucose predictions
- Time-based features: Incorporates temporal features like day of the week and time of day to capture daily and weekly patterns
- Historical context: Uses historical glucose readings to understand trends and patterns
- Real-time updates: Continuously updates predictions as new CGM readings arrive

### Under the Hood

1. Data organization
   - Raw CGM readings are fetched by the Kafka producer and stored in Kafka for real-time processing
   - Historical data maintained in offline store (Parquet or Snowflake)
   - Real-time features served from GridGain online store
   - Custom feature transformations for time-based aggregations
2. Feature engineering
   - Time-based feature extraction (hour of day, day of week)
   - Event-based feature generation from CGM data streams
3. Performance
   - Sub-millisecond feature retrieval times
   - Real-time feature updates from streaming data
4. Model integration
   - Seamless integration with pre-trained glucose prediction model
   - Real-time feature serving for immediate predictions

This implementation demonstrates how GridGain's distributed computing capabilities can be leveraged to build a scalable, high-performance feature store that provides accurate and timely features for glucose prediction while maintaining low latency and high availability.

## Demonstration Project

A fully functional demo project is available on GitHub in the [Feast demo](https://github.com/GridGain-Demos/ignite_feast_cgm_demo) repository. It includes functional sample code, as well as step-by-step instructions on setting up and running the project.

## Related

- [Feast](https://feast.dev/) - The feature store platform used for storing, managing, and serving features.
- [GridGain Feast CGM demo](https://github.com/GridGain-Demos/ignite_feast_cgm_demo) - The demonstration project with sample code and setup instructions.
