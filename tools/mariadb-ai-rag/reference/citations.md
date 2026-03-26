# Citations

In a Retrieval-Augmented Generation (RAG) system, the AI answers with retrieved documents from your database.

Citations show exactly where an answer came from. They point to the document, page, and chunk used for that statement.

This improves trust, verification, and auditability. It also helps reduce hallucinations by exposing the source material.

## How citations work

The citation flow runs automatically during generation:

1. **Retrieval and reranking**: The system finds the most relevant document chunks.
2. **Context injection**: Each chunk is passed to the model with a source ID such as `Source 1` or `Source 2`.
3. **Generation with markers**: The model inserts raw markers such as `[1]` or `[src_1]` when it uses a source.
4. **Citation processing**: The internal `CitationProcessor` validates and formats these markers before returning the response.
   * **Validation**: Confirms the model did not reference a non-existent source.
   * **Formatting**: Converts raw markers into formatted citations such as footnotes or superscripts.
5. **Final output**: The user receives formatted text and structured citation metadata, including titles, snippets, and page numbers.

## Supported citation styles

The `CitationStyle` configuration supports these rendering styles:

1. **Footnote** (default): Adds a reference in the text and a detailed citation list at the bottom.
   * Example text: `The company revenue grew by 20%[^1].`
   * Example citation: `[^1]: **Financial_Report.pdf** (p. 15) — _Revenue increased significantly in Q3..._`
2. **Superscript**: Renders citations as HTML superscripts.
   * Example text: `The company revenue grew by 20%<sup>[1]</sup>`

## API response structure

The API response includes dedicated citation fields:

* `markdown_content`: Final text with formatted citations.
* `raw_content`: Text with all citation markers removed.
* `citations`: Array with metadata for each cited source.
  * `id`: Citation marker, such as `src_1`
  * `title`: Document filename or title
  * `page_number`: Page where the text was found
  * `snippet`: First 200 characters of the source chunk
* `citation_spans`: Array with citation start and end positions for frontend highlighting.
