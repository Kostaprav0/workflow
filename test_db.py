from app.database import engine
from app.models.task import Base
from app.database import SessionLocal
from app.models.task import Task


Base.metadata.create_all(engine)

task = Task(
    title= "Плохое обучение",
    description = "Я устал от того что ты просиш самостоятельно чтото придумать не показывая до этого примера как правильно чтото должно быть сделано",
    completed = True
)
print(task.title)
print(task.description)
print(task.completed)

with SessionLocal() as session:
    session.add(task)
    session.commit()