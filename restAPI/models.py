from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import EmailStr, constr, conint

#Modelo principal
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

#Modelo para entrada de dados
class UserCreate(SQLModel):
    name: constr(min_length=1) # type: ignore # garantindo que o nome não seja vazio
    email: EmailStr # garantindo que o email seja válido
    age: conint(gt=0, lt=120) # type: ignore # garantindo que a idade esteja entre 1 e 119

#Modelo para saída de dados:
class UserRead(SQLModel):
    id: int
    name: str
    email: str
    age: int

#Configuração do banco de dados
sqlite_file_name = "users.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}",echo=True)

#Criar o banco de dados e as tabelas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)