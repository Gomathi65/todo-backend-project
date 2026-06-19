from sqlalchemy.orm import Session
import models
import schemas


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
from models import Todo
from schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(
        title=todo.title,
        completed=False
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todos(db: Session):
    return db.query(models.Todo).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(
        models.Todo.id == todo_id
    ).first()


def update_todo(
    db: Session,
    todo_id: int,
    todo: schemas.TodoUpdate
):
    db_todo = get_todo_by_id(db, todo_id)
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todos_by_status(db: Session, completed: bool):
    return db.query(Todo).filter(Todo.completed == completed).all()


def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not db_todo:
        return None

    db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)

    update_data = todo_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()

    return True
    return db_todo
