# Reranker

Reranking improves retrieval quality in the RAG pipeline.

Vector search is fast, but it can miss deeper contextual relevance. A reranker adds a second pass that rescans the retrieved documents and sorts them by how well they answer the exact query.

In practice, retrieval may return 10 candidate documents. The reranker scores those candidates more precisely and returns the best few results to the next stage.

## Rerank endpoint

Use `POST /rerank` to rerank raw text documents against a query.

This endpoint uses a cross-encoder model to re-score and sort documents. It improves relevance over vector similarity alone.

### Request headers

* `Authorization`: Bearer `<your_jwt_token>`
* `Content-Type`: `application/json`

### Request body

| Field        | Type            | Required | Default                     | Description                                                                                     |
| ------------ | --------------- | -------- | --------------------------- | ----------------------------------------------------------------------------------------------- |
| `query`      | `string`        | Yes      | -                           | Query used to score each document.                                                              |
| `documents`  | `Array<string>` | Yes      | -                           | Document texts to rerank. Must contain at least one item.                                       |
| `doc_ids`    | `Array<Any>`    | No       | `null`                      | Optional IDs for mapping results back to source records.                                        |
| `metadata`   | `Array<dict>`   | No       | `null`                      | Optional metadata entries aligned with each document.                                           |
| `top_k`      | `integer`       | No       | `null`                      | Maximum number of results to return. If omitted, all documents are returned in ranked order.    |
| `model_type` | `string`        | No       | `"flashrank"`               | Backend to use. Valid values: `"flashrank"`, `"sentence-transformers"`, `"cohere"`, `"hybrid"`. |
| `model_name` | `string`        | No       | `"ms-marco-MiniLM-L-12-v2"` | Specific reranker model.                                                                        |
| `alpha`      | `float`         | No       | `0.7`                       | Hybrid-only weight for the cross-encoder score.                                                 |
| `beta`       | `float`         | No       | `0.3`                       | Hybrid-only weight for the TF-IDF score.                                                        |
| `api_key`    | `string`        | No       | `null`                      | Required only when `model_type` is `"cohere"`.                                                  |

### Example request

```json
{
  "query": "What are the financial results for Q3 2023?",
  "documents": [
    "The company released a new product in Q3.",
    "In Q3 2023, the company saw a 20% increase in revenue reaching $5M.",
    "Our marketing budget for 2023 was approved.",
    "Q3 2023 financial statements indicate a strong profit margin."
  ],
  "doc_ids": [101, 102, 103, 104],
  "top_k": 2,
  "model_type": "flashrank",
  "model_name": "ms-marco-MiniLM-L-12-v2"
}
```

### Response format

The response is a JSON array of `RerankResponse` objects, sorted from highest score to lowest score.

| Field      | Type      | Description                                 |
| ---------- | --------- | ------------------------------------------- |
| `doc_id`   | `Any`     | Document ID, if provided in the request.    |
| `text`     | `string`  | Document text.                              |
| `score`    | `float`   | Relevance score. Higher is better.          |
| `rank`     | `integer` | Final rank. `1` is best.                    |
| `metadata` | `dict`    | Metadata entry, if provided in the request. |

### Example response

```json
[
  {
    "doc_id": 102,
    "text": "In Q3 2023, the company saw a 20% increase in revenue reaching $5M.",
    "score": 0.985,
    "rank": 1,
    "metadata": null
  },
  {
    "doc_id": 104,
    "text": "Q3 2023 financial statements indicate a strong profit margin.",
    "score": 0.892,
    "rank": 2,
    "metadata": null
  }
]
```

## Reranking in the full pipeline

You will usually enable reranking inside `POST /orchestrate/generation`.

Include a `reranking` object in the request body:

```json
{
  "query": "What are the key findings?",
  "document_ids": [1, 2, 3],
  "retrieval_method": "hybrid",
  "top_k": 5,
  "reranking": {
    "enabled": true,
    "model_type": "flashrank",
    "model_name": "ms-marco-MiniLM-L-12-v2",
    "top_k": 5
  },
  "llm_provider": "openai",
  "llm_model": "gpt-4"
}
```

If `reranking.enabled` is `true`, the system fetches extra documents first, such as `top_k * 2.0`. It reranks them and forwards only the best `top_k` results to the LLM.

## Supported models and providers

The reranking layer supports multiple backends and models.

By default, the system uses FlashRank with `ms-marco-MiniLM-L-12-v2`.

Why this default:

* It is fast.
* It runs well on CPUs.
* It does not require a GPU.
* It is cached in memory for faster repeated requests.

Supported backends:

1. `flashrank`: Default option for fast local CPU deployments. Example: `ms-marco-MiniLM-L-12-v2`
2. `sentence-transformers`: Local Python ML environments. Example: `cross-encoder/ms-marco-TinyBERT-L-2-v2`
3. `cohere`: External cloud API. Example: `rerank-english-v3.0`

## Configuration

You can control default reranker behavior through `config.env`.

### Core settings

* `RERANKING_ENABLED=true`: Enables or disables reranking globally.
* `RERANKING_MODEL_TYPE=flashrank`: Selects the backend.
* `RERANKING_MODEL_NAME=ms-marco-MiniLM-L-12-v2`: Selects the model.
* `RERANKING_API_KEY=`: Required only for cloud providers such as Cohere.

### Search strategy settings

* `RERANKING_TOP_K_MULTIPLIER=2.0`: Number of extra documents to fetch before reranking.
* `RERANKING_DEFAULT_TOP_K=5`: Default number of reranked results to return.

With a multiplier of `2.0`, a request for 5 final documents pulls 10 candidates before reranking.

### Performance and caching settings

* `RERANKING_CACHE_MODELS=true`: Keeps models loaded in memory.
* `RERANKING_CACHE_MAX_SIZE=3`: Maximum number of cached models.
* `RERANKING_ENABLE_BATCHING=true`: Processes documents in batches.
* `RERANKING_BATCH_SIZE=32`: Number of documents scored per batch.

## Presets

You can also use built-in presets through `RERANKING_PRESET`.

### `fast`

* Model: `ms-marco-TinyBERT-L-2-v2` with FlashRank
* Best for lowest latency
* Uses a `1.5x` multiplier

### `balanced`

* Model: `ms-marco-MiniLM-L-12-v2` with FlashRank
* Default preset
* Balances speed and quality
* Uses a `2.0x` multiplier

### `quality`

* Model: `BAAI/bge-reranker-v2-m3` with Sentence-Transformers
* Best for highest accuracy
* Better suited to GPU-backed deployments
* Uses a `3.0x` multiplier

## Summary

* For standard use, keep the default FlashRank setup.
* For custom workflows, use `POST /rerank`.
* For higher accuracy on strong hardware, use `RERANKING_PRESET=quality`.
* For fully managed cloud reranking, use `RERANKING_MODEL_TYPE=cohere` and provide `RERANKING_API_KEY`.
