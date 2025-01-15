from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Главная страница"


@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(
        user_id: Annotated[int, Path(
            ge=1, le=100,  # Ограничение по значению
            description="Enter User ID",  # Описание
            example=1  # Пример
        )]
):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}", response_class=HTMLResponse)
async def read_user_info(
        username: Annotated[str, Path(
            min_length=5, max_length=20,  # Ограничение по длине
            description="Enter username",  # Описание
            example="UrbanUser"  # Пример
        )],
        age: Annotated[int, Path(
            ge=18, le=120,  # Ограничение по значению
            description="Enter age",  # Описание
            example=24  # Пример
        )]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
