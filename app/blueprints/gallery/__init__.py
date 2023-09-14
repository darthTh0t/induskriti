from flask import Blueprint, flash ,redirect, render_template, request, url_for
from app.blueprints.admin.models import ImageHash
from app.blueprints.admin.firebase import File

gallery_page = Blueprint('gallery', __name__, template_folder='templates/', static_folder='static/')

@gallery_page.route('/')
def index():
	image_urls = File().image_download()
	return render_template('gallery.html', image_urls=image_urls)