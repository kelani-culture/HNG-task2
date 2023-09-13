# API Documentation

## Introduction

This API provides endpoints for performing CRUD (Create, Read, Update, Delete) operations on a resource. The API accepts a single parameter named `name`, which should be a string. All data submitted through the API is stored in the database. When creating a new entry, both `id` and `name` fields will be returned. The `id` is used for retrieval, updating, and deletion, while the `name` is used for creating a new entry.

## Base URL

# Dummy API Documentation

## Create a New Record

**Request:**

- Method: `POST`
- URL: `http://<url>/api`
- Parameters: 
  - `name` (string, required): The name of the record.

**Response:**

- Status Codes:
  - `201 Created`: Successfully created.
  - `400 Bad Request`: Invalid input data (e.g., if the name contains digits or alphanumeric characters).

**Example:**

```http
POST http://<url>/api
Content-Type: application/json
```

```Json
{
  "name": "John Doe"
}
```


## Update a Record

### Request

- **Method:** `PUT`
- **URL:** `http://<url>/api/{user_id}`
  - Replace `{user_id}` with the unique ID of the record to be updated.
- **Parameters:**
  - `name` (string, required): The new name for the record.

### Response

- **Status Codes:**
  - `200 OK`: Successfully updated.
  - `404 Not Found`: Record with the specified ID does not exist.

### Example

```http
PUT http://<url>/api/123
Content-Type: application/json
```
```
{
  "name": "Jane Doe"
}
```

# Dummy API Documentation

## Read a Record

### Request

- **Method:** `GET`
- **URL:** `http://<url>/api/{user_id}`
  - Replace `{user_id}` with the unique ID of the record to be retrieved.

### Response

- **Status Codes:**
  - `200 OK`: Successfully retrieved.
  - `404 Not Found`: Record with the specified ID does not exist.

### Example

```http
GET http://<url>/api/123
```
*** Response Success ***

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "123",
  "name": "Jane Doe"
}
```

# Dummy API Documentation

## Delete a Record

### Request

- **Method:** `DELETE`
- **URL:** `http://<url>/api/{user_id}`
  - Replace `{user_id}` with the unique ID of the record to be deleted.

### Response

- **Status Codes:**
  - `204 No Content`: Successfully deleted.
  - `404 Not Found`: Record with the specified ID does not exist.

### Example

```http
DELETE http://<url>/api/123
HTTP/1.1 204 No Content
```