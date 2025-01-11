import sys
from typing import Optional
from fastapi import FastAPI, Request, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import __version__ as fastapi_version

from config import config

app = FastAPI()

# mount the static file
app.mount(
    config.STATIC_URL, StaticFiles(directory=config.STATIC_DIR), name=config.STATIC_NAME
)

# create the template class
templates = Jinja2Templates(directory=config.TENOKARES_DIR)


@app.get("/server-status", include_in_schema=False)
async def server_status(respose: Response, token: Optional[str]) -> dict:
    if token == "binghu":
        data = {
            "status": "OK",
            "FastAPI Version": fastapi_version,
            "Python Version": sys.version_info,
        }
        return data
    else:
        respose.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "NOT FOUND"}


class Data(BaseModel):
    title: str
    body: str


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"messgae": "welcome to open the page", "name": name}


@app.get("/post")
async def post(request: Request):
    page = Data(title="From Server", body="I am the Subject01")
    data = {"page": page, "author": "binghu", "name": "I am the Test"}
    return templates.TemplateResponse(name="post.html", context=data, request=request)
