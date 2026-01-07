from fastapi import FastAPI,Header
from pydantic import BaseModel
import bcrypt
import json
import os
from jose import jwt ,JWTError
from datetime import  datetime,timedelta

app = FastAPI()

USER_FILE = "users_info.json"
SECRET_KEY = "Invoice-Project-Key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30



def load_user():
    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE,"r",encoding="utf-8") as f:
        return json.load(f)

def save_user(users):
    with open(USER_FILE,"w",encoding="utf-8") as f:
        return json.dump(users,f,indent=4)

def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )
    return hashed.decode("utf-8")

def verify_password(password,hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def create_token(username:str):
    payload = {
        "sub" : username,
        "exp" : datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }

    return  jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


def verify_token(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = ALGORITHM)
        return payload["sub"]
    except JWTError:
        return None



class User(BaseModel):
    username : str
    password : str


@app.post("/register")

def register(user:User):
    users = load_user()

    if user.username in users:
        return {"error" : "the user is already exists"}

    users[user.username] = hash_password(user.password)
    save_user(users)

    return {"message": "User registered successfully"}


@app.post("/login")

def login(user:User):
    users = load_user()

    if user.username not in users:
        return {"error" : "User not Found"}

    if not verify_password(user.password,users[user.username]):
        return {"error" : "Wrong Password"}

    token = create_token(user.username)
    return {"token":token}


@app.get("/protected")
def protected_route(authorization = Header(None)):
    if not authorization:
        return {"error":"Token missing"}

    username = verify_token(authorization)

    if not username:
        return {"error": "Invalid token"}

    return {"message" : f"welcome {username}"}


