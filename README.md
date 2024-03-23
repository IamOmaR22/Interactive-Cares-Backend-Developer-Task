# Document Management Tool

This Django-based Document Management Tool provides API endpoints for user authentication, document CRUD operations and access control.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/IamOmaR22/Interactive-Cares-Backend-Developer-Task.git
   cd Interactive-Cares-Backend-Developer-Task
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the API endpoints:
   - User Signup: [http://127.0.0.1:8000/api/signup/](http://127.0.0.1:8000/api/signup/)
   - User Login: [http://127.0.0.1:8000/api/login/](http://127.0.0.1:8000/api/login/)
   - Document List/Create: [http://127.0.0.1:8000/api/documents/](http://127.0.0.1:8000/api/documents/)
   - Document Detail/Update/Delete: [http://127.0.0.1:8000/api/documents/<document_id>/](http://127.0.0.1:8000/api/documents/<document_id>/)
   - Add/Update Access to a Document: [http://127.0.0.1:8000/api/documents/<document_id>/access/](http://127.0.0.1:8000/api/documents/<document_id>/access/)

---
# Live Link

The API is live and accessible at: [https://document.pythonanywhere.com/api/signup/](https://document.pythonanywhere.com/api/signup/)

## Live API Documentation

- Interactive Swagger Documentation: [https://document.pythonanywhere.com/swagger/](https://document.pythonanywhere.com/swagger/)
- ReDoc Documentation: [https://document.pythonanywhere.com/redoc/](https://document.pythonanywhere.com/redoc/)
- Postman Documentation: [https://documenter.getpostman.com/view/31578330/2sA35Bb3x3](https://documenter.getpostman.com/view/31578330/2sA35Bb3x3)

## Endpoints

### User Management
- **User Signup:** [https://document.pythonanywhere.com/api/signup/](https://document.pythonanywhere.com/api/signup/)
  - Method: POST
  - Request Body:
    ```json
    {
      "username": "your_username",
      "email": "your_email@example.com",
      "password": "your_password"
    }
    ```
  - Response: User created successfully
  
- **User Login:** [https://document.pythonanywhere.com/api/login/](https://document.pythonanywhere.com/api/login/)
  - Method: POST
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - Response: Login successful, token returned

### Document Management
- **Create a Document:** [https://document.pythonanywhere.com/api/documents/](https://document.pythonanywhere.com/api/documents/)
  - Method: POST
  - Request Body:
    ```json
    {
      "title": "Your Document Title",
      "content": "Lorem ipsum dolor sit amet..."
    }
    ```
  - Response: Document created successfully

- **List Documents:** [https://document.pythonanywhere.com/api/documents/](https://document.pythonanywhere.com/api/documents/)
  - Method: GET
  - Response: List of documents belonging to the authenticated user

- **Retrieve a Document:** [https://document.pythonanywhere.com/api/documents/{document_id}/](https://document.pythonanywhere.com/api/documents/{document_id}/)
  - Method: GET
  - Response: Details of the specified document

- **Update a Document:** [https://document.pythonanywhere.com/api/documents/{document_id}/](https://document.pythonanywhere.com/api/documents/{document_id}/)
  - Method: PUT
  - Request Body:
    ```json
    {
      "title": "Updated Document Title",
      "content": "Updated content..."
    }
    ```
  - Response: Document updated successfully
  
- **Delete a Document:** [https://document.pythonanywhere.com/api/documents/{document_id}/](https://document.pythonanywhere.com/api/documents/{document_id}/)
  - Method: DELETE
  - Response: Document deleted successfully

### Access Control
- **Add/Update Access for a Document:** [https://document.pythonanywhere.com/api/documents/{document_id}/access/](https://document.pythonanywhere.com/api/documents/{document_id}/access/)
  - Method: POST
  - Request Body:
    ```json
    {
      "shared_with": [user_id1, user_id2, ...]
    }
    ```
  - Response: Access updated successfully
---

## Local API Documentation

You can view the API documentation and test the endpoints using tools like Swagger or Django Rest Swagger.

- Swagger API Docs: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Django Rest Swagger: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

## Testing the APIs

You can use Postman or any API testing tool to test the API endpoints. Here are some example requests:

### User Signup

- **Endpoint:** [http://127.0.0.1:8000/api/signup/](http://127.0.0.1:8000/api/signup/)
- **Method:** POST
- **Request Body:**
  ```json
  {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }
  ```
- **Response:** User created successfully

### User Login

- **Endpoint:** [http://127.0.0.1:8000/api/login/](http://127.0.0.1:8000/api/login/)
- **Method:** POST
- **Request Body:**
  ```json
  {
    "username": "testuser",
    "password": "password123"
  }
  ```
- **Response:** Login successful, token returned

### Create a Document

- **Endpoint:** [http://127.0.0.1:8000/api/documents/](http://127.0.0.1:8000/api/documents/)
- **Method:** POST
- **Request Body:**
  ```json
  {
    "title": "My Document",
    "content": "Lorem ipsum dolor sit amet..."
  }
  ```
- **Response:** Document created successfully

### Get a List of Documents

- **Endpoint:** [http://127.0.0.1:8000/api/documents/](http://127.0.0.1:8000/api/documents/)
- **Method:** GET
- **Response:** List of documents owned by the user

### Update a Document

- **Endpoint:** [http://127.0.0.1:8000/api/documents/<document_id>/](http://127.0.0.1:8000/api/documents/<document_id>/)
- **Method:** PUT
- **Request Body:**
  ```json
  {
    "title": "Updated Document Title",
    "content": "Updated content..."
  }
  ```
- **Response:** Document updated successfully

### Delete a Document

- **Endpoint:** [http://127.0.0.1:8000/api/documents/<document_id>/](http://127.0.0.1:8000/api/documents/<document_id>/)
- **Method:** DELETE
- **Response:** Document deleted successfully

### Share a Document

- **Endpoint:** [http://127.0.0.1:8000/api/documents/<document_id>/access/](http://127.0.0.1:8000/api/documents/<document_id>/access/)
- **Method:** POST
- **Request Body:**
  ```json
  {
    "shared_with": [2, 3]  // User IDs to share with
  }
  ```
- **Response:** Access updated successfully

### Get a Document with Details

- **Endpoint:** [http://127.0.0.1:8000/api/documents/<document_id>/](http://127.0.0.1:8000/api/documents/<document_id>/)
- **Method:** GET
- **Response:** Details of the specified document

### Get All Shared Documents

- **Endpoint:** [http://127.0.0.1:8000/api/shared-documents/](http://127.0.0.1:8000/api/shared-documents/)
- **Method:** GET
- **Response:** List of documents shared with the user

### Revoke Document Access

- **Endpoint:** [http://127.0.0.1:8000/api/documents/<document_id>/revoke-access/](http://127.0.0.1:8000/api/documents/<document_id>/revoke-access/)
- **Method:** POST
- **Request Body:**
  ```json
  {
    "user_id": 2  // User ID to revoke access
  }
  ```
- **Response:** Access revoked successfully

## Description

This project is a document management tool that allows users to perform various actions such as creating, updating, deleting documents, sharing documents with other users, and managing access control to documents.

## Features

- User Signup and Login
- Create, Update, Delete Documents
- Share Documents with Other Users
- Manage Access Control to Documents

## Technologies Used

- Django
- Django REST Framework
- SQLite

## License

This project is licensed under the [MIT License](LICENSE).

---
