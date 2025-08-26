from sqlmodel import SQLModel, Field, create_engine, Session, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

sqlite_file_name = "users.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}",echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)