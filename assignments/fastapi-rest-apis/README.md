# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework in Python, focusing on routing, request handling, response formatting, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Set Up Basic FastAPI Application

#### Description
Create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the server and verify the endpoint works

### 🛠️ Implement CRUD Endpoints for Items

#### Description
Add endpoints to perform Create, Read, Update, and Delete operations on a simple "item" resource.

#### Requirements
Completed program should:

- Define a Pydantic model for Item with fields like id, name, and description
- Implement GET /items to retrieve all items
- Implement POST /items to create a new item
- Implement GET /items/{item_id} to retrieve a specific item
- Implement PUT /items/{item_id} to update an item
- Implement DELETE /items/{item_id} to delete an item

### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance the API with input validation using Pydantic and proper error responses.

#### Requirements
Completed program should:

- Use Pydantic models for request bodies with validation
- Handle cases where an item is not found (return 404)
- Ensure proper HTTP status codes for different operations
- Add basic error messages for invalid requests