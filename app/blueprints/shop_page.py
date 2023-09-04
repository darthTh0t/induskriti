from flask import Blueprint, redirect, request, flash, render_template, url_for
from app import db


shop_page = Blueprint('shop', __name__, template_folder='templates/shop', static_folder='static/shop')

@shop_page.route('/')
def shop_base():
	return render_template('shop/shop_base.html')