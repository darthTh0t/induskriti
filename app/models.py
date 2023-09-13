from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Customer(db.Model):

    """Data Model for Customer Details"""
    
    __tablename__ = 'customer_info'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    contact = db.Column("contact", db.Integer)
    email = db.Column("email", db.String)
    remarks = db.Column("remarks", db.Text)
    # date = db.Column(db.String)

    def __repr__(self):
        return f'<Customer {self.name}>'



# Admin related models

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
    


class Blog(db.Model):
    """Data Model for Blogs"""
    __tablename__= 'blog_info'
    id = db.Column("id", db.Integer, nullable=False, primary_key=True)
    title = db.Column("title", db.String(64), nullable=False)
    body = db.Column("body", db.Text)

    def __repr__(self):
        return f'<Blog {self.title}>'



class ImagePath(db.Model):
    """Data Model to store image path"""
    __tablename__= "image_path"
    id = db.Column("id", db.Integer, nullable=False, primary_key=True)
    img_name = db.Column("name", db.String(64), nullable=False)
    img_hash = db.Column(db.String)