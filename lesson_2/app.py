from flask import Flask, request, redirect, url_for, make_response, Response
from flask import render_template

app = Flask(__name__)

@app.get('/')
def not_auth():
    context = {'title': 'Авторизация'}
    return render_template('auth.html', **context)
@app.post('/auth')
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
    response = make_response(render_template('auth.html', **context))
    response.set_cookie(key='name', expires=0)
    response.set_cookie(key='email', expires=0)
    return response

@app.errorhandler(404)
def error_404(e):
    context = {'title': 'Страница не найдена'}
    return render_template('error_404.html', **context), 404

if __name__=='__main__':
    app.run()
