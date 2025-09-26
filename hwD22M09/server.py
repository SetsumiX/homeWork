from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from dbSystem import QuotesDB

app = FastAPI()
db = QuotesDB()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    text_author = db.take_rand_quote()

    return templates.TemplateResponse(
        "index.html",
        {"request": request,
         "text":text_author[0][0], "author":text_author[0][1]}
    )

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="127.0.0.1", port=8000,
        reload=True, reload_dirs=["./static", "./templates"]
    )