# Python-Training

![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)

I'm learning Python and this repo tracks everything I've built along the way. All code is hand-written — the only thing that's ever AI-generated is the exercise prompts in the `Claude/` folder.

## Currently learning

OOP — building a 3-class system (SQL + menu + hash-encrypted login) on top of the employees database from `lesson_sql.py`.

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

### SQL (SQLite)
- `sqlite3.connect()`, cursors, `commit()`, `close()`
- `CREATE TABLE IF NOT EXISTS`
- `INSERT` / `UPDATE` / `DELETE` / `SELECT` with parameterized queries
- `fetchall()` to read rows

### Standard library
- `random` (`randint`), `math` (`sqrt`), `datetime` / `date.today()`, `time.sleep`, `pathlib`, `json`, `sqlite3`

## Repo structure

- **`video_course/`** — exercises from [Curso em Vídeo](https://www.cursoemvideo.com/) by Gustavo Guanabara. Modules 1–3: I follow the video course and solve the exercises as they come up.
- **`Claude/exercises_01-20/`** and **`Claude/exercises_21-40/`** — exercises *proposed* by Claude, *coded* by me. Claude picks the topic based on what I'm currently learning and mixes in things I already know, so each exercise reinforces the new concept while reviewing older ones.
- **`Claude/lessons/`** — lesson-style scripts where a new topic is introduced before I start exercises on it (currently: SQL).
- **`Claude/Tests/`** — mini self-assessments.
- **`test.py`** — standalone script (phone number formatter).

## Up next

- **3-class system on the employees database**, split as:
  1. **SQL class** — wraps the table structure and CRUD operations (builds on `Claude/lessons/lesson_sql.py`).
  2. **Menu class** — handles the terminal menu and user flow.
  3. **Login class** — user authentication with hash-encrypted passwords, plus role handling: admin (can `INSERT` / `UPDATE` / `DELETE`) vs. common user (read-only `SELECT`).

  Continues the menu work started in `Claude/exercises_21-40/ex_claude_025.py`.
- Continue module 3 of Curso em Vídeo.
