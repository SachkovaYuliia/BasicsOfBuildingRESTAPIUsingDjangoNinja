from .models import Task
from .schemas import TaskCreate, TaskOut
from django.shortcuts import get_object_or_404
from typing import List
from typing import Optional
from ninja import NinjaAPI

ninja_api = NinjaAPI()

# Список всіх завдань
@ninja_api.get("/tasks", response=List[TaskOut])
def list_tasks(request, status: Optional[str] = None, sort_by: Optional[str] = 'created_at'):
    tasks = Task.objects.all()

    if status:
        tasks = tasks.filter(status=status)

    if sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    else:
        tasks = tasks.order_by('created_at')

    return [TaskOut.from_orm(task) for task in tasks]


"""
Створення завдання
"""
@ninja_api.post("/tasks", response=TaskOut)
def create_task(request, task: TaskCreate):
    user = request.user  
    task_obj = Task.objects.create(**task.dict(), user=user)
    return TaskOut.from_orm(task_obj)
"""
Деталі завдання
""" 
@ninja_api.get("/tasks/{task_id}", response=TaskOut)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    return TaskOut.from_orm(task)

"""
Оновлення завдання
"""
@ninja_api.put("/tasks/{task_id}", response=TaskOut)
def update_task(request, task_id: int, task: TaskCreate):
    task_obj = get_object_or_404(Task, id=task_id)
    for attr, value in task.dict().items():
        setattr(task_obj, attr, value)
    task_obj.save()
    return TaskOut.from_orm(task_obj)

"""
Видалення завдання
"""
@ninja_api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"message": "Task deleted successfully"}


