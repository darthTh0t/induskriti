
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Customer, User, Blog
from app.forms import GalleryForm, LoginForm, BlogForm
from app import db
from flask_login import login_user, login_required, logout_user
from .image_upload import image_upload


# adding an admin blueprint
admin_page = Blueprint(
    "admin", __name__, template_folder="templates/", static_folder="static/"
)


@admin_page.route("/", methods=['GET', 'POST'])
@admin_page.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login Successful", "success")
            return redirect(
                request.args.get("next") or url_for("admin.admin_dashboard")
            )
        else:
            flash("Invalid Credentials", "danger")
            return redirect(url_for("admin.login"))
    return render_template("login.html", form=form)


@admin_page.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("admin.login"))


@admin_page.route("/dashboard/")
@login_required
def admin_dashboard():
    return render_template("dashboard.html")


@admin_page.route("/customer-list/")
@login_required
def customer_list():
    customers = Customer.query.all()
    return render_template("customer_details.html", customers=customers)


@admin_page.route("/admin-gallery/", methods=['GET', 'POST'])
@login_required
def gallery_list():
    form = GalleryForm()
    if form.validate_on_submit():
        image = form.image.data
        if not image:
            flash(f"No file selected for uploading")
            return redirect(url_for("admin.gallery_list"))
        else:
            image_upload(image)
            flash(f"Image Uploaded Successfully")
            return redirect(url_for("admin.gallery_list"))
    return render_template("admin_gallery.html", form=form)


@admin_page.route("/admin-blog", methods=["GET", "POST"])
@login_required
def blog_list():
    form = BlogForm()
    if form.validate_on_submit():
        title = request.form.get("blog_title")
        body = request.form.get("blog_body")

        blog = Blog(title=title, body=body)
        db.session.add(blog)
        db.session.commit()
        flash(f"Blog Uploaded!", "success")
        return redirect(url_for("blog_list"))

    blog_list = Blog.query.all()
    return render_template("blog_upload.html", form=form, blog_list=blog_list)
