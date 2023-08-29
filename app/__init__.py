from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text, MetaData, Table


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    #login_manager.init_app(app)
    with app.app_context():
        from . import routes
        #db.drop_all()
        return app
