# main.py
from fastapi import FastAPI
from string_ops import router as string_router
from json_converter import router as json_router

# Create the main app
app = FastAPI(title="Modular String and JSON API")

# Include the routers, adding unique prefixes for clear organization
app.include_router(string_router, prefix="/string", tags=["String Operations"])
app.include_router(json_router, prefix="/json", tags=["JSON Converters"])

@app.get("/")
def read_root():
    return {"message": "Welcome! Access /string and /json routes for operations."}

# To Run: uvicorn main:app --reload