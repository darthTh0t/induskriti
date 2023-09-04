# adding an admin blueprint

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Customer, User
from app.forms import GalleryForm, LoginForm
from app import db
from flask_login import login_user, login_required, logout_user

admin_page = Blueprint('admin', __name__, template_folder='templates/admin', static_folder='static/admin')

@admin_page.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login Successful", "success")
            return redirect(request.args.get('next') or url_for('admin.admin_dashboard'))
        else:
            flash("Invalid Credentials", "danger")
            return redirect(url_for('admin.login'))
    return render_template("admin/login.html", form=form)

@admin_page.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for('admin.login'))


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