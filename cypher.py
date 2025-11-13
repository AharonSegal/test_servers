from fastapi import Body,APIRouter

router = APIRouter()

#/caesar
@router.post("/caesar")
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