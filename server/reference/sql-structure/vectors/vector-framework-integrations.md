---
description: >-
  MariaDB Vector integrations with popular AI, web and ORM frameworks.
---

# Vector Framework Integrations

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

MariaDB Vector has integrations in several frameworks. For a general overview of MariaDB Vector — feature summary, benchmarks, tutorials, and demos — see the [MariaDB Vector project page](https://mariadb.org/projects/mariadb-vector/).

All of these integrations need a MariaDB version with vector support, as listed in the note above. Some require a later version; check each integration's documentation for its minimum version.

Integrations differ in how much they cover, and in where the code lives. The support column uses these values:

- **Yes** — MariaDB Vector is supported by the framework itself.
- **Yes, via package** — supported through a separate package the framework does not maintain.
- **Yes, MariaDB project** — maintained by MariaDB; not a third-party framework integration.
- **Open request** — an issue asking for the integration is open, but no code has been merged yet.
- **—** — no MariaDB Vector support, and no open request that we know of.

Each table lists supported frameworks first, then those without an integration.

## AI Frameworks

| Framework | Language | MariaDB Vector support | Covers |
| --- | --- | --- | --- |
| [LangChain](https://docs.langchain.com/oss/python/integrations/vectorstores) ([PyPI](https://pypi.org/project/langchain-mariadb/)) | Python | Yes, via package | Store, index, similarity search. The `langchain-mariadb` package is maintained by MariaDB at [mariadb-corporation/langchain-mariadb](https://github.com/mariadb-corporation/langchain-mariadb) |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | Python | Yes | Agentic workflows reuse LangChain vector stores |
| [LangChain4j](https://docs.langchain4j.dev/integrations/embedding-stores/mariadb/) | Java | Yes | `MariaDbEmbeddingStore` in the `dev.langchain4j:langchain4j-mariadb` module |
| [LangChain.js](https://www.npmjs.com/package/@langchain/community) | Node.js | Yes, via package | `MariaDBStore` in `@langchain/community`, which was [deprecated in May 2026](https://github.com/langchain-ai/langchainjs-community/issues/61); no standalone MariaDB package yet |
| [LlamaIndex](https://developers.llamaindex.ai/python/framework-api-reference/storage/vector_store/mariadb/) ([PyPI](https://pypi.org/project/llama-index-vector-stores-mariadb/)) | Python | Yes | `MariaDBVectorStore` in the `llama-index-vector-stores-mariadb` package; synchronous API only |
| [Haystack](https://haystack.deepset.ai/integrations/mariadb-documentstore) ([PyPI](https://pypi.org/project/mariadb-haystack/)) | Python | Yes | `MariaDBDocumentStore` in the `mariadb-haystack` package, maintained by deepset |
| [Spring AI](https://docs.spring.io/spring-ai/reference/api/vectordbs/mariadb.html) | Java | Yes | `MariaDBVectorStore` with Spring Boot auto-configuration via `spring-ai-starter-vector-store-mariadb` |
| [Quarkus LangChain4j](https://docs.quarkiverse.io/quarkus-langchain4j/dev/rag-hibernate-orm-store.html) | Java | Yes | Hibernate ORM embedding store, which supports MariaDB |
| [Laravel AI SDK](https://laravel.com/docs/13.x/ai-sdk#querying-embeddings) | PHP | Yes | Embeddings stored and searched in MariaDB through Laravel's query builder, including the `SimilaritySearch` agent tool |
| [Symfony AI](https://symfony.com/doc/current/ai/components/store.html) ([Packagist](https://packagist.org/packages/symfony/ai-maria-db-store)) | PHP | Yes | MariaDB store bridge in the `symfony/ai-maria-db-store` package |
| [Neuron AI](https://docs.neuron-ai.dev/rag/vector-store) | PHP | Yes | `MariaDBVectorStore`, with vector index and cosine distance |
| [Drupal AI](https://www.drupal.org/project/ai) with [MariaDB VDB Provider](https://www.drupal.org/project/ai_vdb_provider_mariadb) | PHP | Yes, via package | Vector database provider for the AI module and Search API |
| [MariaDB MCP server](https://github.com/mariadb/mcp) | Python | Yes, MariaDB project | SQL access and vector search for AI agents |
| [MariaDB skills for AI coding agents](https://github.com/MariaDB/skills) | — | Yes, MariaDB project | Guidance for agents writing MariaDB Vector SQL |
| [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/) | .NET, Python, Java | — | No MariaDB connector |

## Web Frameworks and ORMs

| Framework | Language | MariaDB Vector support | Covers |
| --- | --- | --- | --- |
| [Hibernate ORM](https://hibernate.atlassian.net/browse/HHH-18900) | Java | Yes | MariaDB vector type, since Hibernate ORM 7.0 |
| [Exposed](https://www.jetbrains.com/help/exposed/vector-types.html) | Kotlin | Yes | Vector column type and distance functions, since Exposed 1.3.0 |
| [ServiceStack OrmLite](https://docs.servicestack.net/ormlite/vectors) | .NET | Yes | Vector columns, vector index and cosine distance, since ServiceStack 10.4 |
| [TypeORM](https://typeorm.io/docs/drivers/mysql/) | TypeScript / Node.js | Yes | MariaDB vector columns only, since TypeORM 0.3.28 |
| [Laravel](https://laravel.com/docs/13.x/queries#vector-similarity-clauses) | PHP | Yes | Vector columns, `VECTOR INDEX`, the `AsVector` cast and similarity queries, since Laravel 13.28. Use the `mariadb` driver. Euclidean distance via [laravel-vector-metrics](https://packagist.org/packages/rhaima96/laravel-vector-metrics); for Laravel 12, [laravel-mariadb-vector](https://packagist.org/packages/devilsberg/laravel-mariadb-vector) |
| [SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/types.html) with [mariadb-vector](https://pypi.org/project/mariadb-vector/) | Python | Yes, via package | VECTOR type and distance functions. The `mariadb-vector` package is community-maintained at [kwon-evan/mariadb-vector](https://github.com/kwon-evan/mariadb-vector) |
| [Django](https://docs.djangoproject.com/en/stable/ref/models/fields/) with [django-mariadb-vector](https://pypi.org/project/django-mariadb-vector/) | Python | Yes, via package | Vector field, `VECTOR INDEX` and distance functions. The `django-mariadb-vector` package is community-maintained at [lexsysko/django-mariadb-vector](https://github.com/lexsysko/django-mariadb-vector). A vector field in Django itself is proposed in [django/new-features#151](https://github.com/django/new-features/issues/151) |
| [Doctrine ORM](https://www.doctrine-project.org/projects/doctrine-dbal/en/current/reference/types.html) | PHP | Open request | [doctrine/dbal#6703](https://github.com/doctrine/dbal/issues/6703). A draft pull request, [doctrine/dbal#7152](https://github.com/doctrine/dbal/pull/7152), adds a vector type for MariaDB |
| [Drizzle ORM](https://orm.drizzle.team/docs/guides/vector-similarity-search) | TypeScript / Node.js | Open request | [drizzle-orm#2007](https://github.com/drizzle-team/drizzle-orm/issues/2007) |
| [jOOQ](https://github.com/jOOQ/jOOQ) | Java | Open request | [jOOQ#19291](https://github.com/jOOQ/jOOQ/issues/19291) |
| [Prisma](https://www.prisma.io/docs/orm/data-modeling) | TypeScript / Node.js | — | Supports MariaDB as a database, but has no vector type for it; see the general [First class Vector support](https://github.com/prisma/orm/issues/26546) request |
| [Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/repositories/vector-search.html) | Java | — | Vector search covers only PGvector and Oracle; MariaDB support can be requested in its [issue tracker](https://github.com/spring-projects/spring-data-jpa/issues) |

For a worked example of picking an embedding model for MariaDB Vector in a Laravel application, see [MariaDB Vector in Laravel: insights on choosing an embedding model](https://mariadb.org/mariadb-vector-in-laravel-insights-on-choosing-an-embedding-model/).

## Low-Code and No-Code AI Platforms

| Platform | MariaDB Vector support | Covers |
| --- | --- | --- |
| [Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling) | Yes | Vector store for retrieval (RAG), with vector index and similarity search, using MariaDB Connector/Python. Community-maintained, added in March 2026 ([open-webui#21931](https://github.com/open-webui/open-webui/pull/21931)) |
| [Dify](https://docs.dify.ai/) | — | No MariaDB vector store |
| [Flowise](https://docs.flowiseai.com/integrations/langchain/vector-stores) | — | No MariaDB vector store |
| [Langflow](https://docs.langflow.org/components-vector-stores) | — | No MariaDB vector store |
| [n8n](https://n8n.io/integrations/categories/ai/vector-stores/) | — | No MariaDB vector store |

## Contributing an Integration

Where to go next depends on the framework's status in the tables above:

- **Marked *Open request*** — add your use case, or just a 👍, to the linked issue. Maintainers prioritize by demand, so this is usually the fastest way to move it forward.
- **Marked with a dash (—)** — there's no known request yet. Open one directly in the framework's own repository or issue tracker; a concrete use case from you carries more weight than one from us.
- **Building the integration yourself** — submit it as a pull request to the framework itself, or to the relevant community package linked in the *Covers* column, following that project's contribution guidelines.

Once it's built or merged, tell us through the MariaDB Ecosystem Hub's [Get Involved page](https://ecohub.mariadb.org/get-involved) or at [foundation@mariadb.org](mailto:foundation@mariadb.org) so we can add it here.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
