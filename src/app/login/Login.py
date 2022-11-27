
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from datetime import datetime
from typing import List
from logging import currentframe
from os import access, stat
from pydantic.networks import url_regex
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()

class Settings(BaseModel):
    authjwt_secret_key : str = 's7dlti4ltfc80drrly5fetx6gu8gp6qrwcq7w1xb8avuvrrjbfcf97egajhw2l5y'

@AuthJWT.load_config
def get_config():
    return Settings()

class User(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "john",
                "email": "john@gmail.com",
                "password": "password"
            }
        }

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "john",
                "password": "password"
            }
        }

users = []

@app.post('/signup', status_code=201)
def create_user(user: User):
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }

    users.append(new_user)

    return new_user

@app.post('/login')
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    for u in users:
        if (u["username"] == user.username) and (u["password"] == user.password):
            access_token = Authorize.create_access_token(subject=user.username)
            refresh_token = Authorize.create_refresh_token(subject=user.username)

            return {"access_token": access_token, "refresh_token": refresh_token}

        raise HTTPException(status_code='401', detail="Invalid username or password")

@app.get('/time')
def current_time(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    time = datetime.now()
    current_user = Authorize.get_jwt_subject()

    return {
        "current_user": current_user,
        "time": time.strftime("%H:%M:%S")
    }

