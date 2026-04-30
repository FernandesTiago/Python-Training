# Python-Training
![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)
I'm learning Python and this repo tracks everything I've built along the way. All code is hand-written — the only thing that's ever AI-generated is the exercise prompts in the `Claude/` folder.

## Currently learning
**FastAPI** — learning HTTP basics and REST API fundamentals before building a real project.

## What I've learned
### Python basics
- `input()` / `print()`, f-strings, basic types (`int`, `float`, `str`, `bool`)
- String methods: `.strip()`, `.title()`, `.upper()`, `.isalpha()`, `.isnumeric()`, `.isdigit()`, `.split()`, `.replace()`, `.join()`
- Arithmetic, integer/float casting, exponents, roots

### Control flow
- `if / elif / else`, ternary expressions
- `while`, `for` with `range`, `break`, `continue`
- `try / except / else / finally` for input validation and file handling

### Functions
- `def`, positional and default arguments
- `return`, docstrings
- `global`
- `lambda` with `sorted(..., key=...)`

### Data structures
- Lists: `.append()`, `.pop()`, `.sort()`, `sorted()`, `min` / `max` / `index`, `enumerate()`
- Dicts: `.update()`, `.get()` with defaults, `del`, nested dicts, lists of dicts

### File I/O
- `open()` with `r` / `w` / `a` modes, `readlines()`, `write()`
- `pathlib.Path(__file__).parent` so scripts always read/write next to themselves
- Handling `FileNotFoundError`

### JSON
- `json.dump` / `json.load`
- Handling `JSONDecodeError` alongside `FileNotFoundError`
- Persisting class instances by converting them to dicts

### OOP
- `class`, `__init__`, `__str__`
- Inheritance with `super().__init__(...)`
- Methods that mutate instance state (add / reset / delete points, etc.)
- Multi-class systems with composition (one class owning and using another)
- Role-based access control logic inside a Menu class

### Security
- Password hashing with `bcrypt` — `hashpw`, `gensalt`, `checkpw`
- Never storing plain-text passwords
- Generic error messages to prevent username enumeration

### SQL (SQLite)
- `sqlite3.connect()`, cursors, `commit()`, `close()`
- `CREATE TABLE IF NOT EXISTS`
- `INSERT` / `UPDATE` / `DELETE` / `SELECT` with parameterized queries
- `fetchall()` / `fetchone()` to read rows
- Multiple independent tables in the same database

### Standard library
- `random` (`randint`), `math` (`sqrt`), `datetime` / `date.today()`, `time.sleep`, `pathlib`, `json`, `sqlite3`, `os`, `bcrypt`

## Repo structure
- **`video_course/`** — exercises from [Curso em Vídeo](https://www.cursoemvideo.com/) by Gustavo Guanabara. Modules 1–3 completed.
- **`Claude/exercises_01-20/`** and **`Claude/exercises_21-40/`** — exercises *proposed* by Claude, *coded* by me. Claude picks the topic based on what I'm currently learning and mixes in things I already know, so each exercise reinforces the new concept while reviewing older ones.
- **`Claude/lessons/`** — lesson-style scripts where a new topic is introduced before I start exercises on it.
- **`Claude/Tests/`** — mini self-assessments.

## Highlights
**ex_claude_026 — Login and Permissions System** was the most complete exercise so far. Three classes, two independent SQLite tables, bcrypt password hashing, and role-based access control — all in a single terminal application. Admin users get full CRUD access; common users are read-only. Took a full session to debug and build, and genuinely fun to get working.

## Up next
- **Stealth Network Monitor** — a Raspberry Pi project exposing a REST API built with FastAPI. Scans the local network periodically using Scapy, persists device history in SQLite, and serves the data through authenticated endpoints. Combines everything learned so far: OOP, SQLite, authentication, and adds FastAPI + background tasks + networking.
