import requests
from flask import Flask, request, redirect, url_for, make_response
from flask import render_template
from models import db, User
from generate_hash import generate_pass_to_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.get('/registry/')
def registration_page():
    context = {'title': 'Регистрация', 'error': 'Заполните все поля и нажмите кнопку: Зарегистрировать'}
    return render_template('sing_up.html', **context)


@app.post('/registry/')
def reg_user():
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    secret = generate_pass_to_hash(first_name, request.form.get('secret'))
    secret_check = generate_pass_to_hash(first_name, request.form.get('secret_check'))
    email = request.form.get('email')
    all_info = [first_name, last_name, secret, secret_check, email]
    try:
        first_name = int(first_name)
        last_name = int(last_name)
        context = {'title': 'Регистрация', 'error': 'Имя и(или) Фамилия не могут содержать цифр!'}
        response = make_response(render_template('sing_up.html', **context))
        return response
    except:
        if '' in all_info:
            context = {'title': 'Регистрация', 'error': 'Необходимо заполнить все поля!'}
            response = make_response(render_template('sing_up.html', **context))
            return response
        elif secret != secret_check:
            context = {'title': 'Регистрация', 'error': 'Введенные пароли не совпадают!'}
            response = make_response(render_template('sing_up.html', **context))
            return response
        else:
            check_user = User.query.filter_by(email=email).all()
            if check_user:
                context = {'title': 'Регистрация', 'error': 'Пользователь с таким Email уже существует!'}
                response = make_response(render_template('sing_up.html', **context))
                return response
            else:
                user = User(first_name=first_name,
                            last_name=last_name,
                            pass_hash=secret,
                            email=email)
                db.session.add(user)
                db.session.commit()
                context = {'title': 'Регистрация', 'error': 'Вы успешно зарегистрированы!'}
                response = make_response(render_template('sing_up.html', **context))
                return response

@app.get('/')
def not_auth():
    context = {'title': 'Авторизация'}
    return render_template('sing_in.html', **context)

@app.post('/auth/')
def auth_post():
    name = request.form.get('username')
    email = request.form.get('email')
    name_cookie = request.cookies.get('name')
    email_cookie = request.cookies.get('email')
    if name != '' and email != '':
        context = {'title': 'Интернет-магазин: Главная', 'username': name, 'email': email}
        response = make_response(render_template('main.html', **context))
        response.set_cookie(key='name', value=name)
        response.set_cookie(key='email', value=email)
        return response
    else:
        if name_cookie is not None and email_cookie is not None:
            context = {'title': 'Интернет-магазин: Главная', 'username': name_cookie, 'email': email_cookie}
            response = make_response(render_template('main.html', **context))
            return response
        return render_template('sing_in.html')

@app.route('/main/')
def main_page():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    if name is None or email is None:
        return redirect(url_for('not_auth'))
    context = {'title': 'Интернет-магазин: Главная', 'username': name, 'email': email}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes_page():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    if name is None or email is None:
        return redirect(url_for('not_auth'))
    context = {'title': 'Интернет-магазин: Одежда', 'username': name}
    return render_template('clothes.html', **context)

@app.route('/footwear/')
def footwear_page():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    if name is None or email is None:
        return redirect(url_for('not_auth'))
    context = {'title': 'Интернет-магазин: Обувь', 'username': name}
    return render_template('footwear.html', **context)

@app.route('/logout/')
def logout():
    context = {'title': 'Авторизация'}
    response = make_response(render_template('sing_in.html', **context))
    response.set_cookie(key='name', expires=0)
    response.set_cookie(key='email', expires=0)
    return response

@app.errorhandler(404)
def error_404(e):
    context = {'title': 'Страница не найдена'}
    return render_template('error_404.html', **context), 404

if __name__=='__main__':
    app.run()
