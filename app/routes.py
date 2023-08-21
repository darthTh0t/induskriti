from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ContactForm


@app.route("/")
def index():
    title = "Welcome to Induskriti"
    return render_template("hero-page.html", title=title)


@app.route("/gallery/")
def gallery():
    return render_template("gallery.html")


@app.route("/about-us/")
def about_us():
    return render_template("about-us.html")


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Details Received for {form.name.data}!", "success")
        return redirect(url_for("index"))
    return render_template("contact.html", form=form)
