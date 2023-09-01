from flask import render_template, flash, redirect, url_for, request
from flask import current_app as app
from app.forms import ContactForm, LoginForm
from .models import db, Customer
from .data import about_data
#from app import login_manager



@app.route("/")
def index():
    title = "Welcome to Induskriti"
    return render_template("hero-page.html", title=title)


@app.route("/gallery/")
def gallery():
    return render_template("gallery.html")


@app.route("/about-us/")
def about_us():
    return render_template("about-us.html", about_data=about_data)


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name = request.form.get("name")
                contact = request.form.get("phone_number")
                email = request.form.get("email")
                remarks = request.form.get("comment")

                customer = Customer(
                    name=name, 
                    contact=contact, 
                    email=email, 
                    remarks=remarks
                )  # load the model values
                form.populate_obj(Customer)  # populates the form with respective values
                db.session.add(
                    customer
                )  # gathers the session bases data to be added to the DB
                db.session.commit()  # adds data to DB
                flash(f"Details Received for {form.name.data}!", "success")
                return redirect("/contact/")
        except Exception as e:
            db.session.rollback()
            flash(
                f"There was a problem. Please refresh the page and try again", "danger"
            )
            print(e)
            return redirect(url_for("contact"))
    
    #testimonials = Testimonials.query.all()
    return render_template("contact.html", form=form)

