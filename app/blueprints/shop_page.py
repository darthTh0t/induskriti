from flask import Blueprint, redirect, request, flash, render_template, url_for
from app import db
import firebase_admin
from firebase_admin import storage


shop_page = Blueprint('shop', __name__, template_folder='templates/shop', static_folder='static/shop')

def get_image_urls():
	bucket = storage.bucket(app=firebase_admin.get_app())
	blobs = bucket.list_blobs(prefix="images/")
	image_urls = [blob.public_url for blob in blobs]
	return image_urls


@shop_page.route('/')
def shop_base():
	image_urls = get_image_urls()
	return render_template('shop/shop_base.html', image_urls=image_urls)