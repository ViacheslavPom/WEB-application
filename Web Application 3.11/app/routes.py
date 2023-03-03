from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import Users

@app.route('/')
@app.route('/index')
def index():
    title = 'Главная страница'
    form = LoginForm()
    username = None
    if form.validate_on_submit():
        # если отправлена форма
        username = form.username.data
    return render_template('index.html', title=title, username=username, form=form)
@app.route('/second')
def second():
    title = 'Вторая страница'
    return render_template('second.html', title=title)
@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Регистрация'
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pwd = form.password.data
        pwd2 = form.password2.data
        if pwd != pwd2:
            flash("Пароль не совпадает с подтверждением!")
        else:
            user = Users(name=name, email=email, passwd=pwd)
            db.session.add(user)
            db.session.commit()
            flash("Успешная регистрация!")
            return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)