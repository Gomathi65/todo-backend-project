from sqlalchemy.orm import Session
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

    update_data = todo_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()
    return db_todo