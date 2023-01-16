from fastapi import FastAPI
from starlette.requests import Request
from mangum import Mangum

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str
    active: bool = True
    admin: bool = False

app = FastAPI()

@app.get("/users")
async def get_user(request: Request):
    print("\n\n\nentre get users->")
    print(request.scope["aws.event"])
    return {"message": "Hello World!"}

@app.post("/users")
async def create_user(request: Request, user: User):
    print("\nPOST USER \n ")
    print(request.scope["aws.event"])
    print("user: ", user)
    return {"message": "Hello desde el post!"}

lambda_handler = Mangum(app)
