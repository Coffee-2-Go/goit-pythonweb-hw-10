# Tier 2. Module 6 - Fullstack Web Development with Python

## Topic 8. Homework - Building a REST API. Application Architecture

### Description

REST API for storing and managing contacts. The API is built using the FastAPI infrastructure and SQLAlchemy for database management.

### Instruction

Python >=3.14 and Poetry >= 2.3 are required to run the code.

1. Clone The Repo

```bash
git clone https://github.com/Coffee-2-Go/goit-pythonweb-hw-10.git
cd goit-pythonweb-hw-10
```

2. Configure Environment Variables

Create a local `.env` file from `.env.example` and fill in your own values:

```bash
cp .env.example .env
```

3. Start applicaton

```bash
docker compose up --build
```

4. Run migrations in a separate terminal

```bash
docker exec -it contacts-app alembic revision --autogenerate -m "Create contacts table"
docker exec -it contacts-app alembic upgrade head
```

5. Access http://localhost:8000/docs/

6. Stop the container and remove the REST API volume

```bash
docker compose down -v
```

### Technical task

#### Part 1

1. **Contacts**

To store your system's contacts, you need to organize a database that will contain all the necessary information.

This information should include:

- First name
- Last name
- Email address
- Phone number
- Birthday
- Additional data (optional)

2. **API**

The API you are developing should support basic data operations. Below is a list of actions that your API should be able to perform:

- Create a new contact
- Get a list of all contacts
- Get a single contact by ID
- Update an existing contact
- Delete a contact

3. **CRUD API**

In addition to the basic CRUD functionality, the API should also have the following features:

- Contacts should be searchable by first name, last name, or email address (Query parameters).
- The API should be able to get a list of contacts with birthdays for the next 7 days.

#### Part 2

- Implement an authentication mechanism in the application.
- Implement an authorization mechanism using JWT tokens so that all operations with contacts are performed only by registered users.
- A user should only have access to their own operations with contacts.
- Implement a mechanism to verify the registered user's email.
- Limit the number of requests to the user's `/me` route.
- Enable CORS for your REST API.
- Implement the ability to update the user's avatar (use the Cloudinary service).

### General requirements

#### Part 1

1. Using the FastAPI framework to create the API
2. Using the SQLAlchemy ORM to work with the database
3. PostgreSQL should be used as the database.
4. Support for CRUD operations for contacts
5. Support for storing the contact's date of birth
6. Provide Swagger documentation for the REST API
7. Using the Pydantic data validation module

#### Part 2

1. When registering, if a user already exists with such an `email`, the server should return an `HTTP 409 Conflict` error.
2. The server should hash the password and not store it in plain text in the database.
3. In case of successful user registration, the server should return an HTTP response status of 201 Created and the new user data.
4. For all `POST` operations (creating a new resource), the server should return a status of `201 Created`.
5. During the `POST` operation, user authentication occurs, the server should accept a request with user data (name and password) in the request body.
6. If the user does not exist or the password does not match, an `HTTP 401 Unauthorized` error should be returned.
7. The authorization mechanism using `JWT` tokens should be implemented through the access token `access_token`.
8. All environment variables should be stored in the `.env` file. There should be no confidential data in the "clean" form inside the code.
9. Docker Compose is used to launch all services and databases in the application.
