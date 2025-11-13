"""
===========================================================
                 PYTHON & GIT QUICK TEMPLATE
===========================================================
  Includes: Main Entry, Git Commands, Virtual Env Setup,
  File/JSON Handling, Class Template, Error Handling
===========================================================
"""

# ╔══════════════════════════════════════════════════════╗
# ║   MAIN ENTRY POINT                                   ║
# ╚══════════════════════════════════════════════════════╝

if __name__ == "__main__":
    print("Run the program here!")


# ╔══════════════════════════════════════════════════════╗
# ║   BASIC GIT COMMANDS (REFERENCE)                     ║
# ╚══════════════════════════════════════════════════════╝
"""
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main

git init                        # New repo
git clone <url>                 # Clone from remote
git status                      # View changes
git log --oneline               # Condensed history
git remote -v                   # Show remote URL

git add <file>                  # Stage file
git add .                       # Stage all
git commit -m "message"         # Commit changes

git push -u origin main         # First push
git push                        # Next pushes

git pull                        # Fetch + merge
git fetch                       # Fetch only

git branch                      # List branches
git switch -c <branch>          # Create + switch
git switch <branch>             # Switch only
"""


# ╔══════════════════════════════════════════════════════╗
# ║   GIT BASH ENVIRONMENT SETUP (WINDOWS)               ║
# ╚══════════════════════════════════════════════════════╝
"""
python -m pip install --upgrade pip      # Update pip
python -m venv venv                      # Create venv
source venv/Scripts/activate             # Activate venv
deactivate                               # Exit venv
pip install -r requirements.txt          # Install deps
pip freeze > requirements.txt            # Save deps
"""


# ╔══════════════════════════════════════════════════════╗
# ║   JSON HANDLING TEMPLATE                             ║
# ╚══════════════════════════════════════════════════════╝

import json

data = {"a": 1, "b": 2}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)


# ╔══════════════════════════════════════════════════════╗
# ║   FILE HANDLING TEMPLATE                             ║
# ╚══════════════════════════════════════════════════════╝

try:
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")


# ╔══════════════════════════════════════════════════════╗
# ║   CLASS TEMPLATE                                     ║
# ╚══════════════════════════════════════════════════════╝


class MyClass:
    def __init__(self, attr1, attr2, attr3, attr4, attr5, attr6, attr7, attr8):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4
        self.attr5 = attr5
        self.attr6 = attr6
        self.attr7 = attr7
        self.attr8 = attr8

class MyClass:
    def __init__(self, *args):
        for i, value in enumerate(args, start=1):
            setattr(self, f"attr{i}", value)

    def __str__(self):
        return f"MyClass({', '.join(str(v) for v in self.__dict__.values())})"


# Optional Inheritance Example
class Parent:
    def __init__(self, x):
        self.x = x


class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


# ╔══════════════════════════════════════════════════════╗
# ║   ERROR HANDLING (COMMON EXCEPTIONS)                 ║
# ╚══════════════════════════════════════════════════════╝

try:
    # Code that might raise an exception
    print("Enter your code here")

except (TypeError, ValueError, KeyError) as e:
    print(f"Handled known error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")



# +========================+
# | ERROR HANDELING custom |
# +========================+

try:
    # Code that might raise an exception
    print("Enter your code here")

# Catch any exception
except Exception as e:
    print(f"Unexpected error: {e}")

# Common Python exceptions individually
except AttributeError as e:
    print(f"AttributeError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
except KeyError as e:
    print(f"KeyError: {e}")
except NameError as e:
    print(f"NameError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except IOError as e:
    print(f"IOError: {e}")
except ImportError as e:
    print(f"ImportError: {e}")
except StopIteration as e:
    print(f"StopIteration: {e}")
except AssertionError as e:
    print(f"AssertionError: {e}")
except MemoryError as e:
    print(f"MemoryError: {e}")
except OverflowError as e:
    print(f"OverflowError: {e}")




"""
============================================================
        🚀 FASTAPI + GIT + ENV QUICK SETUP TEMPLATE
============================================================

📁 PROJECT STRUCTURE
------------------------------------------------------------
your_project/
│
├── venv/                   # Virtual environment (auto-created)
├── app/
│   ├── __init__.py
│   └── main.py              # Your FastAPI entry file
│
├── requirements.txt         # Dependencies
└── .gitignore               # Ignored files for Git


============================================================
1️⃣ ENVIRONMENT SETUP (Git Bash)
============================================================

# Create project folder
mkdir your_project && cd your_project

# Initialize Git repository
git init

# Create virtual environment
python -m venv venv

# Activate environment (Git Bash)
source venv/Scripts/activate

# Upgrade pip
python -m pip install --upgrade pip


============================================================
2️⃣ INSTALL FASTAPI + UVICORN
============================================================

# Install dependencies
pip install fastapi uvicorn

# (Optional: add extra tools)
pip install python-dotenv requests

# Save dependencies
pip freeze > requirements.txt


============================================================
3️⃣ CREATE FASTAPI APP
============================================================

# File: app/main.py
------------------------------------------------------------
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI + Git!"}


============================================================
4️⃣ RUN THE APP
============================================================

# Run with uvicorn
uvicorn app.main:app --reload

# Then open in browser:
http://127.0.0.1:8000

# Or test the interactive docs:
http://127.0.0.1:8000/docs


============================================================
5️⃣ BASIC GIT WORKFLOW
============================================================

# Configure Git (first time)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main

# Stage & commit
git add .
git commit -m "Initial FastAPI setup"

# Add remote & push (if you have GitHub repo)
git remote add origin <your_repo_url>
git push -u origin main


============================================================
6️⃣ .GITIGNORE TEMPLATE
============================================================
# Python / venv / cache
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.env

# OS / Editor junk
.DS_Store
*.log
.idea/
.vscode/


============================================================
7️⃣ TESTING THE ENDPOINT
============================================================
# Option 1: Using browser
→ visit http://127.0.0.1:8000/

# Option 2: Using curl (Git Bash)
curl http://127.0.0.1:8000/

# Option 3: Using Python requests
------------------------------------------------------------
import requests
print(requests.get("http://127.0.0.1:8000/").json())
------------------------------------------------------------


============================================================
✅ READY TO BUILD
============================================================
- Add more routes in `app/main.py`
- Organize code into modules (routers, models, services)
- Integrate SQLite, PostgreSQL, or MongoDB later
- Deploy with Uvicorn + Gunicorn (or Docker)
============================================================
"""