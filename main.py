from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    version="1.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Todo API Running"}


@app.post("/todos")
def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db)
):
    return crud.create_todo(db, todo)


@app.get("/todos")
def get_todos(
    db: Session = Depends(get_db)
):
    return crud.get_todos(db)


@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = crud.get_todo_by_id(db, todo_id)

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    todo: schemas.TodoUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_todo(db, todo_id, todo)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return updated


@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_todo(db, todo_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {"message": "Todo deleted successfully"}