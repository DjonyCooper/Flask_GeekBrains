import sqlite3

path_db = 'lesson_5/config/config.db'


def show_all_task():
    """Отображение списка всех задач из базы данных"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM tasks')
    all_task = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': all_task}}


def get_task(id: int):
    """Возвращает задачу из базы данных по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM tasks WHERE ID="{id}"')
    task = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': task}}


def post_task(name: str, status: str, description: str | None = None):
    """Создание задачи в базе данных"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO tasks (name_task, description_task, status_task) VALUES ("{name}", "{description}", "{status}");')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'create new row in db'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_5/function/product.py/post_task func'}}


def put_task(id: int, name: str, status: str, description: str | None = None):
    """Изменяет задачу в базе данных по ID"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(f'UPDATE tasks '
                    f'SET name_task = "{name}", description_task = "{description}", status_task = "{status}" '
                    f'WHERE ID = {id};')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'update row in db'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_5/function/product.py/put_task func'}}


def del_task(id: int):
    """Удаляет задачу из базы данных по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'DELETE FROM tasks '
                f'WHERE ID="{id}"')
    con.commit()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': 'delete row in db'}}
