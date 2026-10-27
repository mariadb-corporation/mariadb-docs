---
description: >-
  Use GridGain 8 as an online store for Feast to serve features with high-performance, in-memory storage and retrieval.
---

# Feast Stores

The GridGain Feast integration provides a way of using GridGain as online store for Feast, providing high-performance, in-memory data storage and retrieval for feature serving.

## Features

- **GridGain Integration:** Leverages GridGain's in-memory database to provide online features for real-time model predictions.
- **Feature Management:** Feast manages feature definitions, versioning, and the synchronization between online and offline stores.

## Project Structure

The project consists of two main components:

1. **Ignite Online Store** (`online_store.py`): Sets up Apache Ignite as the online feature store.
2. **GridGain Online Store** (`gridgain_online_store.py`): Configures GridGain as the online feature store.

Both implementations provide similar functionality but are tailored to their respective systems.

## Prerequisites

The following is required to use LangChain integration:

- GridGain 8.9.17 or later with an appropriate license is required to use vector store.
- Python 3.11.7 or later is required to use the LangChain extension.

## Installation

Install the package using pip:

```bash
pip install feast-gridgain
```

## API Reference

### Online Store Reference

Both Apache Ignite and GridGain stores provide the following methods:

- `online_read(config, table, entity_keys, requested_features)` - Reads feature values from the online store.
- `online_write_batch(config, table, data, progress)` - Writes a batch of feature data to the online store.
- `update(config, tables_to_delete, tables_to_keep, entities_to_delete, entities_to_keep, partial)` - Updates the online store based on changes to the feature repository.
- `teardown(config, tables, entities)` - Cleans up the online store.

## Feast Tutorial

GridGain provides a comprehensive example of using Ignite for creating an online store for a Feast integration with Kafka. This tutorial provides a detailed implementation that demonstrates the integration of Ignite Online Store with Feast in a Continuous Glucose Monitoring (CGM) use case. It includes examples of configuration, feature definitions, and usage in different environments.

The full tutorial is available in the [Low-Latency Machine Learning Feature Store with GridGain and Feast](https://www.gridgain.com/docs/tutorials/vector/feast) section.
