from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text, MetaData, Table
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    with app.app_context():

        from .blueprints.admin import admin_page
        from .blueprints.gallery import gallery_page


        app.register_blueprint(gallery_page, url_prefix='/gallery')
        app.register_blueprint(admin_page, url_prefix='/admin')

        from . import routes
        #db.drop_all()
        return app
