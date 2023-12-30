import sqlite3

path_db = 'lesson_6/config/config.db'


def show_all_order():
    """Отображение списка всех заказов из таблицы orders"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM orders')
    all_orders = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': all_orders}}


def get_order(id: int):
    """Возвращает заказ из таблицы orders по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM orders WHERE ID="{id}"')
    order = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': order}}


def post_order(id_user: int, id_product: int, date: str | None = None, status: str | None = None):
    """Создание заказа в таблице orders"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO orders (id_user, id_product, date, status) VALUES ("{id_user}", "{id_product}", "{date}", "{status}");')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'create new row in table orders'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/orders.py/post_task func'}}


def put_order(id: int, id_user: int, id_product: int, date: str | None = None, status: str | None = None):
    """Изменяет заказ в таблице orders по ID"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(f'UPDATE orders '
                    f'SET id_user = "{id_user}", id_product = "{id_product}", date = "{date}", status = "{status}" '
                    f'WHERE ID = {id};')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'update row in table orders'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/orders.py/put_task func'}}


def del_order(id: int):
    """Удаляет заказ из таблицы orders по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'DELETE FROM orders '
                f'WHERE ID="{id}"')
    con.commit()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': 'delete row in table orders'}}
