from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.jobs import Jobs
from data.login_form import LoginForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/mars_explorer.sqlite")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    app.run()


if __name__ == '__main__':
    main()
