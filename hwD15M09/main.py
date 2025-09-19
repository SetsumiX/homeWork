from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888,
                reload=True, reload_dirs=["./static", "./template"])