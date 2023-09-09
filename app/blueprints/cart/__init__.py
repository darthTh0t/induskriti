from flask import Blueprint, render_template, redirect, url_for
from app import db


cart_page = Blueprint('cart', __name__, template_folder='templates/', static_folder='static/')

@cart_page.route('/')
def cart_index():
	return render_template('cart_product.html')
