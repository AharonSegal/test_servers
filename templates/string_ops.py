# string_ops.py
from fastapi import APIRouter
from json_converter import write_to_json_file # Import the helper function

# Initialize the router
router = APIRouter()

# -----------------------------
# GET endpoints (Access via /string/...)
# -----------------------------

@router.get("/reverse/{s}")
def reverse_str(s: str):
    body = {
        "original": s,
        "reversed": s[::-1]
    }
    return body

@router.get("/upper/{s}")
def to_upper(s: str):
    body = {
        "original": s,
        "to_upper": s.upper()
    }
    return body


# -----------------------------
# POST endpoints (Access via /string/...)
# -----------------------------

@router.post("/remove_vowels")
def remove_vowels(data: dict):
    s = data.get("text", "")
    vowels = ["o","u","i","e","a", "O", "U", "I", "E", "A"]
    removed = "".join(char for char in s if char not in vowels)
    
    result = {
        "original": s,
        "remove_vowels": removed
    }
    
    # Write the result to a file
    filename = write_to_json_file(result, "remove_vowels")
    result["file_saved_as"] = filename
    return result

@router.post("/remove_every_third")
def remove_every_third(data: dict):
    s = data.get("text", "")
    removed = "".join(char for i, char in enumerate(s) if i % 3 != 0)
    
    result = {
        "original": s,
        "remove_every_third": removed
    }
    
    # Write the result to a file
    filename = write_to_json_file(result, "remove_every_third")
    result["file_saved_as"] = filename
    return result

@router.post("/letter_counts")
def letter_counts_map(data: dict):
    s = data.get("text", "")
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    result = {
        "original": s,
        "counts": counts
    }
    
    # Write the result to a file
    filename = write_to_json_file(result, "letter_counts")
    result["file_saved_as"] = filename
    return result