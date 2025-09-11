

# SkyAI Agent  API – User Guide

## Overview

The **SkyAI Agent API** lets developers interact with **AI agents** built and hosted on the SkySQL platform. This API is perfect for embedding **conversational AI experiences** in your applications, dashboards, or internal tools – all without the need for complex LLM infrastructure or MLOps.


## Authentication

To make requests to the API, you must authenticate using an **API key**.

**Steps:**

1.  **Get an API Key**

      * Go to: [SkySQL API Key Management](https://app.skysql.com/user-profile/api-keys)
      * Generate a new API key.

2.  **Include the key in your request headers:**

    ```
    X-API-Key: YOUR_API_KEY
    ```

-----

-----

## Maintaining Chat Sessions

The **SkyAI Agent Session API** allows you to initiate and manage conversational sessions with your SkyAI agents. Sessions are crucial for maintaining context across multiple interactions, which leads to more natural and coherent conversations with the agent.

-----

### Creating a Session

  * **Endpoint:**

    ```
    POST https://api.skysql.com/copilot/v1/session
    ```

  * **Headers:**

    ```
    Content-Type: application/json
    X-API-Key: YOUR_API_KEY
    ```

  * **Request Body:**

    ```json
    {
      "agent_id": "your-agent-id",
      "metadata": {
        "user_id": "optional-user-id",
        "conversation_topic": "optional-topic"
      }
    }
    ```

      * `agent_id` (string): The identifier of the SkyAI agent you want to talk to.
      * `metadata` (object, optional): Any additional information to associate with the session, like user identifiers or conversation topics.

**Example using `curl`:**

```bash
curl -X POST https://api.skysql.com/copilot/v1/session \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
        "agent_id": "agent-12345",
        "metadata": {
          "user_id": "user-67890",
          "conversation_topic": "monthly sales report"
        }
      }'
```

-----

### Response Structure

A successful response will return a JSON object containing:

  * `session_id` (string): A unique identifier for the session that was created.
  * `agent_id` (string): The identifier of the agent associated with this session.
  * `created_at` (string): A timestamp indicating when the session was created.

**Example Response:**

```json
{
  "session_id": "session-abcde12345",
  "agent_id": "agent-12345",
  "created_at": "2025-05-21T18:37:00Z"
}
```

-----

### Using the Session

Once you have a `session_id`, include it in all subsequent interactions with the agent to maintain context:

  * **Chat Endpoint:**

    ```
    POST https://api.skysql.com/copilot/v1/chat
    ```

  * **Request Body:**

    ```json
    {
      "prompt": "Your question here",
      "session_id": "session-abcde12345"
    }
    ```

Maintaining the same `session_id` across multiple requests lets the agent remember previous interactions, leading to more coherent conversations.

-----

### Error Handling

If your request is invalid or unauthorized, you might receive error responses such as:

  * **401 Unauthorized:** Missing or invalid API key.
  * **400 Bad Request:** Malformed request syntax or missing required fields.
  * **500 Internal Server Error:** An error occurred on the server.

Always ensure your API key is valid and your request body is correctly formatted.

-----

### Tips for Effective Use of Sessions

  * **Session Management:** Use the same `session_id` for a series of related interactions to keep the conversation flowing.
  * **Metadata Usage:** Leverage the `metadata` field to store relevant information that can help the agent provide more personalized responses.
  * **Session Termination:** Implement logic in your application to end sessions when they're no longer needed, which helps free up resources.

-----


## Making a Chat  Request
The  Chat API allows you to send natural language prompts to a SkyAI agent and receive structured responses, including generated SQL and data results when applicable. It supports both stateless and multi-turn conversational use cases and lets you pass agent-specific configuration such as table filters to control the context of the response.

The optional config object allows you to customize how the agent accesses and filters data during query generation. This is especially useful for enforcing data policies, scoping context, or running controlled experiments.

IMPORTANT: You can use this API on its own for single interactions, or in conjunction with the Session API to maintain context across multi-turn conversations with the same agent.
  * **Endpoint:**

    ```
    POST https://api.skysql.com/copilot/v1/chat
    ```

  * **Headers:**

    ```
    Content-Type: application/json
    X-API-Key: YOUR_API_KEY
    ```

  * **Request Body:**

    ```json
    {
      "prompt": "Your natural language question",
      "agent_id": "your agent id",
      "session_id": "optional-session-id",
      "config": {
        "table_filter": {
          "table":"column=value"
        }
      }
    }
    ```

      * `prompt` (string): Your question to the SkyAI agent.
      * `agent_id` (string): The UUID of the SkyAI agent to query
      * `session_id` (string, optional): Use this to maintain 
      conversational context across turns.
      * `config` (object, optional): Configuration to pass contextual filters (e.g., row-level security, scope)
      * `table_filters` (object,optional): Key-value pairs where the key is a table name, and the value is a SQL WHERE clause to apply automatically


 
      
**Example using `curl`:**

```bash
curl -X POST https://api.skysql.com/copilot/v1/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
        "prompt": "What was the total revenue last quarter for the enterprise division?",
        "session_id": "session-4567",
        "agent_id": "your-agent-id",
        "config": {
          "table_filters": {
            "sales": "division = '\''enterprise'\'' AND order_date >= '\''2024-10-01'\'' AND order_date <= '\''2024-12-31'\''"
          }
        }
      }'
  ```

-----

## Response Format

A successful response returns a structured JSON object:

  * `response`: The agent's natural language reply.
  * `sql`: (if applicable) The SQL generated by the agent to answer the question.
  * `data`: Structured data returned (if relevant).
  * `session_id`: Echoes your session ID, to help manage stateful interactions.

**Example Response:**

```json
{
  "response": "Here are the top 5 products by revenue last month.",
  "sql": "SELECT product_name, SUM(revenue) FROM sales WHERE date >= '2024-04-01' AND date <= '2024-04-30' GROUP BY product_name ORDER BY SUM(revenue) DESC LIMIT 5;",
  "data": [
    { "product_name": "Widget A", "revenue": 124000 },
    { "product_name": "Widget B", "revenue": 115000 }
  ],
  "session_id": "session-4567"
}
```

-----

## Error Handling

| Code | Meaning             | Explanation               |
| :--- | :------------------ | :------------------------ |
| 401  | Unauthorized        | Missing or invalid API key |
| 400  | Bad Request         | Malformed request syntax  |
| 500  | Internal Server Error | Something went wrong on the backend |

-----

## Best Practices

  * Use `session_id` to maintain conversation context across multiple prompts.
  * Check the `sql` output if you’re debugging or want insight into how the agent is reasoning.
  * Use clear, specific language in your prompts for optimal results.
  * Validate `data` before injecting it into your UI or downstream services.

-----

# Useful Links

  * **API Reference:** [SkyAI Agent API Docs](https://apidocs.skysql.com/)
  * **SkySQL Console:** [SkySQL Portal](https://app.skysql.com)