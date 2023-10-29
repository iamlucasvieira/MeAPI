from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


def dev():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
