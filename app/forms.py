from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Как вас зовут?', validators=[DataRequired()])
    submit = SubmitField('Нажать')


class RegisterForm(FlaskForm):
    name = StringField('Как вас зовут?', validators=[DataRequired()])
    email = EmailField('Ваша почта', validators=[DataRequired(), Email()])
    password = PasswordField('Ваш пароль', validators=[DataRequired()])
    password2 = PasswordField('Ваш пароль', validators=[DataRequired()])
    submit = SubmitField('Сохранить')