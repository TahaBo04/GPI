"""Conferences routes blueprint - conferences and events page."""
from flask import Blueprint, render_template

conferences_bp = Blueprint("conferences", __name__)


@conferences_bp.route("/conferences")
def conferences():
    """Conferences page route."""
    return render_template("conferences.html")
