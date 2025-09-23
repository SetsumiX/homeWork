import secrets
import string
from importlib import reload
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="template")

pwd = ""

@app.get("/", response_class=HTMLResponse)
async def show_main_page(request: Request):
    return template.TemplateResponse(
        "./index.html",
        {"request": request}
    )
@app.post("/")
async def get_pass(request: Request):
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(char) for _ in range(10))
    return {"pass": password}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888,
                reload=True, reload_dirs=["./static", "./template"])