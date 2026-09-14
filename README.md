# Automating Python Projects with Pip, PyPI & Scripting

A small automation tool that writes a dated log summary to a `.txt` file
using Python's built-in File I/O, with a matching `pytest` suite to verify it.

## Project Structure

```
.
├── lib/
│   ├── __init__.py
│   └── generate_log.py      # writes log entries to log_YYYYMMDD.txt
├── testing/
│   └── test_generate_log.py # pytest suite for generate_log()
├── conftest.py               # marks project root so `lib` imports resolve
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script directly to generate a sample log file:

```
python lib/generate_log.py
```

This writes `log_<today's date>.txt` in the current directory and prints a
confirmation message.

You can also import and call it with your own data:

```python
from lib.generate_log import generate_log

generate_log(["User logged in", "User updated profile", "Report exported"])
```

## Running the Tests

From the project root:

```
pytest testing/ -v
```

The suite checks that `generate_log()`:

- creates the log file
- names it `log_YYYYMMDD.txt`
- writes each list entry as its own line
- raises `ValueError` on non-list input
- still creates an (empty) file when given an empty list

<!--
## Test Results

![Image for passing test](/images/Test.png)
-->

## Dependency Management

Dependencies are tracked in `requirements.txt`. After installing any new
package, regenerate it with:

```
pip freeze > requirements.txt
```

This keeps the environment reproducible for anyone else who clones the repo.
