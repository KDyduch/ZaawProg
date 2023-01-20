from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def zadzialaj():
    return RedirectResponse("/docs")
