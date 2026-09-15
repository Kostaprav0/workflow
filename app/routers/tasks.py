from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate

router = APIRouter()

tasks = [
    {
        "id": 1,
        "title": "Изучить FastAPI",
        "description": "Разобраться с API",
        "completed": False,
    }
]

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "completed": False,
    }

    tasks.append(new_task)

    return new_task

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
def delete_task(task_id, int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")