# shop_page.py
import firebase_admin
from firebase_admin import storage, credentials
from flask import Blueprint, redirect, request, flash, render_template, url_for, current_app
from app import db
from datetime import timedelta


shop_page = Blueprint('shop', __name__, template_folder='templates/', static_folder='static/')

def get_image_urls():
    # initializing firebase-admin SDK
    if not firebase_admin._apps:
        cred = credentials.Certificate('induskritistorage-firebase-adminsdk-b2qf0-4cef56dc0b.json')
        firebase_admin.initialize_app(cred)
    # getting a reference to the Firebase Storage bucket
    bucket = storage.bucket(name="induskritistorage.appspot.com")
    # listing the images in the "images" directory in your Firebase Storage bucket
    blobs = bucket.list_blobs(prefix="images/")
    # creating a list of image URLs by directly using blob.generate_signed_url
    image_urls = [blob.generate_signed_url(expiration=timedelta(minutes=15), method="GET") \
                   for blob in blobs if not blob.name.endswith('/')]
    return image_urls

@shop_page.route('/', methods=['GET'])
def shop_base():
    image_urls = get_image_urls()
    return render_template('shop/shop_base.html', image_urls=image_urls)
