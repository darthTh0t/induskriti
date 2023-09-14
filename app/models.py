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