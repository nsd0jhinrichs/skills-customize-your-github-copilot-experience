# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and learn how to create endpoints, validate request data, and return clear HTTP responses.

## 📝 Tasks

### 🛠️ Build Your First FastAPI Endpoint

#### Description
Create a FastAPI app and implement a basic endpoint to confirm that your API is running.

#### Requirements
Completed program should:

- Create an app instance using `FastAPI()`
- Implement a `GET /` endpoint that returns a welcome message in JSON
- Implement a `GET /health` endpoint that returns `{ "status": "ok" }`


### 🛠️ Create REST Endpoints for Items

#### Description
Add REST endpoints to manage a small collection of items (for example: books, games, or tasks) stored in memory.

#### Requirements
Completed program should:

- Implement `GET /items` to return all items
- Implement `GET /items/{item_id}` to return one item by ID
- Implement `POST /items` to create a new item with a unique ID
- Return `404` when an item ID does not exist


### 🛠️ Add Validation and Better API Responses

#### Description
Use Pydantic models to validate incoming data and improve how your API handles invalid requests.

#### Requirements
Completed program should:

- Define a request model with required fields (for example: `name`, `category`, `price`)
- Validate that `price` is greater than 0
- Return appropriate HTTP status codes (`200`, `201`, `404`, `422`)
- Include clear JSON messages for success and error cases
