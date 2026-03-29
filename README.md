# EDU-Track

A Python command-line application for tracking, managing, and monitoring student learning progress.
Works **fully offline** — all data is stored locally as JSON files (no internet or database required).

## Requirements

- Python 3.8+
- No external packages (stdlib only: `json`, `hashlib`, `subprocess`, `tempfile`, `uuid`, `collections`)

## How to Run

```bash
python main.py
```

## User Flow

```
Launch → Welcome Screen
         ├── 1. Sign Up  (name, email, password, program)
         └── 2. Log In   (email or username + password)
                  │
                  ▼
            COURSE HUB
            Commands: run <course_name> | add | list | exit
                  │
                  ▼
            COURSE DASHBOARD  (after run <course_name>)
            1. View Timeline       → last / this / next week entries
            2. Add Note            → vim / vi / nano / built-in (saved with timestamp)
            3. Add Goal            → name, start date, due date
            4. Add Activity        → name, programming language, description
            5. Language Statistics → % bar chart, favourite language
            0. Back to Course Hub
```

## Project Structure

```
edu_track/
├── main.py                     # Entry point — run this
├── README.md
├── data/                       # Auto-created — JSON storage
│   ├── users.json
│   └── courses.json
└── edutrack/
    ├── __init__.py
    ├── storage.py              # JSON load/save helpers
    ├── models.py               # OOP classes: UserStore, CourseStore
    ├── display.py              # ANSI colors, headers, menus
    ├── auth.py                 # Welcome screen, Sign Up, Log In
    ├── course_hub.py           # Main post-auth screen
    └── course_dashboard.py     # Timeline, Notes, Goals, Activities, Stats
```

## Tech Stack

| Technology | Details |
|---|---|
| Language | Python 3 |
| Storage | JSON files (offline, no SQL) |
| OOP | `UserStore`, `CourseStore` classes with encapsulated methods |
| CLI | ANSI-colored terminal interface |
| Editors | vim / vi / nano / built-in fallback for session notes |

## Features

- User authentication (sign up / log in) with SHA-256 hashed passwords
- Course Hub with command-based navigation (`run <course_name>`)
- Weekly EDU-Timeline — add and view entries for last / this / next week
- Session Notes — write with vim, vi, nano, or built-in editor; saved with timestamp
- Goals — per course, with start date and due date
- Activity logging — tagged by programming language
- Language Statistics — usage % bar chart and favourite language detection
- Input validation throughout
- Fully offline — all data stored in `data/` as JSON

## Universal Commands

| Command | Action |
|---|---|
| `run <course_name>` | Open a course |
| `add` | Add a new course |
| `list` | List all your courses |
| `exit` | Quit EDU-Track |
| `back` or `0` | Return to previous menu |
