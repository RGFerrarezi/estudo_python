from fastapi import FastAPI, HTTPException
from models import User, UserRead, UserCreate, create_db_and_tables, engine, Session, select, constr, conint, EmailStr

app = FastAPI()

create_db_and_tables()

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    with Session(engine) as session:
        db_user = User.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
#Read, single, procura por ID e retorna o usuário se houver
@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        result = session.exec(statement).first()
        if result is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado!")
        return result
    
#Read, all, retorna todos os usuários
@app.get("/users/", response_model=list[UserRead])
def read_users():
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement).all()
        return results
    
#Update
@app.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, updated_user: UserCreate):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado!")
        user.name = updated_user.name
        user.email = updated_user.email
        user.age + updated_user.age
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
#Delete
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado!")
        session.delete(user)
        session.commit()
        return{"ok": True, "message": "Usuário deletado com sucesso!"}
