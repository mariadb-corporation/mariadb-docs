---
description: >-
  MariaDB Vector integrations with popular AI, web and ORM frameworks.
---

# Vector Framework Integrations

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/pBQsCgBA6SJpi0m3pZuk/" %}

{% include "../../../.gitbook/includes/vectors-are-available-from-....md" %}

MariaDB Vector has integrations in several frameworks. For a general overview of MariaDB Vector — feature summary, benchmarks, tutorials, and demos — see the [MariaDB Vector project page](https://mariadb.org/projects/mariadb-vector/).

Integrations differ in how much they cover, and in where the code lives. The support column uses these values:

- **Yes** — MariaDB Vector is supported by the framework itself.
- **Via package** — supported through a separate package the framework does not maintain.
- **Partial** — the framework covers part of it; a package covers the rest.
- **MariaDB project** — maintained by MariaDB; not a third-party framework integration.
- **Open request** — an issue asking for the integration is open, but no code has been merged yet.
- **Submitted, not merged** — a contributor built and submitted an integration, but it was not merged.
- **—** — no MariaDB Vector support, and no open request that we know of.

Each table lists supported frameworks first, then those without an integration.

## AI Frameworks

| Framework | Language | MariaDB Vector support | Covers |
| --- | --- | --- | --- |
| [LangChain](https://docs.langchain.com/oss/python/integrations/vectorstores) ([PyPI](https://pypi.org/project/langchain-mariadb/)) | Python | Yes, via package | Store, index, similarity search. The `langchain-mariadb` package is maintained by MariaDB at [mariadb-corporation/langchain-mariadb](https://github.com/mariadb-corporation/langchain-mariadb) |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Python | Yes | Agentic workflows reuse LangChain vector stores |
| [LangChain4j](https://docs.langchain4j.dev/integrations/embedding-stores/mariadb/) | Java | Yes | `MariaDbEmbeddingStore` in the `dev.langchain4j:langchain4j-mariadb` module |
| [LangChain.js](https://www.npmjs.com/package/@langchain/community) | Node.js | Yes, via package | `MariaDBStore`, exported from `@langchain/community` as `@langchain/community/vectorstores/mariadb` |
| [LlamaIndex](https://developers.llamaindex.ai/python/framework-api-reference/storage/vector_store/mariadb/) | Python | Yes | Vector store in the LlamaIndex repository; synchronous API only |
| [Spring AI](https://docs.spring.io/spring-ai/reference/api/vectordbs/mariadb.html) | Java | Yes | `MariaDBVectorStore` with Spring Boot auto-configuration via `spring-ai-starter-vector-store-mariadb` |
| [MariaDB MCP server](https://github.com/mariadb/mcp) | Python | Yes, MariaDB project | SQL access and vector search for AI agents |
| [MariaDB skills for AI coding agents](https://github.com/MariaDB/skills) | — | Yes, MariaDB project | Guidance for agents writing MariaDB Vector SQL |
| [Haystack](https://haystack.deepset.ai/integrations?type=Document+Store) | Python | Open request | [haystack-core-integrations#2340](https://github.com/deepset-ai/haystack-core-integrations/issues/2340) |
| [MindSQL](https://github.com/Mindinventory/MindSQL) | Python | Open request | A complete integration submitted [PR #34](https://github.com/Mindinventory/MindSQL/pull/34) |
| [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/) | .NET, Python, Java | — | No MariaDB connector |

## Web Frameworks and ORMs

| Framework | Language | MariaDB Vector support | Covers |
| --- | --- | --- | --- |
| [Hibernate ORM](https://hibernate.atlassian.net/browse/HHH-18900) | Java | Yes | MariaDB vector type, since Hibernate ORM 7.0 |
| [TypeORM](https://typeorm.io/docs/drivers/mysql/) | TypeScript / Node.js | Yes | MariaDB vector columns, since TypeORM 0.3.28 |
| [Laravel](https://laravel.com/docs/13.x/migrations#column-method-vector) with [laravel-mariadb-vector](https://packagist.org/packages/devilsberg/laravel-mariadb-vector) | PHP | Yes, partial | Laravel core provides vector columns and indexes — `$table->vectorIndex('embedding')` compiles to a MariaDB `VECTOR INDEX` with `M=6 DISTANCE=cosine` ([#60334](https://github.com/laravel/framework/pull/60334)). Separately, the package adds Eloquent vector casting and similarity-search macros; only the `ORDER BY`-based macros (`orderByVectorDistance`, `nearestNeighbors`) can use that index — `whereVectorSimilarTo` filters by threshold and always does a full table scan |
| [SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/types.html) with [mariadb-vector](https://pypi.org/project/mariadb-vector/) | Python | Yes, via package | VECTOR type and distance functions. The `mariadb-vector` package is community-maintained at [kwon-evan/mariadb-vector](https://github.com/kwon-evan/mariadb-vector) |
| [Doctrine ORM](https://www.doctrine-project.org/projects/doctrine-dbal/en/current/reference/types.html) | PHP | Open request | [doctrine/dbal#6703](https://github.com/doctrine/dbal/issues/6703) |
| [Drizzle ORM](https://orm.drizzle.team/docs/guides/vector-similarity-search) | TypeScript / Node.js | Open request | [drizzle-orm#2007](https://github.com/drizzle-team/drizzle-orm/issues/2007) |
| [Django](https://docs.djangoproject.com/en/stable/ref/models/fields/) | Python | — | Django ships no vector field for any database. MariaDB Vector is native to the server, so this is client-side work only: a Django field mapping to the `VECTOR` type |
| [Prisma](https://www.prisma.io/docs/orm/prisma-schema/data-model/models) | TypeScript / Node.js | — | Supports MariaDB as a database, but has no vector type for it; see the general [First class Vector support](https://github.com/prisma/prisma/issues/26546) request |

For a worked example of picking an embedding model for MariaDB Vector in a Laravel application, see [MariaDB Vector in Laravel: insights on choosing an embedding model](https://mariadb.org/mariadb-vector-in-laravel-insights-on-choosing-an-embedding-model/).

## Low-Code and No-Code AI Platforms

None of these platforms has a MariaDB vector-store connector yet. Each link goes to the platform's own vector-store documentation, where you can check current support and file a request if one doesn't exist.

- [Dify — vector database configuration](https://docs.dify.ai/)
- [n8n — vector store nodes](https://n8n.io/integrations/categories/ai/vector-stores/)
- [Flowise — vector stores](https://docs.flowiseai.com/integrations/langchain/vector-stores)
- [Langflow — vector store components](https://docs.langflow.org/components-vector-stores)
- [Open WebUI — retrieval and vector databases](https://docs.openwebui.com/features/chat-conversations/rag/)

## Contributing an Integration

Where to go next depends on the framework's status in the tables above:

- **Marked *Open request*** — add your use case, or just a 👍, to the linked issue. Maintainers prioritize by demand, so this is usually the fastest way to move it forward.
- **Marked with a dash (—)** — there's no known request yet. Open one directly in the framework's own repository or issue tracker; a concrete use case from you carries more weight than one from us.
- **Building the integration yourself** — submit it as a pull request to the framework itself, or to the relevant community package linked in the *Covers* column, following that project's contribution guidelines.

Once it's built or merged, tell us through the MariaDB Ecosystem Hub's [Get Involved page](https://ecohub.mariadb.org/get-involved) or at [foundation@mariadb.org](mailto:foundation@mariadb.org) so we can add it here.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
