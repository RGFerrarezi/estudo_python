from sqlmodel import SQLModel, Field, create_engine
from pydantic import EmailStr, constr, conint

class User(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

class UserCreate(SQLModel):
    name: constr(min_length=1)
    email: EmailStr
    age: conint(gt=0,lt=120)

class UserRead(SQLModel):
    id: int
    name: str
    email: str
    age: int

sqlite_file_name = "user.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}",echo = True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)