from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import gpt
from db import GLOBAL_REPO

app = FastAPI()
app.mount("/wwwroot", StaticFiles(directory="wwwroot"), name="wwwroot")

templates = Jinja2Templates(directory="wwwroot")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.get("/content/{book}/{page}")
async def content(book: int, page: int):
    data = GLOBAL_REPO.book[book]
    page = data.pages[page]

    print(page)

    return {
        "title": data.name,
        "author": data.author,
        "text": page.content,
        "img": page.img if page.img else gpt.gen_img(page.content)
    }
