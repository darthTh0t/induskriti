from app import db
from datetime import datetime


class Customer(db.Model):

    """Data Model for Customer Details"""
    
    __tablename__ = 'customer-detail'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    contact = db.Column("contact", db.Integer)
    email = db.Column("email", db.String)
    remarks = db.Column("remarks", db.Text)
    # date = db.Column(db.String)

    def __repr__(self):
        return f'<Customer {self.name}>'
    

class Testimonials(db.Model):
    """Data Model for Testimonials"""
    __tablename__ = 'testimonials'
    id = db.Column('id', db.Integer, primary_key=True)
    customer_name = db.Column('customer_name', db.String(30))
    testi_text = db.Column('testi_text', db.Text)
    rating = db.Column('rating', db.Float)
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Testimonial by {self.customer_name}'