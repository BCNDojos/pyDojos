from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # from api import api
    # from views import views
    # app.register_blueprint(api)
    # app.register_blueprint(views)

    from models import db
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
