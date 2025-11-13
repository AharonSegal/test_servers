from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class NameData(BaseModel):
    name: str

@router.get("/test")
def read_test():
    print("basic conection test -> recived hi")
    return {"msg": "hi from test"}

@router.post("/save_name/")
def save_name_to_file(data: NameData):
    """
    Receives a name and saves it to a text file.
    """
    with open("names.txt", "a") as f: 
        f.write(data.name + "\n")
    
    print("saved name")
    return {"message": f"Name '{data.name}' saved successfully."}

@router.get("/get_name/")
def get_names_from_file():
    """
    Retrieves all names from the text file.
    """
    with open("names.txt", "r") as f:
        names = [line.strip() for line in f if line.strip()]

    print("got name")
    return {"names": names}