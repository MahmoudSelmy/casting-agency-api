# FSND: Capstone Project

## Start Project locally

```bash
cd <project-root-dir>
pg_ctl -D <postgress-path> start
createdb agency
pip install -r requirements.txt
python app.py
```

## API Documentation

### 1. GET /actors

Get page of actors
- Request Arguments: 
    - **integer** `page` (optional, 10 actors per page, defaults to `1`)
- Requires permission: `get:actors`
- Returns: 
  1. **list** `actors`:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`
  2. **boolean** `success`
  3. **total_actors** `age`
- Example:
  - URL: 
  - Response:
- Errors:
  - 404 : invalid page number
  - 401 : un authorized

### 2. POST /actors

Post new actor.
- Body:
  - **string** `name`
  - **integer** `age`
  - **string** `gender`
- Requires permission: `post:actors`
- Returns: 
  1. **integer** `actor_id`
  2. **boolean** `success`
  
- Example:
  - URL: 
  - Response:

- Errors:
  - 401 : un authorized "in valid token"
  - 422 : un processable "missing attribute"
  - 400 : invalid body

### 3. PATCH /actors/<actor_id>

Patch existing actor

- Body:
  - **string** `name` 
  - **integer** `age` 
  - **string** `gender`
- Requires permission: `patch:actors`
- Returns: 
  1. **integer** `actor_id`
  2. **boolean** `success`
  3. **list** `actors`:
      - **integer** `id`
      - **string** `name`
      - **string** `gender`
      - **integer** `age`

- Example:
  - URL: 
  - Response:

- Errors:
  - 404 : actor id doesn't exists
  - 400 : invalid body or actor_id
  - 401 : un authorized "in valid token"


### 4. DELETE /actors/<actor_id>

Delete existing actor

- Requires permission: `delete:actors`
- Returns: 
  1. **integer** `actor_id`
  2. **boolean** `success`

- Example:
  - URL: 
  - Response:

- Errors:
  - 404 : actor id doesn't exists
  - 400 : invalid actor_id
  - 401 : un authorized "in valid token"

### 5. GET /movies

Get movies page.

- Request Arguments: 
    - **integer** `page` (optional, 10 movies per page, defaults to `1`)
- Requires permission: `get:movies`
- Returns: 
  1. **list** `movies`:
      - **integer** `id`
      - **string** `name`
      - **date** `release_date`
  2. **boolean** `success`
  3. **integer** `total_movies`
- Example:
  - URL: 
  - Response:
- Errors:
  - 404 : invalid page number
  - 401 : un authorized

### 6. POST /movies

Post new movie.

- Body:
  - **string** `title`
  - **date** `release_date`
- Requires permission: `post:movies`
- Returns: 
  1. **integer** `movie_id`
  2. **boolean** `success`
- Example:
  - URL: 
  - Response:

- Errors:
  - 401 : un authorized "in valid token"
  - 422 : un processable "missing attribute"
  - 400 : invalid body
  
### 7. PATCH /movies/<movie_id>

Patch existing movie.

- Request Arguments: **integer** `movie_id`
- Body
  - **string** `title` 
  - **date** `release_date` 
- Requires permission: `patch:movies`
- Returns: 
  1. **integer** `movie_id`
  2. **boolean** `success`
  3. **list** `movies`:
        - **integer** `id`
        - **string** `title` 
        - **date** `release_date` 
- Example:
  - URL: 
  - Response:

- Errors:
  - 404 : actor id doesn't exists
  - 400 : invalid body or movie_id
  - 401 : un authorized "in valid token"

### 8. DELETE /movies/<movie_id>

Delete existing movie.

- Request Arguments: **integer** `movie_id`
- Requires permission: `delete:movies`
- Returns: 
  1. **integer** `movie_id`
  2. **boolean** `success`

- Example:
  - URL: 
  - Response:

- Errors:
  - 404 : actor id doesn't exists
  - 400 : invalid movie_id
  - 401 : un authorized "in valid token"

