from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/convert")
async def convertSys(valRub: float = Body(...), convIn: str = Body(...)):
    res = calculate(valRub, convIn)
    return {
        "valRub": valRub,
        "convIn": convIn,
        "result": res
    }

def calculate(value, currency):
    if currency == "USD":
        return value * 0.01196

    elif currency == "EU":
        return value * 0.010237

    elif currency == "UAH":
        return value * 0.4961

    elif currency == "JPY":
        return value * 1.79

    elif currency == "CNY":
        return value * 0.085652

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="127.0.0.1", port=8887,
        reload=True, reload_dirs=["./static","./templates"]
    )