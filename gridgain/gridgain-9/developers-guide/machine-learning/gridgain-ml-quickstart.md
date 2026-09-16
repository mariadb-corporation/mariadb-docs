---
description: >-
  A complete, working example of deploying and using a sentiment analysis model
  with the GridGain 9 machine learning engine.
---

# Get Started With GridGain ML

This section provides a complete, working example of deploying and using a sentiment analysis model.

## Prerequisites

GridGain ML uses [Deep Java Library (DJL)](https://djl.ai/) as its inference runtime. To keep the GridGain package size small, the ML engine native libraries (PyTorch, TensorFlow, ONNX Runtime) are not bundled with the distribution and are automatically downloaded on the first inference. For air-gapped environments, you must make them available before the node starts, see the options below.

{% hint style="info" %}
ONNX Runtime on Windows requires the Microsoft JDKs or JDKs where MSVC runtime's version above 14.38.33142.0. For more information, see the [GitHub discussion](https://github.com/microsoft/onnxruntime/discussions/23971).
{% endhint %}

### Compatible native library versions

The following native library versions are compatible with the DJL 0.36.0 runtime embedded in GridGain ML:

| Engine | Native version | DJL JNI artifact version |
| --- | --- | --- |
| PyTorch | 2.7.1 | pytorch-jni:2.7.1-0.36.0 |
| TensorFlow | 2.16.1 | n/a (single artifact) |
| ONNX Runtime | 1.17.0 | n/a (single artifact) |

### Option 1 – Use the GridGain ML Docker image (recommended)

The official GridGain ML Docker image ships with all three engine native libraries pre-loaded. Pull and run it directly; no additional setup is required.

```bash
docker pull gridgain/gridgain9:<VERSION>-ml
docker run gridgain/gridgain9:<VERSION>-ml
```

This is the simplest path for both connected and air-gapped environments when you can transfer Docker images.

### Option 2 – Pre-load native libraries before going air-gapped

In environments where internet access is available at setup time but not at runtime, pre-load the engine native libraries once while connected. DJL will cache them locally and reuse the cache on every subsequent start without any network access.

Run the following utility *once* on each node (or on a base image during build) while internet access is still available:

```java
public static void main(String[] args) {
    System.out.println("Available engines: " + Engine.getAllEngines());
    if (Engine.hasEngine("OnnxRuntime")) {
        Engine.getEngine("OnnxRuntime");
        System.out.println("ONNX Runtime loaded");
    }
    if (Engine.hasEngine("PyTorch")) {
        Engine.getEngine("PyTorch");
        System.out.println("PyTorch loaded");
    }
    if (Engine.hasEngine("TensorFlow")) {
        Engine.getEngine("TensorFlow");
        System.out.println("TensorFlow loaded");
    }
}
```

### Option 3 – Install PyTorch or TensorFlow via pip

If your environment already has a Python runtime, you can install the framework libraries via pip and point DJL to them. This avoids any separate download step.

#### PyTorch

Install the version compatible with DJL 0.36.0:

```bash
pip install torch==2.7.1
```

Then set the following environment variables before starting GridGain:

```bash
export PYTORCH_LIBRARY_PATH=/path/to/site-packages/torch/lib
export PYTORCH_VERSION=2.7.1
export PYTORCH_FLAVOR=cpu   # or cu118, cu121, cu128 for GPU
```

DJL will load the native libraries from `PYTORCH_LIBRARY_PATH` instead of downloading them.

#### TensorFlow

```bash
pip install tensorflow==2.16.1
```

No additional environment variables are needed; DJL auto-detects the TensorFlow installation when it is on the library path.

{% hint style="info" %}
GPU builds require CUDA to be installed on the host. See the [DJL PyTorch engine docs](https://docs.djl.ai/master/engines/pytorch/pytorch-engine/index.html) and [TensorFlow engine docs](https://docs.djl.ai/master/engines/tensorflow/tensorflow-engine/index.html) for platform-specific GPU dependency details.
{% endhint %}

## Configuration

Before using GridGain ML, it is recommended to configure the thread pool size in your GridGain configuration file for optimal performance.

### Thread Pool Configuration

Edit your `gridgain-config.conf` file (located at `$GRIDGAIN_HOME/etc/gridgain-config.conf`) and add the following configuration:

```javascript
ml {
    threadPoolSize = 4
}
```

**Parameters:**

- `threadPoolSize`: Number of threads allocated for ML inference operations. Adjust based on your workload and available CPU cores.

{% hint style="info" %}
Restart GridGain after modifying the configuration file for changes to take effect.
{% endhint %}

## Step 1: Download a Pre-trained Model

Download a sentiment analysis model from DJL Model Zoo:

```java
import ai.djl.Application;
import ai.djl.repository.zoo.Criteria;
import ai.djl.repository.zoo.ZooModel;
import ai.djl.modality.Classifications;

public class DownloadModel {
    public static void main(String[] args) {
        try {
            // Create a criteria builder for sentiment analysis
            Criteria<String, Classifications> criteria = Criteria.builder()
                .setTypes(String.class, Classifications.class)
                .optModelUrls("djl://ai.djl.pytorch/distilbert")
                .build();
                
            System.out.println("Loading model...");
            
            // Load the model from DJL model zoo
            ZooModel<String, Classifications> model = criteria.loadModel();
            Path modelPath = model.getModelPath();
            System.out.println("Model loaded from: " + modelPath);
            
            // Create the target directory
            Path targetDir = Paths.get("src/main/resources/models/sentiment");
            Files.createDirectories(targetDir);
            
            // Copy all model files to the target directory
            System.out.println("Copying model files to: " + targetDir);
            copyDirectory(modelPath, targetDir);
            System.out.println("Model downloaded successfully to: " + targetDir);
            
            // Close the model
            model.close();
        } catch (Exception e) {
            System.err.println("Error downloading model: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static void copyDirectory(Path source, Path target) throws IOException {
        Files.createDirectories(target);
        Files.list(source).forEach(path -> {
            try {
                Path targetPath = target.resolve(source.relativize(path));
                if (Files.isDirectory(path)) {
                    copyDirectory(path, targetPath);
                } else {
                    Files.copy(path, targetPath, StandardCopyOption.REPLACE_EXISTING);
                    System.out.println("  Copied: " + targetPath.getFileName());
                }
            } catch (IOException e) {
                throw new RuntimeException("Failed to copy: " + path, e);
            }
        });
    }
}
```

## Step 2: Deploy Model to GridGain

Deploy the downloaded model to all nodes:

```bash
# Deploy the downloaded model to all nodes
cluster unit deploy sentiment-model \
    --version 1.0.0 \
    --path /path/to/model/directory \
    --nodes ALL

# Verify deployment
cluster unit list
```

For more information about code deployment, see the [Code Deployment](../code-deployment/code-deployment.md) article.

## Step 3: Run Your First Prediction

Run the prediction using the downloaded model:

```java
package org.apache.ignite.example.ml;

import org.apache.ignite.client.IgniteClient;
import org.gridgain.ml.IgniteMl;
import org.gridgain.ml.model.*;
import ai.djl.modality.Classifications;

public class QuickStartExample {
    public static void main(String[] args) {
        start(MODE.EMBEDDED);

        // Prepare prediction request
        MlSimpleJobParameters<String> jobParams =
            MlSimpleJobParameters.<String>builder()
                .id("sentiment-model")
                .version("1.0.0")
                .type(ModelType.PYTORCH)
                .name("traced_distilbert_sst_english")
                .inputClass(String.class.getName())
                .outputClass(Classifications.class.getName())
                .property("application",
                    "ai.djl.Application$NLP$SENTIMENT_ANALYSIS")
                .translatorFactory("ai.djl.pytorch.zoo.nlp.sentimentanalysis.PtDistilBertTranslatorFactory")
                .input("This product is absolutely fantastic! Best purchase ever!")
                .build();

        // Run prediction
        Classifications result = ml.predict(jobParams);

        // Display results
        System.out.println("Sentiment Analysis Result:");
        System.out.println("Text: 'This product is absolutely fantastic! Best purchase ever!'");
        System.out.println("Prediction: " + result.best().getClassName());
        System.out.println("Confidence: " + (result.best().getProbability() * 100) + "%");
    }
}
```
