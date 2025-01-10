from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "hello world"}


@app.get("/greet")
async def greet_name(name: Optional[str] = "User", age: Optional[int] = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


class BookCrearteModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCrearteModel) -> dict:
    return {"title": book_data.title, "author": book_data.author}
