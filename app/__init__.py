from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
# Redirect users to this page if they try to access a protected page without being logged in
login_manager.login_view = 'routes.login'
login_manager.login_message_category = 'info'  # Optional: for better message styling


def create_app(config_class=Config):
    """
    Creates and configures an instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Bind the extensions to the app instance
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register the blueprint from the routes file
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # The user loader function needs to be available to Flask-Login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
