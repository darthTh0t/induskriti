from flask import Blueprint, flash ,redirect, render_template, request, url_for
from app import db
import firebase_admin
from firebase_admin import storage, credentials

gallery_page = Blueprint('gallery', __name__, template_folder='templates/', static_folder='static/')

@gallery_page.route('/')
def index():
	return render_template('gallery.html')