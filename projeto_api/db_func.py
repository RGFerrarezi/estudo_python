from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import User, UserCreate, UserRead, engine

router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    db_user = User.from_orm(user)
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

@router.get("/users/",response_model=list[UserRead])
def get_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

@router.post("/users/{user_id}",response_model=UserRead)
def update_user(user_id: int, user: UserCreate):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            setattr(db_user, key, value)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(db_user)
        session.commit()
        return {"ok": True}