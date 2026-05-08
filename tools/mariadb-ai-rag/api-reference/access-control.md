---
description: >-
  MariaDB AI RAG access control endpoints manage authentication, role
  assignment, document sharing, and ingest directory configuration using JWT
  tokens and admin-only operations.
---

# Access Control

## Overview

The API implements a comprehensive access control system that includes:

1. **Authentication** - JWT-based authentication with support for multiple token types
2. **Role-Based Access Control** - Different permission levels for users
3. **Document-Level Permissions** - Control who can access specific documents

## Authentication

### Login for Access Token

```
POST /token
```

**Purpose**: Authenticates a user and provides a JWT token for subsequent API calls.

**Request body**:

```json
{
  "username": "user@example.com",
  "password": "secure_password"
}
```

**Response**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Usage Example**: Authentication should be performed before any other API calls.

```bash
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=secure_password"
```

## User Management

### Register User

```
POST /users/register
```

**Purpose**: Creates a new user account (admin only).

**Request body**:

```json
{
  "email": "newuser@example.com",
  "password": "secure_password"
}
```

**Response**:

```json
{
  "email": "newuser@example.com",
  "id": 42,
  "is_active": true
}
```

**Usage Example**:

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "password": "secure_password"
  }'
```

### Get Current User

```
GET /users/me
```

**Purpose**: Retrieves information about the currently authenticated user.

**Response**:

```json
{
  "email": "user@example.com",
  "id": 42,
  "is_active": true,
  "roles": ["user", "admin"]
}
```

### Delete User

```
DELETE /users/delete
```

**Purpose**: Deletes a user by email address (admin only).

**Request body**:

```json
{
  "email": "user@example.com"
}
```

**Response**:

```json
{
  "message": "User user@example.com deleted successfully"
}
```

**Usage Example**:

```bash
curl -X DELETE "http://localhost:8000/users/delete" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com"}'
```

**Note**: Users cannot delete their own admin account. Only admin users can delete other users.

## Document Sharing

### Share Document

```
POST /documents/{document_id}/share
```

**Purpose**: Shares a document with specific users.

**Request body**:

```json
{
  "user_emails": ["user1@example.com", "user2@example.com"]
}
```

**Response**:

```json
{
  "document_id": 42,
  "shared_with": ["user1@example.com", "user2@example.com"],
  "status": "success"
}
```

**Usage Example**: Use this endpoint to share documents with other users.

```bash
curl -X POST "http://localhost:8000/documents/42/share" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_emails": ["user1@example.com", "user2@example.com"]}'
```

### List Document Access

```
GET /documents/{document_id}/access
```

**Purpose**: Lists all users who have access to a document.

**Response**:

```json
{
  "document_id": 42,
  "owner": "admin@example.com",
  "shared_with": ["user1@example.com", "user2@example.com"]
}
```

## Role Management

### Get User Roles

```
GET /users/me/roles
```

**Purpose**: Gets the roles assigned to the current user.

**Response**:

```json
{
  "roles": ["user", "admin"]
}
```

### Add User Role

```
POST /users/{user_id}/roles
```

**Purpose**: Assigns a role to a user (admin only).

**Request body**:

```json
{
  "role": "admin"
}
```

### Remove User Role

```
DELETE /users/{user_id}/roles/{role_name}
```

**Purpose**: Removes a role from a user (admin only).

## User Directory Management

The API supports custom ingest directories for users, allowing administrators to configure where each user's documents are stored and ingested from.

### Get User Ingest Directory

```
GET /users/ingest-directory?email={email}
```

**Purpose**: Retrieves the custom ingest directory configured for a user (admin only or self).

**Query Parameters**:

* `email` (required): Email address of the user

**Response**:

```json
{
  "email": "user@example.com",
  "ingest_directory": "/data/users/user@example.com",
  "created_at": "2025-10-20T10:00:00",
  "updated_at": "2025-10-20T10:00:00"
}
```

**Response (no directory configured)**:

```json
{
  "email": "user@example.com",
  "ingest_directory": null,
  "message": "No custom ingest directory configured"
}
```

**Usage Example**:

```bash
curl -X GET "http://localhost:8000/users/ingest-directory?email=user@example.com" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Note**: Users can view their own ingest directory, but only admins can view other users' directories.

### Set User Ingest Directory

```
POST /users/ingest-directory
```

**Purpose**: Sets or updates the custom ingest directory for a user (admin only).

**Request body**:

```json
{
  "email": "user@example.com",
  "directory": "/data/users/user@example.com"
}
```

**Response**:

```json
{
  "email": "user@example.com",
  "ingest_directory": "/data/users/user@example.com",
  "created_at": "2025-10-20T10:00:00",
  "updated_at": "2025-10-20T10:00:00",
  "message": "Ingest directory set successfully"
}
```

**Usage Example**:

```bash
curl -X POST "http://localhost:8000/users/ingest-directory" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "directory": "/data/users/user@example.com"}'
```

**Validation**:

* The directory path must exist on the server
* Only admin users can set ingest directories
* The directory path is validated before being saved

### Delete User Ingest Directory

```
DELETE /users/ingest-directory
```

**Purpose**: Removes the custom ingest directory configuration for a user (admin only).

**Request body**:

```json
{
  "email": "user@example.com"
}
```

**Response**:

```json
{
  "email": "user@example.com",
  "ingest_directory": null,
  "message": "Ingest directory deleted successfully"
}
```

**Response (no directory configured)**:

```json
{
  "email": "user@example.com",
  "ingest_directory": null,
  "message": "No custom ingest directory was configured"
}
```

**Usage Example**:

```bash
curl -X DELETE "http://localhost:8000/users/ingest-directory" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com"}'
```

**Note**: Deleting the ingest directory configuration will cause the user to fall back to the default ingest directory (`./`).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
