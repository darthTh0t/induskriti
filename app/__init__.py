from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import text, MetaData, Table


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    admin = Admin(app, template_mode='bootstrap3', name='Induskriti-Admin')
    
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from . import routes
        #db.drop_all()
        return app
