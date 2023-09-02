# adding an admin blueprint

from flask import Blueprint, render_template
from .models import Customer
from .forms import GalleryForm
from app import db

admin_page = Blueprint('admin', __name__, template_folder='templates/admin', static_folder='static/admin')

@admin_page.route('/dashboard/')
def admin_dashboard():
    return render_template('dashboard.html')


@admin_page.route('/customer-list/')
def customer_list():
    customers = Customer.query.all()
    return render_template('customer_details.html', customers=customers)


@admin_page.route('/admin-gallery/')
def gallery_list():
    form = GalleryForm()
    return render_template('admin_gallery.html', form=form)