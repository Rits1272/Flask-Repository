
import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext 
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    OUTPUT_SIZE = (250, 250)
    i = Image.open(form_picture) 
    i.thumbnail(OUTPUT_SIZE)
    i.save(picture_path)
    
    return picture_fn 


def send_request_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='ritikjain1272@gmail.com', recipients=[user.email])
    msg.body = f''' 
    To reset your password, visit the following link
{url_for("reset_token", token=token, _external=True)}
    
    If you did not make this request then simply ignore this email
    '''
    mail.send(msg)
