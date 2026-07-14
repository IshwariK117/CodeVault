# CodeVault

CodeVault is a coding problem tracker built with FastAPI.

The motto of this project is simple:

> Track every problem you solve, understand your progress, and build better coding habits.

This project is inspired by coding platforms like LeetCode, Codeforces, HackerRank, GeeksforGeeks, and similar sites. The goal is to create one place where a user can store and review important information about their coding practice.

## What CodeVault Will Track

CodeVault can grow into a tracker for things like:

- Problems solved
- Problem title and platform
- Difficulty level, such as easy, medium, or hard
- Topic or tag, such as arrays, strings, dynamic programming, graphs, or SQL
- Time taken to solve a problem
- Solution status, such as solved, attempted, or needs revision
- Notes about the approach
- Code solution link or saved solution
- Date solved
- Revision count
- Overall progress statistics

## Example Use Case

A user solves a LeetCode problem called `Two Sum`.

In CodeVault, they can save:

- Platform: LeetCode
- Problem: Two Sum
- Difficulty: Easy
- Tags: Array, Hash Map
- Time taken: 20 minutes
- Status: Solved
- Notes: Used a dictionary to store numbers and indexes
- Date solved: 2026-07-14

Later, the user can check how many problems they solved, which topics are weak, how much time they usually take, and which problems need revision.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

Later, this project can also use:

- SQLite or PostgreSQL for database storage
- SQLAlchemy or SQLModel for database models
- JWT authentication for users
- React or another frontend framework for the user interface

## Important Files

```text
CodeVault/
├── README.md
└── app/
    ├── __init__.py
    └── main.py
```

### `app/main.py`

This is the main entry point of the FastAPI application.

Current code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
```

What this means:

- `FastAPI()` creates the web application.
- `@app.get("/")` creates a route for the home page.
- When someone opens `/`, the API returns a JSON response.

### `app/__init__.py`

This file tells Python that `app` is a package.

It can be empty, but it is still useful because it allows imports like:

```python
from app.main import app
```

### `README.md`

This file explains the project idea, setup steps, folder structure, and future plan.

## How To Run The Project

From the root folder of this repository, go inside the `CodeVault` folder:

```bash
cd CodeVault
```

Then run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open this URL in your browser:

```text
http://127.0.0.1:8000
```

You should see:

```json
{
  "message": "Hello FastAPI"
}
```

## API Docs

FastAPI automatically creates API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

This page lets you test API endpoints from the browser.

## Beginner-Friendly Feature Plan

### Step 1: Basic FastAPI App

- Create the FastAPI app
- Add a home route
- Learn how to run the server
- Open the API docs

### Step 2: Problem Data Model

Create a model for a coding problem.

Example fields:

- `id`
- `title`
- `platform`
- `difficulty`
- `tags`
- `status`
- `time_taken_minutes`
- `notes`
- `date_solved`

### Step 3: Basic API Routes

Add routes like:

- `GET /problems` - show all tracked problems
- `POST /problems` - add a new problem
- `GET /problems/{problem_id}` - show one problem
- `PUT /problems/{problem_id}` - update a problem
- `DELETE /problems/{problem_id}` - delete a problem

### Step 4: Store Data

Start simple with in-memory data.

Later, move to a real database like SQLite or PostgreSQL.

### Step 5: Progress Stats

Add stats like:

- Total solved problems
- Problems solved by difficulty
- Problems solved by platform
- Average time taken
- Most practiced topic
- Problems marked for revision

## Future Ideas

- User login and signup
- Dashboard page
- Streak tracking
- Calendar view
- Topic-wise progress chart
- Import solved problems from platforms
- Search and filter problems
- Revision reminders
- Public profile or shareable progress page

## Project Status

This project is currently in the beginner setup stage.

The first goal is to build a clean FastAPI backend. After that, database support, authentication, statistics, and frontend features can be added step by step.
