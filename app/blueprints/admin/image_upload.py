from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, storage
import hashlib
from app.models import ImagePath
from app import db
from werkzeug.utils import secure_filename
from flask_wtf.file import FileStorage

def image_upload(image: FileStorage) -> None:
    load_dotenv()
    service_account_json = os.getenv("FIREBASE_ADMIN_CREDENTIALS_JSON")
    
    # initializing firebase-admin SDK
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account_json)
        firebase_admin.initialize_app(cred, {"storageBucket": "induskritistorage.appspot.com"})
    
    bucket = storage.bucket()

    #creating image hash
    img_hash = hashlib.sha256(image.read()).hexdigest()

    #upload the image to Firebase Storage
    blob = bucket.blob(f'images/{img_hash}.jpg')
    blob.upload_from_file(image, rewind=True)

    #store image hash in database
    img_name = secure_filename(image.filename)
    image_hash = ImagePath(img_name=img_name, img_hash=img_hash)
    db.session.add(image_hash)
    db.session.commit()