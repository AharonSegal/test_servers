# main.py
# To Run: uvicorn main:app --reload
from fastapi import FastAPI, HTTPException, Body, Query
from pydantic import BaseModel
import logging

# Create the main app
app = FastAPI(title="test FastApi")

# Define a Pydantic model for the request body
class NameData(BaseModel):
    name: str

#START - NAME

@app.get("/test")
def read_test():
    print("basic conection test -> recived hi")
    return {"msg": "hi from test"}

@app.post("/save_name/")
def save_name_to_file(data: NameData):
    """
    Receives a name and saves it to a text file.
    """
    with open("names.txt", "a") as f:  # "a" for append mode
        f.write(data.name + "\n")
    
    print("saved name")
    return {"message": f"Name '{data.name}' saved successfully."}

@app.get("/get_name/")
def get_names_from_file():
    """
    Retrieves all names from the text file.
    """
    with open("names.txt", "r") as f:
        names = [line.strip() for line in f if line.strip()]

    print("got name")
    return {"names": names}

#CIPHER
@app.post("/caesar")
def caesar(
    text: str = Body(..., description="The text to encrypt or decrypt"),
    offset: int = Body(..., description="The offset value for the Caesar cipher"),
    mode: str = Body("encrypt", description="Mode: 'encrypt' or 'decrypt'")
):
    """
    Encrypts or decrypts a message using the Caesar cipher.

    Example request body:
    {
        "text": "welcome kodkod",
        "offset": 16,
        "mode": "encrypt"
    }

    Response:
    {
        "encrypt": "muskcdu eudeud"
    }
    """

    result = ""

    # Reverse offset for decryption
    if mode == 'decrypt':
        offset = -offset  

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            result += chr((ord(char) - start + offset) % 26 + start)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            result += chr((ord(char) - start + offset) % 26 + start)
        else:
            result += char

    print("cypher complete")
    return {mode: result}

@app.get("/fence")
def fence(txt):
    even = []
    odd = []
    for i in range(len(txt)):
        if txt[i].isalpha():
            if i % 2 == 0:
                even.append(txt[i])
            else:
                odd.append(txt[i])
    result = ""
    while even:
        result += even.pop(0)
    while odd:
        result += odd.pop(0)

    print("fence complete")
    return {"encrypted_text" : result}