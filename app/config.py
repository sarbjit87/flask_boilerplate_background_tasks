import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '13b8184b924cf6f8e31fe7abfd1d3721' #secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  ******  EMAIL Settings  ******

    # GMAIL Configuration for sending emails
    #MAIL_SERVER = 'smtp.googlemail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # Test Server for emails
    # Run the server on Python terminal as
    # python -m smtpd -n -c DebuggingServer localhost:8025
    MAIL_SERVER='localhost'
    MAIL_PORT=8025

    #  ******  Back ground tasks  ******

    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    # This is required to be used inside email sending background task
    SERVER_NAME='127.0.0.1:5000'


    FILE_UPLOAD = os.path.join(basedir, 'uploads')
    APP_NAME = "My Application"

    #  ******  LDAP Settings  ******

    #LDAP_LOGIN_ENABLED = True
    #LDAP_PROVIDER_URL = 'ldap://ldap.forumsys.com:389/'
    #LDAP_PROTOCOL_VERSION = 3
