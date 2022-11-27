from fastapi import FastAPI
import math
import uvicorn

app = FastAPI()

@app.get('/prime/{number}')
def prime(number: int):
    response = {
        "Number": number,
        "Prime": is_prime(number)
    }
    return response

def is_prime(number: int):
    if(number <= 1):
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i == 0):
            return False
    return True

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000)