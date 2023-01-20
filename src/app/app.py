from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def display():
    return RedirectResponse("/docs")
