# Layout Awareness

When you upload a document (like a PDF) to an AI system, the system needs to read the text. Standard text extractors simply pull the words out left-to-right, top-to-bottom. This works fine for simple text, but it completely destroys the structure of complex documents—tables become jumbled messes of words, headings are lost, and mathematical formulas become unreadable.

Layout-Aware Extraction solves this by intelligently analyzing the visual structure of the document before reading it.

Instead of just extracting raw text, layout-aware processors convert your document into beautifully structured Markdown format. This means:

* Tables remain perfectly aligned and formatted (with rows/columns intact).
* Headings (H1, H2, H3) and reading order are preserved.
* Lists and bullet points stay intact.
* Code blocks and mathematical formulas are accurately captured.

Because the output is clean Markdown, our AI can chunk the document much more intelligently. By pairing this with `chunking_method: "semantic"`, the system naturally splits the document along topical boundaries (headers), leading to vastly superior RAG (Retrieval-Augmented Generation) answers.

## The three extraction tiers

The API offers three different processing tiers, which you can select when uploading documents via the `processor_type` parameter inside the `document_processing` JSON object.

### Tier 1: Base

* Parameter: `processor_type: "base"`
* How it works: Fast, basic text extraction using libraries like pdfplumber and python-docx.
* Pros: Blazing fast, requires no special hardware, works entirely locally. Best for simple, text-heavy documents.
* Cons: Loses complex formatting; tables may be extracted poorly.

### Tier 2: Layout-aware standard

* Parameter: `processor_type: "layout_aware_standard"`
* How it works: Uses the advanced open-source 'Docling' AI engine running locally on your hardware.
* Pros: Excellent preservation of tables, headings, and lists. Supports OCR (Optical Character Recognition) for scanned documents. Completely private and local (no data sent to the cloud).
* Cons: Slower than the base processor; can be CPU/memory intensive.

### Tier 3: Layout-aware advanced

* Parameter: `processor_type: "layout_aware_advanced"`
* How it works: Sends the document to LlamaIndex's premium cloud API service (LlamaParse).
* Pros: The absolute highest quality extraction available. Incredible accuracy on highly complex, multi-column PDFs with dense tables.
* Cons: Requires an active internet connection, requires a paid API key from LlamaIndex, and documents leave your local network.

## API reference

To use advanced processing, you inject a `document_processing` JSON object into your ingestion API calls.

#### A. Manual File Upload Endpoint

**Endpoint:** `POST /documents/ingest`\
**Purpose:** Upload physical files from a user's computer to the API.

Since this is a `multipart/form-data` endpoint, the configuration must be passed as a stringified JSON object in the `document_processing` form field.

**Form Data Example:**

```bash
curl -X POST "http://localhost:8000/api/v1/documents/ingest" \
  -H "Authorization: Bearer <token>" \
  -F "files=@report2024.pdf" \
  -F "chunking_method=semantic" \
  -F 'document_processing={"processor_type": "layout_aware_standard", "enable_ocr": true, "enable_table_extraction": true}'
```

#### B. Cloud Storage / Orchestration Endpoint (Recommended)

**Endpoint:** `POST /orchestrate/ingestion`\
**Purpose:** Programmatically scan an S3/GCS bucket and ingest its contents using a specific processor.

This is a standard JSON endpoint, so you pass the configuration directly as an object.

**JSON Payload Example:**

```json
{
  "chunking_method": "semantic",
  "chunk_size": 512,
  "cloud_storage_sources": [
    {
      "integration_id": "int_abc123",
      "prefix": "financial_reports/Q3/",
      "recursive": true,
      "file_extensions": [".pdf"]
    }
  ],
  "document_processing": {
    "processor_type": "layout_aware_standard",
    "enable_ocr": true,
    "ocr_provider": "rapidocr",
    "enable_table_extraction": true,
    "table_structure_mode": "accurate"
  }
}
```

## Configuration schema options

Here is the complete reference for the `document_processing` JSON object.

| Field            | Type     | Default  | Description                                                       |
| ---------------- | -------- | -------- | ----------------------------------------------------------------- |
| `processor_type` | `string` | `"base"` | `"base"`, `"layout_aware_standard"`, or `"layout_aware_advanced"` |

**Settings for `layout_aware_standard` (Docling):**

| Field                       | Type     | Default      | Description                                                                                                           |
| --------------------------- | -------- | ------------ | --------------------------------------------------------------------------------------------------------------------- |
| `enable_ocr`                | `bool`   | `false`      | Turns on Optical Character Recognition for scanned images.                                                            |
| `ocr_provider`              | `string` | `"rapidocr"` | Engine to use if OCR is enabled: `"rapidocr"` (fastest), `"tesseract"`, `"easyocr"`, or `"surya"` (state-of-the-art). |
| `enable_table_extraction`   | `bool`   | `true`       | Preserves tables as markdown grids.                                                                                   |
| `table_structure_mode`      | `string` | `"accurate"` | Table detection quality: `"accurate"` (better) or `"fast"`.                                                           |
| `enable_code_enrichment`    | `bool`   | `false`      | Specifically detect and format code blocks.                                                                           |
| `enable_formula_enrichment` | `bool`   | `false`      | Specifically detect and format mathematical formulas.                                                                 |
| `enable_ray`                | `bool`   | `false`      | Use Ray cluster for distributed parallel processing of large PDFs.                                                    |

**Settings for `layout_aware_advanced` (LlamaParse):**

| Field               | Type     | Default     | Description                                                                                                    |
| ------------------- | -------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| `llamaparse_preset` | `string` | `"agentic"` | Quality tier: `"cost_effective"` (~~$0.003/page), `"agentic"` (~~$0.01/page), `"agentic_plus"` (\~$0.03/page). |

## Layout-aware standard

### Docling and Ray

The Standard tier uses IBM's Docling engine. Because Docling uses actual machine learning models to visually "read" the document layout, processing a 100-page PDF can take some time.

To solve this performance bottleneck, we integrated "Ray" — a framework for distributed computing.

How Ray Speeds Up Docling: Instead of processing a 100-page PDF sequentially (page 1, then page 2, then page 3...), Ray allows the system to split the document up and process multiple pages simultaneously across different CPU cores or even entirely different servers in a cluster.

Global Configuration Variables (config.env) to control Docling behavior when requested by the API:

* DOCLING\_ENABLE\_OCR=true : Enables OCR globally as default.
* DOCLING\_OCR\_PROVIDER=rapidocr : Global default engine used for OCR.
* DOCLING\_RAY\_ENABLED=true : Turns on parallel processing using Ray.
* DOCLING\_RAY\_NUM\_ACTORS=4 : The number of parallel "workers" to spawn.
* DOCLING\_RAY\_HEAD\_ADDRESS=auto : Set to 'auto' for local processing, or provide an IP address.
* DOCLING\_RAY\_SERVICE\_URL=http://... : (Optional) URL to an external, dedicated Docling HTTP service.

## Layout-aware advanced

### LlamaParse

For enterprise users who need the absolute best accuracy and are willing to use a cloud API, we support LlamaParse.

Configuration Variables (config.env):

* LLAMA\_CLOUD\_API\_KEY=llx-... : Your private API key from https://cloud.llamaindex.ai

LlamaParse Presets: You can control the quality vs. cost ratio of LlamaParse dynamically in the API payload using `llamaparse_preset` or globally via the `LLAMAPARSE_PRESET` env variable:

1. `cost_effective` (\~$0.003 per page): Fast extraction, lower cost. Best for mostly-text documents.
2. `agentic` (\~$0.01 per page): Balanced quality and cost. Excellent table extraction. (Recommended default).
3. `agentic_plus` (\~$0.03 per page): The highest quality available. Extracts intense detail, perfect alignment, and includes image descriptions.

## Summary

* FOR SPEED & SIMPLICITY: Pass `{"processor_type": "base"}` to the API. It is fast and requires zero configuration.
* FOR PRIVATE, HIGH-QUALITY RAG: Pass `{"processor_type": "layout_aware_standard"}` to the API. Ensure you have `DOCLING_RAY_ENABLED=true` set in the environment so the system can use all your CPU cores to process documents faster.
* FOR THE BEST POSSIBLE ACCURACY: Pass `{"processor_type": "layout_aware_advanced", "llamaparse_preset": "agentic"}` to the API. You must provide your `LLAMA_CLOUD_API_KEY` in the environment. This is highly recommended if your documents consist heavily of complex financial tables or multi-column research papers.
