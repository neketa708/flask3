# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, flash, render_template, request
from flask_wtf.csrf import CSRFProtect
from form_3 import LoginForm, RegistrationForm
from hw_model_04 import User, db
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_hw_app_04.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('initdb_04')
def initdb_command():
    db.create_all()
    print('Initialized the database.')

@app.route('/')
def index():
    return render_template('hw_task_04.html')


@app.route('/login', methods=['GET', 'POST'])
@csrf.exempt
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user_exist = (
            User.query.filter(User.email == email).first() or 
            User.query.filter(User.username == username).first()
            )
        if user_exist:
            flash(f'Пользователь уже зарегистрирован!!!')
            return render_template('message.html')
        new_user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
            )
        db.session.add(new_user)
        db.session.commit()
        flash('Регистрация прошла успешно!!!')
        return render_template('message.html')
    return render_template('register.html', form=form)
        

if __name__ == '__main__':
    app.run(debug=True)