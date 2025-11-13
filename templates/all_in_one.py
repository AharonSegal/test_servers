from fastapi import FastAPI
import json
import datetime
# Import Response classes needed for the helper function (not used here, but good practice if you modify helpers)
# from fastapi import Response
# from fastapi.responses import JSONResponse 

# 1. Create the main FastAPI app instance
app = FastAPI(title="String Operations API")

# =============================
# NEW HELPER FUNCTION
# =============================

def write_to_json_file(data: dict, operation_name: str = "result"):
    """
    Writes a Python dictionary to a JSON file with a timestamped filename.
    Returns the filename.
    """
    # Create a unique filename with the operation name and current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{operation_name}_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            # Use json.dump to write the dictionary to the file
            json.dump(data, f, indent=4)
        print(f"Successfully wrote data to {filename}")
        return filename
    except Exception as e:
        print(f"Error writing file {filename}: {e}")
        return None

# -----------------------------
# GET endpoints
# -----------------------------

@app.get("/reverse/{s}")
def reverse_str(s: str):
    """Reverses a given string."""
    body = {
        "original": s,
        "reversed": s[::-1]
    }
    return body

@app.get("/upper/{s}")
def to_upper(s: str):
    """Converts a given string to uppercase."""
    body = {
        "original": s,
        "to_upper": s.upper()
    }
    return body

# -----------------------------
# POST endpoints (MODIFIED to use helper)
# -----------------------------

@app.post("/remove_vowels")
def remove_vowels(data: dict):
    """Removes standard English vowels from a string provided in the POST body."""
    s = data.get("text", "")
    vowels = ["o","u","i","e","a", "O", "U", "I", "E", "A"] 
    removed = "".join(char for char in s if char not in vowels)
    
    result = {
        "original": s,
        "remove_vowels": removed
    }
    
    # CALL HELPER: Write the result to a file
    filename = write_to_json_file(result, "remove_vowels")
    
    # Add the filename to the response body for confirmation
    result["file_saved_as"] = filename
    return result

@app.post("/remove_every_third")
def remove_every_third(data: dict):
    """Removes every third character from a string provided in the POST body."""
    s = data.get("text", "")
    removed = "".join(char for i, char in enumerate(s) if i % 3 != 0)
    
    result = {
        "original": s,
        "remove_every_third": removed
    }
    
    # CALL HELPER: Write the result to a file
    filename = write_to_json_file(result, "remove_every_third")
    
    result["file_saved_as"] = filename
    return result

@app.post("/letter_counts")
def letter_counts_map(data: dict):
    """Computes letter counts for a string provided in the POST body."""
    s = data.get("text", "")
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    result = {
        "original": s,
        "counts": counts
    }
    
    # CALL HELPER: Write the result to a file
    filename = write_to_json_file(result, "letter_counts")
    
    result["file_saved_as"] = filename
    return result

# -----------------------------
# Run with:
# uvicorn string_ops:app --reload
# -----------------------------