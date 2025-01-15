from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Создаем объект Jinja2Templates и указываем папку с шаблонами
templates = Jinja2Templates(directory="templates")

# Пустой список пользователей
users = []


# Определение модели User
class User(BaseModel):
    id: int
    username: str
    age: int


# Модель для обновления пользователя
class UserUpdate(BaseModel):
    username: str
    age: int


# GET запрос для отображения списка пользователей
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# GET запрос для получения конкретного пользователя по ID
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int = Path(..., ge=1)):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос для обновления пользователя
@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int = Path(..., ge=1), user_update=UserUpdate):
    for user in users:
        if user.id == user_id:
            user.username = user_update.username
            user.age = user_update.age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int = Path(..., ge=1)):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")


@app.on_event("startup")
async def startup_event():
    await create_user("UrbanUser", 24)
    await create_user("UrbanTest", 22)
    await create_user("Capybara", 60)
