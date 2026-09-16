from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskUpdate

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

@router.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:

            if task_update.title is not None:
                task["title"] = task_update.title

            if task_update.description is not None:
                task["description"] = task_update.description

            if task_update.completed is not None:
                task["completed"] = task_update.completed

            return task

    raise HTTPException(status_code=404, detail="Task not found")