# API Documentation

## Introduction

This API provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on a resource. The API accepts a single parameter named `name`, which should be a string. All data submitted through the API is stored in the database. When creating a new entry, both `id` and `name` fields will be returned. The `id` is used for retrieval, updating, and deletion, while the `name` is used for creating a new entry.

## Base URL

The base URL for all endpoints is:


## Endpoints

### Create a new entry

#### Request

- URL: `/api/resource`
- Method: `POST`
- Content-Type: `application/json`

Creates a new entry with the provided `name`.

#### Parameters

| Name | Type   | Description         |
| ---- | ------ | ------------------- |
| name | string | The name to be added |

#### Example

```json
{
  "name": "John Doe"
}
```

### Response

- Status: `201 Created`

Returns both the `id` and `name`

```
{
  "id": 1,
  "name": "John Doe"
}



# Update an Entry

**Request**

- URL: `/api/resource/{id}`
- Method: `PUT`
- Content-Type: `application/json`

Updates the name of the specified entry using its ID.

**Parameters**

| Name | Type | Description       |
| ---- | ---- | ----------------- |
| id   | int  | The ID of the entry |
| name | string | New name value     |

**Example**

```json
{
  "name": "Jane Doe"
}

# Delete an Entry

## Request

- **URL:** `/api/resource/{id}`
- **Method:** `DELETE`

Deletes the entry with the specified ID.

## Parameters

| Name | Type | Description       |
| ---- | ---- | ----------------- |
| id   | int  | The ID of the entry |

## Response

- **Status:** `204 No Content`

Indicates successful deletion.