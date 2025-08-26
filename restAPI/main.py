from fastapi import FastAPI, HTTPException
from models import User, create_db_and_tables, engine, Session, select

app = FastAPI()

create_db_and_tables()

@app.post("/users/", response_model=User)
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        results = session.exec(statement).first()
        if results is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado!")
        return results