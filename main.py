# To Run: uvicorn main:app --reload
from fastapi import FastAPI
from basic import router as basic_router
from cypher import router as cypher_router
from fence import router as fence_router


# Create the main app
app = FastAPI(title="test FastApi")
app.include_router(basic_router)
app.include_router(cypher_router)
app.include_router(fence_router)


