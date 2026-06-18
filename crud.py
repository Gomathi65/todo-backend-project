from sqlalchemy.orm import Session
import models
import schemas


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
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

    if not db_todo:
        return None

    db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)

    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)

    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()

    return True