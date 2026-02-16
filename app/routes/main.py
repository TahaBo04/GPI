"""Main routes blueprint - home and about pages."""
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    """Home page route."""
    return render_template("index.html")


@main_bp.route("/process")
def process():
    """About/process page route."""
    return render_template("process.html")
