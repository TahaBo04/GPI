"""Partners routes blueprint - internships and sponsors."""
from flask import Blueprint, render_template, request, redirect, url_for, current_app

partners_bp = Blueprint("partners", __name__)


@partners_bp.route("/sponsors_protect", methods=["GET", "POST"])
def sponsors_protect():
    """Password-protected sponsors page."""
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == current_app.config["SPONSOR_PASSWORD"]:
            return redirect(url_for("partners.internships"))
        return render_template("sponsors_protect.html", error=True)
    return render_template("sponsors_protect.html", error=False)


@partners_bp.route("/internships")
def internships():
    """Internships and partners page route."""
    return render_template("internships.html")
