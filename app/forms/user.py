from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
from wtforms import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Add(FlaskForm):
    name = StringField('Ниаменование ', validators=[DataRequired()])
    submit = SubmitField('Создать')


class CreateA(FlaskForm):
    name = StringField('Товар ', validators=[DataRequired()])
    art = StringField('Артикул ', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class CreateOrd(FlaskForm):
    name = StringField('Товар ', validators=[DataRequired()])
    art = StringField('Артикул ', validators=[DataRequired()])
    count = StringField('Количество ', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class Ord(FlaskForm):
    submit = SubmitField('Добавить')
