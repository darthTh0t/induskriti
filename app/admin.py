# adding an admin blueprint

from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for
from .models import Customer, User
from .forms import GalleryForm, LoginForm
from app import db
from flask_login import login_user, logout_user, login_required

admin_page = Blueprint('admin', __name__, template_folder='templates/admin', static_folder='static/admin')

@admin_page.route('/login/', methods=['GET','POST'])
def admin_login():
    form=LoginForm()
    next_url = request.form.get("next")
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash(f'Login Successful', 'success')
            if next_url:
                return redirect(next_url)
            return redirect(url_for('admin.admin_dashboard'))
        else:
            flash(f'Invalid Credentials', 'danger')
    return render_template('admin/login.html', form=form)

@admin_page.route('/logout/')
@login_required
def admin_logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('admin.admin_login()'))

@admin_page.route('/dashboard/')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')


@admin_page.route('/customer-list/')
@login_required
def customer_list():
    customers = Customer.query.all()
    return render_template('admin/customer_details.html', customers=customers)


@admin_page.route('/admin-gallery/')
@login_required
def gallery_list():
    form = GalleryForm()
    return render_template('admin/admin_gallery.html', form=form)