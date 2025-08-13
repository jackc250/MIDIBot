# Python MIDI Composer

A lightweight, programmable MIDI composition tool for Python.

---

**NOTICE** You must use your own API Key. 
- Set one up at https://platform.openai.com/
- Once your API Key is set up, the errors in main.py should go away.

## Features
- As of now generated a small MIDI file in the key of C major with melody and percussion.
- Will be working on more features (suggest some if you would like) in the future.

## Quickstart

```bash
# 1) Create & activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) (Optional) Configure AI features
cp .env.example .env
# then edit .env to set OPENAI_API_KEY and MODEL if desired
```

## Project structure (suggested)

```text
midi-composer/
├── main.py
├── composer/
│   ├── __init__.py
│   ├── scales.py
│   ├── chords.py
│   ├── rhythm.py
│   └── writer.py
├── outputs/
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Common development tasks

- **Run tests** (if you add pytest):
  ```bash
  pytest -q
  ```

- **Format & lint** (optional but recommended):
  ```bash
  pip install ruff black
  ruff check . && black .
  ```

## Troubleshooting

If `python-rtmidi` fails to build and you don’t need realtime I/O, comment it out in `requirements.txt`.

If `git push` fails, see the “Git Push Troubleshooting” in this README or ask for help with your exact error text.

## License
MIT (or your choice)

---
