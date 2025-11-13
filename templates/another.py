from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI(title="Basic FastAPI Example")

# -----------------------------
#  POST Request Body Model
# -----------------------------
class TextInput(BaseModel):
    text: str


# -----------------------------
#  Utility: Save result to JSON
# -----------------------------
def save_to_json(filename: str, data: dict):
    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return filepath


# -----------------------------
#  GET ROUTES (Simple Examples)
# -----------------------------

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI demo!"}


@app.get("/reverse/{s}")
def reverse_string(s: str):
    """Return the reversed string"""
    return {"original": s, "reversed": s[::-1]}


@app.get("/mod/{a}/{b}")
def modulus(a: int, b: int):
    """Return a mod b"""
    if b == 0:
        return {"error": "Division by zero not allowed"}
    return {"a": a, "b": b, "a mod b": a % b}


# -----------------------------
#  POST ROUTES (With JSON Output)
# -----------------------------

@app.post("/remove_vowels/")
def remove_vowels(data: TextInput):
    """Remove vowels and save result to JSON"""
    vowels = "aeiouAEIOU"
    result = "".join([ch for ch in data.text if ch not in vowels])
    output = {"original": data.text, "without_vowels": result}
    path = save_to_json("remove_vowels.json", output)
    return {"result": output, "saved_to": path}


@app.post("/letter_count/")
def count_letters(data: TextInput):
    """Count occurrences of each letter and save result"""
    counts = {}
    for ch in data.text:
        if ch.isalpha():
            counts[ch.lower()] = counts.get(ch.lower(), 0) + 1
    output = {"original": data.text, "letter_counts": counts}
    path = save_to_json("letter_counts.json", output)
    return {"result": output, "saved_to": path}


@app.post("/every_third_removed/")
def remove_every_third(data: TextInput):
    """Remove every third character and save result"""
    result = "".join(ch for i, ch in enumerate(data.text, 1) if i % 3 != 0)
    output = {"original": data.text, "every_third_removed": result}
    path = save_to_json("every_third_removed.json", output)
    return {"result": output, "saved_to": path}
