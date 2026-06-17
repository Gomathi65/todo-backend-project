from sqlalchemy.orm import Session
from models import Todo
from database import engine , Base

# Create tables
Base.metadata.create_all(bind=engine)

# Insert a sample task
with Session(engine) as session:
    new_task = Todo(title="First Task", completed=False)
    session.add(new_task)
    session.commit()

# Query all tasks
    tasks = session.query(Todo).all()
    print(tasks)
