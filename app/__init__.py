"""Flask application factory."""
from flask import Flask
import os


def create_app(config_name=None):
    """
    Create and configure the Flask application.
    
    Args:
        config_name: Configuration name (development, production, or default)
        
    Returns:
        Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")
    
    from app.config import config
    app.config.from_object(config[config_name])
    
    # Ensure required directories exist
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(os.path.dirname(app.config["PROJECTS_DB_PATH"]), exist_ok=True)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.projects import projects_bp
    from app.routes.resources import resources_bp
    from app.routes.partners import partners_bp
    from app.routes.teams import teams_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(partners_bp)
    app.register_blueprint(teams_bp)
    
    return app
