from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):

    """Data Model for User Login"""
    __tablename__ = 'admin_info'
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String)

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class ImageHash(db.Model):
    """Image Hash Table to store the image hash values and corresponding images."""
    __tablename__ = "image_info"
    id = db.Column("id", db.Integer, primary_key=True)
    img_name = db.Column("img_name", db.String(64), nullable=False)
    img_hash = db.Column("img_hash", db.String)