"""
===============================
 Pydantic Basic Example
===============================
Pydantic is used to define structured data models
and automatically validate incoming data.

You can run this file directly to see examples.
"""

# -----------------------------
# Import
# -----------------------------
from pydantic import BaseModel, ValidationError
from typing import List, Optional


# -----------------------------
# 1️⃣ Define a Data Model
# -----------------------------
class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None  # optional field
    hobbies: List[str] = []      # list of strings


# -----------------------------
# 2️⃣ Create Valid Data
# -----------------------------
print("✅ Example 1: Valid Data")
user = User(name="Alice", age=25, email="alice@example.com", hobbies=["reading", "coding"])
print(user)
print(user.dict())  # convert to normal Python dict
print()


# -----------------------------
# 3️⃣ Automatic Type Conversion
# -----------------------------
print("✅ Example 2: Type Conversion (string -> int)")
user2 = User(name="Bob", age="30")  # age is a string, Pydantic converts it to int automatically
print(user2)
print()


# -----------------------------
# 4️⃣ Invalid Data Example
# -----------------------------
print("🚫 Example 3: Invalid Data (age is not a number)")
try:
    User(name="Charlie", age="not a number")
except ValidationError as e:
    print("Validation error:")
    print(e)
print()


# -----------------------------
# 5️⃣ Access Fields
# -----------------------------
print("✅ Example 4: Accessing fields")
print("Name:", user.name)
print("First hobby:", user.hobbies[0] if user.hobbies else "none")
print()


# ----------------------------
