import time
from app.auth.models import User
from flask_mail import Message
from flask import url_for

def send_reset_email_task(user):
    # Get the application context
    from app.config import Config
    from app import db, create_app, mail
    flask_app = create_app(Config)
    flask_app.app_context().push()

    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('auth_bp.reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)

    print("Task Started")
    user = User.query.get(1)
    print(user)
    print("Task Completed")

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('auth_bp.reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)
