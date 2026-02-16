"""Resources/courses routes blueprint."""
from flask import Blueprint, render_template

resources_bp = Blueprint("resources", __name__)


@resources_bp.route("/courses")
def courses():
    """Courses/resources page route."""
    return render_template("courses.html")
