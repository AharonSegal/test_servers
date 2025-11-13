# json_converter.py
import json
import datetime
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

# Initialize the router
router = APIRouter()

# ---------------------------
# HELPER FUNCTIONS
# ---------------------------

def write_to_json_file(data: dict, operation_name: str = "result"):
    """
    Writes a Python dictionary to a JSON file with a timestamped filename.
    Returns the filename.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{operation_name}_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully wrote data to {filename}")
        return filename
    except Exception as e:
        print(f"Error writing file {filename}: {e}")
        return None

def to_json_response(data):
    """Using built-in FastAPI JSONResponse"""
    return JSONResponse(content=data)

def manual_json_response(data, status_code=200):
    """Manually convert any Python object to JSON using Response"""
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    return Response(content=json_data, media_type="application/json", status_code=status_code)

def compute_letter_counts(s: str):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return {
        "original": s,
        "counts": counts
    }

# ---------------------------
# ENDPOINTS (Access via /json/...)
# ---------------------------

@router.get("/fastapi/{text}")
def endpoint_fastapi(text: str):
    """Returns JSON using built-in JSONResponse."""
    result = compute_letter_counts(text)
    return to_json_response(result)

@router.get("/manual/{text}")
def endpoint_manual(text: str):
    """Returns JSON using manual Response conversion."""
    result = compute_letter_counts(text)
    return manual_json_response(result)