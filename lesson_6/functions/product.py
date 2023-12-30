import sqlite3

path_db = 'lesson_6/config/config.db'


def show_all_product():
    """Отображение списка всех продуктов из таблицы products"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM products')
    all_products = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': all_products}}


def get_product(id: int):
    """Возвращает продукт из таблицы products по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'SELECT * FROM products WHERE ID="{id}"')
    product = cur.fetchall()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': product}}


def post_product(name: str, price: str, description: str | None = None):
    """Добавление нового продукта в таблицу products"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(
            f'INSERT INTO products (name, description, price) VALUES ("{name}", "{description}", "{price}");')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'create new row in table products'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/product.py/post_task func'}}


def put_product(id: int, name: str, price: str, description: str | None = None):
    """Изменяет данные о продукте в таблице products по ID"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.execute(f'UPDATE products '
                    f'SET name = "{name}", description = "{description}", price = "{price}" '
                    f'WHERE ID = {id};')
        con.commit()
        cur.close()
        con.close()
        return {'result': True, 'more_details': {'info': 'update row in table products'}}
    except:
        return {'result': False, 'more_details': {'info': 'unknown error in lesson_6/function/product.py/put_task func'}}


def del_product(id: int):
    """Удаляет продукт из таблицы products по ID"""
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute(f'DELETE FROM products '
                f'WHERE ID="{id}"')
    con.commit()
    cur.close()
    con.close()
    return {'result': True, 'more_details': {'info': 'delete row in table products'}}
