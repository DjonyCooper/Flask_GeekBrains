import sqlite3

path_db = 'lesson_6/config/config.db'


def show_all_users():
    """Отображение списка всех пользователей из таблицы users"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users')
    all_users = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': all_users}}


def get_user(id: int):
    """Возвращает пользователя из таблицы users по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users WHERE ID="{id}"')
    user = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': user}}


def post_user(name: str, surname: str | None = None, email: str | None = None, secret: str | None = None):
    """Создание пользователя в таблице users"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO users (name, surname, email, secret) VALUES ("{name}", "{surname}", "{email}", "{secret}");')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'create new row in table users'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/users.py/post_task func'}}


def put_user(id: int, name: str, surname: str | None = None, email: str | None = None, secret: str | None = None):
    """Изменяет данные о пользователе в таблице users по ID"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(f'UPDATE users '
                    f'SET name = "{name}", surname = "{surname}", email = "{email}", secret = "{secret}" '
                    f'WHERE ID = {id};')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'update row in table users'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/users.py/put_task func'}}


def del_user(id: int):
    """Удаляет пользователя из таблицы users по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'DELETE FROM users '
                f'WHERE ID="{id}"')
    con.commit()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': 'delete row in table users'}}
