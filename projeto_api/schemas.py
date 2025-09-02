import strawberry
from sqlmodel import Session, select
from typing import List
from models import User, engine

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    age: int

    @classmethod
    def from_orm(cls, user: User) -> "UserType":
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age
        )


@strawberry.type
class Query:
    @strawberry.field
    def list_users(self) -> List[UserType]:
        print("Executando list_users...")
        with Session(engine) as s:
            users = s.exec(select(User)).all()
            print(f"Usuários encontrados: {users}")
            return [UserType.from_orm(user) for user in users]

    
schema = strawberry.Schema(query=Query)