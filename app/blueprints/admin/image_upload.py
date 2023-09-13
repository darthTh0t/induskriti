from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, storage
import hashlib
from app.models import ImagePath
from app import db

def image_upload(img_name: str, image) -> None:
    load_dotenv()
    service_account_json = os.getenv("FIREBASE_ADMIN_CREDENTIALS_JSON")
    
    # initializing firebase-admin SDK
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account_json)
        firebase_admin.initialize_app(cred)
    
    bucket = storage.bucket()

    #creating image hash
    img_hash = hashlib.sha256(image.read()).hexdigest()

    #upload the image to Firebase Storage
    blob = bucket.blob(f'images/{img_hash}.jpg')
    blob.upload_from_file(image)

    #store image hash in database
    image_hash = ImagePath(img_name=img_name, img_hash=img_hash)
    db.session.add(image_hash)
    db.session.commit()