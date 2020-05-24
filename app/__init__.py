from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from app.config import Config

from app.utils.worker import conn
from rq import Queue
import rq_dashboard

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.login_message_category = 'info'
mail = Mail()
q = Queue(connection=conn)

def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    migrate.init_app(flask_app,db)
    bcrypt.init_app(flask_app)
    login_manager.init_app(flask_app)
    mail.init_app(flask_app)

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.errors.handlers import errors_bp
    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(main_bp)
    flask_app.register_blueprint(errors_bp)

    flask_app.config.from_object(rq_dashboard.default_settings)
    flask_app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

    return flask_app
