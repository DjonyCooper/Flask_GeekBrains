from fastapi import FastAPI

# import all models
from lesson_6.models.users import User
from lesson_6.models.products import Product
from lesson_6.models.orders import Order

# import all function
from lesson_6.functions.users import *
from lesson_6.functions.product import *
from lesson_6.functions.orders import *

app = FastAPI()

@app.get('/')
@app.get('/orders/')
async def root():
    """Возвращает список всех заказов"""
    all_orders = show_all_order()
    return all_orders


@app.get('/users/{id}')
async def user(id: int):
    """Возвращает пользователя с указанным идентификатором"""
    show_user = get_user(id)
    return show_user

@app.get('/products/{id}')
async def product(id: int):
    """Возвращает продукт с указанным идентификатором"""
    show_product = get_product(id)
    return show_product

@app.get('/orders/{id}')
async def order(id: int):
    """Возвращает продукт с указанным идентификатором"""
    show_order = get_order(id)
    return show_order

@app.post('/users/')
async def create_user(info: User):
    """Добавляет нового пользователя"""
    create = post_user(name=info.dict()['name'],
                       surname=info.dict()['surname'],
                       email=info.dict()['email'],
                       secret=info.dict()['secret'])
    return create

@app.post('/products/')
async def create_product(info: Product):
    """Добавляет новый продукт"""
    create = post_product(name=info.dict()['name'],
                          price=info.dict()['price'],
                          description=info.dict()['description'])
    return create

@app.post('/orders/')
async def create_order(info: Order):
    """Добавляет новый заказ"""
    create = post_order(id_user=info.dict()['id_user'],
                        id_product=info.dict()['id_product'],
                        date=info.dict()['date'],
                        status=info.dict()['status'])
    return create

@app.put('/users/{id}')
async def update_user(info: User):
    """Обновляет инфо о пользователе по указанному идентификатору"""
    update = put_user(name=info.dict()['name'],
                      surname=info.dict()['surname'],
                      email=info.dict()['email'],
                      secret=info.dict()['secret'])
    return update

@app.put('/products/{id}')
async def update_product(info: Product):
    """Обновляет инфо о продукте по указанному идентификатору"""
    update = put_product(name=info.dict()['name'],
                         price=info.dict()['price'],
                         description=info.dict()['description'])
    return update

@app.put('/orders/{id}')
async def update_order(info: Order):
    """Обновляет инфо о заказе по указанному идентификатору"""
    update = put_order(id_user=info.dict()['id_user'],
                       id_product=info.dict()['id_product'],
                       date=info.dict()['date'],
                       status=info.dict()['status'])
    return update

@app.delete('/users/{id}')
async def delete_user(id: int):
    """Удаляет пользователя по указанному идентификатору"""
    delete = del_user(id)
    return delete

@app.delete('/products/{id}')
async def delete_product(id: int):
    """Удаляет продукт по указанному идентификатору"""
    delete = del_product(id)
    return delete

@app.delete('/orders/{id}')
async def delete_order(id: int):
    """Удаляет заказ по указанному идентификатору"""
    delete = del_order(id)
    return delete
