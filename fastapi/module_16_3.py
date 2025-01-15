from fastapi import FastAPI, Path, HTTPException
from typing import Dict, Annotated

app = FastAPI()
# Словарь
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(
            min_length=5, max_length=20,
            description="Имя пользователя",
            example="UrbanUser"
        )],
        age: Annotated[int, Path(
            ge=1, le=120,
            description="Возраст пользователя",
            example=24
        )]
):
    # Определяем новый id на основе максимального ключа
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(
            ge=1,
            description="ID пользователя для обновления",
            example=1
        )],
        username: Annotated[str, Path(
            min_length=5, max_length=20,
            description="Новое имя пользователя",
            example="UrbanProfi"
        )],
        age: Annotated[int, Path(
            ge=1, le=120,
            description="Новый возраст пользователя",
            example=28
        )]
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(
            ge=1,
            description="ID пользователя для удаления",
            example=2
        )]
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[str(user_id)]
    return f"User {user_id} has been deleted"
