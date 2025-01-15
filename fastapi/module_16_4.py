from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пустой список
users = []


# Определение модели User
class User(BaseModel):
    id: int
    username: str
    age: int


# GET запрос для получения всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    return users


# POST запрос для добавления
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    # Определяем новый id на основе максимального id в списке или 1, если список пуст
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос для обновления
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
        user_id: int = Path(..., ge=1),
        username=str,
        age=int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
        user_id: int = Path(..., ge=1)
):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
