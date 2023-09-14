# adding an admin blueprint

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Customer
from .models import User, ImageHash
from .forms import GalleryForm, LoginForm
from .firebase import File
from flask_login import login_user, login_required, logout_user

admin_page = Blueprint('admin', __name__, template_folder='templates/', static_folder='static/')

@admin_page.route("/", methods=['GET', 'POST'])
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
    return render_template("login.html", form=form)

@admin_page.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for('admin.login'))


@admin_page.route('/dashboard/')
@login_required
def admin_dashboard():
    return render_template('dashboard.html')


@admin_page.route('/customer-list/')
@login_required
def customer_list():
    customers = Customer.query.all()
    return render_template('customer_details.html', customers=customers)


@admin_page.route('/admin-gallery/', methods=['GET', 'POST'])
@login_required
def gallery_list():
    form = GalleryForm()
    if form.validate_on_submit():
        image = form.image.data
        if not image:
            flash(f"No file selected for uploading")
            return redirect(url_for("admin.gallery_list"))
        else:
            File().image_upload(image)
            flash(f"Image Uploaded Successfully", "success")
            return redirect(url_for("admin.gallery_list"))
    
    image_info = ImageHash.query.all()
    return render_template('admin_gallery.html', form=form, image_info=image_info)