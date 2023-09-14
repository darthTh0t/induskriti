import hashlib
from .models import ImageHash
import os
import firebase_admin
from firebase_admin import storage, credentials
from werkzeug.utils import secure_filename
from flask_wtf.file import FileStorage
from dotenv import load_dotenv
from app import db
from datetime import timedelta


class File:

    def __init__(self):
        load_dotenv()
        service_account_json = os.getenv("FIREBASE_ADMIN_CREDENTIALS_JSON")

        #initialising firebase admin SDK
        if not firebase_admin._apps:
            cred = credentials.Certificate(service_account_json)
            firebase_admin.initialize_app(cred, {"storageBucket":"induskritistorage.appspot.com"})


    def image_upload(self, image:FileStorage) -> None:
        bucket = storage.bucket()

        #creating image hash
        img_hash = hashlib.sha256(image.read()).hexdigest()

        #upload the image to Firebase Storage
        blob = bucket.blob(f'gallery/{img_hash}.jpg')
        blob.upload_from_file(image, rewind=True)

        #store image hash in database
        img_name = secure_filename(image.filename)
        image_hash = ImageHash(img_name=img_name, img_hash=img_hash)
        db.session.add(image_hash)
        db.session.commit()

    def image_download(self) -> list:
        bucket = storage.bucket(name="induskritistorage.appspot.com")

        blobs = bucket.list_blobs(prefix="gallery/")

        image_urls = [
            blob.generate_signed_url(expiration=timedelta(minutes=20), method="GET") for blob in blobs if not blob.name.endswith("/")
        ]

        return image_urls