from random import choices
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('<PASSWORD>', validators=[DataRequired()])
    
    
class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = StringField('Пол', choices=[('male', 'Мужской'), ('female', 'Женский]')])
    
    
class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('<PASSWORD>', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('<CONFIRM_PASSWORD>', validators=[DataRequired(),EqualTo('password')])