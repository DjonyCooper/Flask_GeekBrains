from fastapi import FastAPI

from lesson_5.models.item import Item
from lesson_5.functions.task import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/')
@app.get('/tasks/')
async def root():
    """Возвращает список всех задач"""
    logger.info('request GET run complete')
    all_task = show_all_task()
    return all_task


@app.get('/tasks/{id}')
async def task(id: int):
    """Возвращает задачу с указанным идентификатором"""
    logger.info('request GET run complete')
    show_task = get_task(id)
    return show_task


@app.post('/tasks/')
async def create_task(info: Item):
    """Добавляет новую задачу"""
    logger.info('request POST run complete')
    create = post_task(name=info.dict()['name'],
                       description=info.dict()['description'],
                       status=info.dict()['status'])
    return create


@app.put('/tasks/{id}')
async def update_item(info: Item):
    """Обновляет задачу с указанным идентификатором"""
    logger.info(f'request PUT run complete for item id = {info.dict()['id']}')
    update = put_task(id=info.dict()['id'],
                      name=info.dict()['name'],
                      description=info.dict()['description'],
                      status=info.dict()['status'])
    return update


@app.delete('/tasks/{id}')
async def delete_item(task_id: int):
    """Удаляет задачу с указанным идентификатором"""
    logger.info(f'request DELETE run complete for task id = {task_id}')
    delete = del_task(task_id)
    return delete
