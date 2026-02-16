"""Configuration management for GPI Flask application."""
import os
from pathlib import Path


class Config:
    """Base configuration class."""
    
    # Basic Flask config
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    
    # File upload configuration
    BASE_DIR = Path(__file__).parent.parent
    UPLOAD_FOLDER = os.path.join("static", "uploads")
    ALLOWED_EXTENSIONS = {"pdf", "docx", "zip", "png", "jpg", "jpeg"}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Database/storage paths
    PROJECTS_DB_PATH = os.path.join("static", "projects.json")
    
    # Access codes
    UPLOAD_ACCESS_CODE = os.environ.get("UPLOAD_ACCESS_CODE", "zyad lchgr")
    SPONSOR_PASSWORD = os.environ.get("SPONSOR_PASSWORD", "lchgr zyad")


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
