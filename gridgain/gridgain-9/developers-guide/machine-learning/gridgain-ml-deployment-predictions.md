---
description: >-
  Deploy machine learning models to a GridGain 9 cluster and run simple, batch,
  SQL-based, and colocated predictions, including advanced custom translators
  and compute jobs.
---

# GridGain ML Model Deployment and Running Predictions

{% hint style="info" %}
Before deploying models, ensure you have configured GridGain ML thread pool settings. See the [Thread Pool Configuration](gridgain-ml-quickstart.md#thread-pool-configuration) section in the quickstart guide.
{% endhint %}

## Model Deployment

### Preparing the Model

You can use models from the following sources:

- Pretrained models from DJL Model Zoo.
- Locally trained models.
- Pre-trained models in supported formats with correct model names.

#### DJL Model Zoo

DJL Model Zoo models come in supported formats pre-configured with serving.properties that have the modelName preconfigured. You can download them easily using a program like the one in the quickstart guide.

#### Other Sources

The system automatically searches for model files named `model.*` (e.g., `model.onnx`, `model.pt`). You can override this default behavior by adding `.name("your-model-name")` to your job parameters.

### Supported Model Formats

| Framework | Supported Formats | Required Files |
| --- | --- | --- |
| PyTorch | .pt | Model file + configuration files. |
| TensorFlow | .pb | Model file + configuration files. |
| ONNX | .onnx | Model file + configuration files. |

### Unsupported Formats

- **SafeTensors (.safetensors)**: Not supported by DJL. Must convert to PyTorch format.
- **Pytorch Pickled (.pth)**: Not supported by DJL. Must convert to TorchScript (.pt) format.
- **Pickle files (.pkl)**: Raw pickle files need proper model wrapper.

### Deploying the Model

Models are deployed as deployment units using the CLI or REST:

```bash
# Deploy model to cluster
cluster unit deploy sentiment-model \
    --version 1.0.0 \
    --path /path/to/model/directory \
    --nodes ALL
```

For more information refer to [code deployment](../code-deployment/code-deployment.md) documentation.

### Automated Deployment

GridGain ML provides utility methods to automate model download and deployment for different scenarios.

#### Standard Models with Custom Classes

For models with custom input/output types, translators, or marshallers:

```java
List<String> urls = Arrays.asList(
    "https://huggingface.co/model-repo/resolve/main/model.onnx",
    "https://huggingface.co/model-repo/resolve/main/tokenizer.json"
);

Path tempModelDir = ModelUtils.downloadAndDeployModelAndJar(
    urls,                // URLs to download model files from
    "model-id",         // Model identifier
    "1.0.0",            // Model version
    sourceDir           // Path to custom classes for JAR packaging
);
```

This method automatically:

- Downloads all required model files from the specified URLs
- Creates a temporary directory for the model files
- Packages custom classes (translators, marshallers) into a JAR
- Deploys both the model and custom classes to the GridGain cluster

#### DJL Model Zoo Models

For models from the DJL Model Zoo using `djl://` protocol:

```java
String modelUrl = "djl://ai.djl.huggingface.pytorch/deepset/minilm-uncased-squad2";

Path tempModelDir = ModelUtils.downloadAndDeployDJLModelAndJar(
    modelUrl,                           // DJL model URL
    PytorchQAInput.class,              // Input type class
    String.class,                       // Output type class
    "pytorch-qa-model",                // Model identifier
    "1.0.0",                           // Model version
    sourceDir,                          // Path to custom classes
    PytorchQATranslatorFactory.class.getName() // Translator factory
);
```

This method automatically:

- Downloads the PyTorch model from DJL model zoo
- Compiles custom classes from the source directory
- Generates a JAR containing the custom compiled classes
- Deploys both the model files and custom classes JAR to the GridGain cluster

#### TensorFlow Models with Folder Structure

For TensorFlow SavedModel format that requires specific folder structure:

```java
List<String> urls = Arrays.asList(
    "https://huggingface.co/model-repo/resolve/main/saved_model.pb",
    "https://huggingface.co/model-repo/resolve/main/variables/variables.data-00000-of-00001",
    "https://huggingface.co/model-repo/resolve/main/variables/variables.index"
);

Path tempModelDir = ModelUtils.downloadAndDeployModelAndJarWithFolderStructure(
    urls,                // URLs to download model files from
    "tf-model-id",      // Model identifier
    "1.0.0",            // Model version
    sourceDir           // Path to custom classes for JAR packaging
);
```

This method automatically:

- Downloads all required TensorFlow model files
- Creates the proper folder structure (`saved_model.pb` in root, variables in `variables/` subdirectory)
- Packages custom classes into a JAR
- Deploys both the model and custom classes to the GridGain cluster

{% hint style="info" %}
The `downloadAndDeployModelAndJarWithFolderStructure` method is specifically designed to handle TensorFlow's folder structure requirements.
{% endhint %}

## Model Properties Reference

### Core Properties

Some examples of common model properties that could optionally be used in job parameters:

```java
.property("application", "ai.djl.Application$NLP$SENTIMENT_ANALYSIS")
```

{% hint style="info" %}
In case your model requires additional properties, the below attributes could be defined.
{% endhint %}

| Property | Description |
| --- | --- |
| application | DJL application type |
| groupId | Model zoo group ID |
| artifactId | Model zoo artifact ID |

{% hint style="info" %}
Either translator or translator factory must be provided.
{% endhint %}

### Translator Arguments

Properties without the `option.` prefixes are passed to the TranslatorFactory.

1. For built-in translators you will need to check their source code.
2. For custom translators, you can pass ANY properties (without the `option.` prefix) and they will be available in your TranslatorFactory's `newInstance()` method via the arguments' parameter.

### Engine Options

Properties that do not match the [Core Properties](#core-properties) and do not have the `option.` prefix are passed as engine options.

Examples:

- `option.mapLocation` - (PyTorch) Map to CPU before loading.
- `option.ortDevice` - (ONNX) Device selection.
- `option.Tags` - (TensorFlow) Model tags.

## Running Predictions

### Simple Predictions

Execute inference with a single input.

```java
String input = "This movie is absolutely fantastic! I loved every minute of it.";

// Create job parameters
MlSimpleJobParameters<String> jobParams =
    MlSimpleJobParameters.<String>builder()
        .id("sentiment-model")
        .version("1.0.0")
        .type(ModelType.PYTORCH)
        .name("traced_distilbert_sst_english")
        .config(ModelConfig.builder().build())
        .inputClass(String.class.getName())
        .outputClass(Classifications.class.getName())
        .translatorFactory("ai.djl.pytorch.zoo.nlp.sentimentanalysis.PtDistilBertTranslatorFactory")
        .input(input)
        .build();

// Execute prediction
Classifications result = ml.predict(jobParams);
System.out.println("Prediction: " + result.best().getClassName() +
    " (confidence: " + result.best().getProbability() + ")");
```

### Batch Predictions

Execute inference on multiple inputs in a batch.

```java
List<String> batchInputs = Arrays.asList(
        "This movie is very good",
        "This book is not good",
        "This food is very good",
        "This game is not good",
        "This song is very good",
        "This show is very good",
        "This app is very good"
);

try {
    // Create job parameters for batch prediction
    MlBatchJobParameters<String> jobParams = MlBatchJobParameters.<String>builder()
            .id(MODEL_ID)
            .version(MODEL_VERSION)
            .type(ModelType.PYTORCH)
            .name("traced_distilbert_sst_english")
            .inputClass(String.class.getName())
            .outputClass(Classifications.class.getName())
            .translatorFactory(TRANSLATOR_FACTORY)
            .batchInput(batchInputs)
            .build();

    long startTime = System.currentTimeMillis();

    List<Classifications> results = mlApi.batchPredict(jobParams);
    long duration = System.currentTimeMillis() - startTime;

    System.out.println("  Batch Results (" + results.size() + " items):");
    for (int i = 0; i < results.size(); i++) {
        Classifications classification = results.get(i);
        Classification best = classification.best();
        System.out.printf("   %d. \"%s\" → %s (%.2f%%)\n",
                i + 1,
                batchInputs.get(i),
                best.getClassName(),
                best.getProbability() * 100);
    }

    System.out.println("Total processing time: " + duration + "ms");
    System.out.println("Average per item: " + (duration / batchInputs.size()) + "ms");
} catch (Throwable e) {
    System.err.println("Error in batch API prediction");
    throw e;
}
```

### SQL-Based Predictions

Execute inference using SQL queries on database tables:

```java
String sqlQuery = "SELECT review FROM PRODUCT_REVIEWS";
try {
    // Create job parameters for SQL prediction
    MlSqlJobParameters jobParams = MlSqlJobParameters.builder()
            .id(MODEL_ID)
            .version(MODEL_VERSION)
            .type(ModelType.PYTORCH)
            .name("traced_distilbert_sst_english")
            .inputClass(String.class.getName())
            .outputClass(Classifications.class.getName())
            .translatorFactory(TRANSLATOR_FACTORY)
            .sqlQuery(sqlQuery)
            .inputColumn("review")
            .build();

    long startTime = System.currentTimeMillis();

    List<Classifications> results = mlApi.predictFromSql(jobParams);

    long duration = System.currentTimeMillis() - startTime;

    System.out.println(" SQL ML Results (" + results.size() + " items):");
    for (int i = 0; i < results.size(); i++) {
        Classifications classification = results.get(i);
        Classification best = classification.best();
        System.out.printf("   %d → %s (%.2f%%)\n",
                i + 1,
                best.getClassName(),
                best.getProbability() * 100);
    }

    System.out.println("Total processing time: " + duration + "ms");
    System.out.println("Average per item: " + (duration / results.size()) + "ms");
} catch (Throwable e) {
    System.err.println("Error in SQL Prediction");
    throw e;
}
```

#### Parameterized Queries

Execute inference using parameterized SQL queries:

```java
String parameterizedQuery = "SELECT review_text FROM product_reviews WHERE product_category = ? AND sentiment IS NULL LIMIT ?";
Serializable[] params = {"Electronics", 10};

MlSqlJobParameters jobParams = MlSqlJobParameters.builder()
    // ... other parameters ...
    .sqlQuery(parameterizedQuery)
    .sqlParams(params)
    .limit(10) // Additional limit
    .build();

List<Classifications> results = ml.predictFromSql(jobParams);
```

### Colocated Predictions

Execute inference on data stored locally on specific cluster nodes.

```java
String sqlQuery = "SELECT review FROM PRODUCT_REVIEWS WHERE category = ?";
Serializable[] params = {"Electronics"};

try {
    // Create job parameters for parameterized SQL prediction
    MlSqlJobParameters jobParams = MlSqlJobParameters.builder()
            .id(MODEL_ID)
            .version(MODEL_VERSION)
            .type(ModelType.PYTORCH)
            .name("traced_distilbert_sst_english")
            .inputClass(String.class.getName())
            .outputClass(Classifications.class.getName())
            .translatorFactory(TRANSLATOR_FACTORY)
            .sqlQuery(sqlQuery)
            .sqlParams(params)
            .limit(3)
            .build();

    System.out.println("SQL Query: " + sqlQuery);
    System.out.println("SQL Query Params: " + Arrays.toString(params));

    long startTime = System.currentTimeMillis();
    List<Classifications> results = mlApi.predictFromSql(jobParams);

    long duration = System.currentTimeMillis() - startTime;

    System.out.println("Parameterized SQL Prediction (" + results.size() + " items):");
    for (int i = 0; i < results.size(); i++) {
        Classifications classification = results.get(i);
        Classification best = classification.best();
        System.out.printf("   %d → %s (%.2f%%)\n",
                i + 1,
                best.getClassName(),
                best.getProbability() * 100);
    }

    System.out.println("Total processing time: " + duration + "ms");
    System.out.println("Average per item: " + (duration / results.size()) + "ms");
} catch (Throwable e) {
    System.err.println("Error in Parameterized SQL Prediction");
    throw e;
}
```

### Asynchronous Operations

All prediction methods support asynchronous execution:

```java
// Async single prediction
CompletableFuture<Classifications> futureResult = ml.predictAsync(jobParams);

// Async batch prediction 
CompletableFuture<List<Classifications>> futureBatchResults =
    ml.batchPredictAsync(batchJobParams);

// Async SQL prediction
CompletableFuture<List<Classifications>> futureSqlResults =
    ml.predictFromSqlAsync(sqlJobParams);

// Async colocated prediction
CompletableFuture<Classifications> futureColocatedResult =
    ml.predictColocatedAsync(colocatedJobParams);
```

## Execution Modes

GridGain ML examples can run in different modes depending on your deployment scenario. The examples use a base class (`MlBaseExample`) that supports two execution modes:

All four examples supports both execution modes, we can select either `MODE.EMBEDDED` or `MODE.CLIENT_ONLY`

### Available Modes

{% hint style="info" %}
All examples in this documentation support both execution modes.
{% endhint %}

#### Embedded Mode (MODE.EMBEDDED)

Runs the ML inference directly within the GridGain server process.

**Characteristics:**

- Single JVM process
- No separate client connection needed
- Lowest latency for inference operations
- Ideal for testing and development

**Setup:**

```java
start(MODE.EMBEDDED);
mlApi = server.api().ml(); // Direct access to ML API
```

#### Client-Only Mode (MODE.CLIENT_ONLY)

Connects to an existing GridGain cluster as a thin client.

**Characteristics:**

- Requires a running GridGain cluster
- Separate client process connects to the cluster
- Production-ready deployment pattern
- Network overhead for operations

**Setup:**

```java
start(MODE.CLIENT_ONLY);
mlApi = client.ml(); // ML API accessed via client connection
```

## Advanced Usage

### When to Use Standard vs Custom Approaches

#### Use Standard Approach When:

1. **Standard input/output types**: Working with primitives or built-in DJL types (e.g., `String`, `Classifications`)
2. **Built-in DJL translator functionality**: The translator provided by DJL meets your pre/post data processing needs
3. **Simple data flows**: No complex pre/post-processing workflows required

This approach is shown in the basic prediction examples above.

#### Use Custom Compute Jobs When:

1. **Custom input/output types**: Implementing user-defined types that require specialized marshalling beyond built-in DJL serialization
2. **Advanced processing logic**: Building complex pre/post-processing workflows that extend beyond standard translator capabilities
3. **Non-standard data flows**: Creating advanced examples with specialized data handling requirements
4. **Fine-grained execution control**: Needing direct control over the model inference pipeline and data transformation steps

Custom compute jobs provide the flexibility to define independent input types, output types, translators, and marshallers when the standard framework cannot accommodate your specific use case.

### Download Model

Download a zeroshot classification model files from HuggingFace:

```bash
curl --ssl-no-revoke -O "https://huggingface.co/MoritzLaurer/deberta-v3-xsmall-zeroshot-v1.1-all-33/resolve/main/onnx/model_quantized.onnx"
curl --ssl-no-revoke -O "https://huggingface.co/MoritzLaurer/deberta-v3-xsmall-zeroshot-v1.1-all-33/resolve/main/tokenizer.json?download=true"
```

### Custom Translator

Create a custom translator and translator factory to pre-process the inputs before prediction and post process the output from the model for consumption.

#### Step 1: Create a Custom Translator

```java
public class CustomTranslator implements NoBatchifyTranslator<CustomInput, CustomOutput> {
    
    private CustomTranslator(HuggingFaceTokenizer tokenizer, boolean int32) {
        this.tokenizer = tokenizer;
        this.int32 = int32;
    }
    
    @Override
    public void prepare(TranslatorContext ctx) throws IOException, ModelException {
        Model model = ctx.getModel();
        this.predictor = model.newPredictor(new NoopTranslator((Batchifier)null));
        ctx.getPredictorManager().attachInternal(UUID.randomUUID().toString(),
            new AutoCloseable[]{this.predictor});
    }
    
    @Override
    public NDList processInput(TranslatorContext ctx, CustomInput input) {
        //process input to create and return an NDList
    }
    
    @Override
    public CustomOutput processOutput(TranslatorContext ctx, NDList list) 
            throws TranslateException {
        CustomInput input = (CustomInput)ctx.getAttachment("input");
        //process the output (NDList list) and return the custom output
        return new CustomOutput(input.getText(), labels, scores);
    }
}
```

#### Step 2: Create a Custom Translator Factory

```java
public class CustomTranslatorFactory implements TranslatorFactory, Serializable {
    @Override
    public <I, O> Translator<I, O> newInstance(Class<I> input, Class<O> output,
            Model model, Map<String, ?> arguments) {
        // Custom translator implementation
        return new CustomTranslator();
    }
}
```

#### Step 3: Using Custom Translator

```java
MlSimpleJobParameters<CustomInput> jobParams =
    MlSimpleJobParameters.<CustomInput>builder()
        .id(MODEL_ID)
        .version(MODEL_VERSION)
        .type(ModelType.ONNX)
        .name("model_quantized")
        .config(ModelConfig.builder().build())
        .inputClass("org.apache.ignite.example.ml.multiinput.CustomInput")
        .outputClass("org.apache.ignite.example.ml.multiinput.CustomOutput")
        .translatorFactory(
            "org.apache.ignite.example.ml.multiinput.CustomTranslatorFactory")
        .input(input)
        .build();

CustomOutput result = mlApi.predict(jobParams);
System.out.println("Classification Results:");
System.out.println("Text: " + prompt);
System.out.println("Predictions: " + result.getLabels()[0]);
System.out.println("Scores: " + result.getScores()[0]);
```

### Custom Compute Jobs (Brief Introduction)

When you need full control over the prediction pipeline, including custom marshallers for serialization, you can extend the `MlComputeJob` class.

#### Basic Structure

```java
public class CustomComputeJob<I extends MlSimpleJobParameters, O>
        extends MlComputeJob<I, O> {

    @Override
    public CompletableFuture<O> predictAsync(JobExecutionContext context, I arg) {
        if (arg == null) {
            return CompletableFuture.completedFuture(null);
        }
        return context.ignite().ml().predictAsync(arg);
    }

    @Override
    public Marshaller<I, byte[]> inputMarshaller() {
        return new CustomInputMarshaller<>();
    }

    @Override
    public Marshaller<O, byte[]> resultMarshaller() {
        return new CustomOutputMarshaller<>();
    }
}
```

#### When to Use Custom Compute Jobs

Custom compute jobs are required when:

- You have custom input/output types that need specialized serialization
- You need to implement custom marshallers for data transfer
- You want to use different prediction methods (predict, batchPredict, predictFromSql, predictColocated) with custom types

#### Adding to Job Parameters

```java
MlSimpleJobParameters<CustomInput> jobParams =
    MlSimpleJobParameters.<CustomInput>builder()
        // ... standard parameters ...
        .customJobClass(CustomComputeJob.class)
        .customInputMarshaller(new CustomInputMarshaller<>())
        .customOutputMarshaller(new CustomOutputMarshaller<>())
        .build();
```
