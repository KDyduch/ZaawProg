from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def zadzialaj():
    return RedirectResponse("/docs")
