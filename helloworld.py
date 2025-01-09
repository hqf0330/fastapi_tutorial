from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Hello FastAPI"}


@app.get("/helloworld")
async def hello_world():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("helloworld:app")
