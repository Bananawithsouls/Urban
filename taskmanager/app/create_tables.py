from backend.db import engine
from models import User, Task
from backend.db import Base

Base.metadata.create_all(bind=engine)

print("SQL для User:")
print(User.__table__)

print("SQL для Task:")
print(Task.__table__)
