from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db_depends import get_db
from typing import List
from models import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter()


@router.get("/", response_model=List[User])
async def all_users(db: Session = Depends(get_db)):
    """
    Возвращает список всех пользователей из базы данных.
    """
    users = db.execute(select(User)).scalars().all()
    return users


@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Возвращает пользователя по его идентификатору.
    Если пользователь не найден, выбрасывает исключение 404.
    """
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    """
    Создает нового пользователя. Проверяет на существование пользователя с таким же username.
    """
    existing_user = db.execute(select(User).where(User.username == user.username)).scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)  # создание slug на основе username
    )

    db.execute(insert(User).values(new_user))
    db.commit()

    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    """
    Обновляет данные пользователя. Если пользователь не найден, выбрасывает исключение 404.
    """
    stmt = update(User).where(User.id == user_id).values(
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age
    )

    result = db.execute(stmt)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")

    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Удаляет пользователя по идентификатору. Если пользователь не найден, выбрасывает исключение 404.
    """
    stmt = delete(User).where(User.id == user_id)

    result = db.execute(stmt)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
