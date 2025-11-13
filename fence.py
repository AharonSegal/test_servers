from fastapi import Body,APIRouter
router = APIRouter()

@router.get("/fence")
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