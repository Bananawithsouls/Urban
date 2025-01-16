from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0)  # возраст не может быть отрицательным

class UpdateUser(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0)  # возраст не может быть отрицательным

class User(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

    class Config:
        orm_mode = True  # Позволяет Pydantic работать с SQLAlchemy моделями
