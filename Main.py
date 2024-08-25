from fastapi import FastAPI
from uuid import UUID, uuid4
from FirstUsers import User, Gender
from typing import List

app = FastAPI()

db: List[User] = [
        User(
        id = uuid4(),
        first_name = "Bella",
        last_name = "Ja",
        gender = Gender.female
    )
]


@app.get("/")
async def root():
    return {"Hey!"}

@app.get("/Users")
async def show_users():
    return db;

@app.post("/Users")
async def add_user(user:User):
    db.append(user)
    return user;
