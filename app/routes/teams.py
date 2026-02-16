"""Teams/cellules routes blueprint."""
from flask import Blueprint, render_template

teams_bp = Blueprint("teams", __name__)


@teams_bp.route("/cellule_projet")
def cellule_projet():
    """Cellule Projet page route."""
    return render_template("cellule_projet.html")


@teams_bp.route("/cellule_logistique")
def cellule_logistique():
    """Cellule Logistique page route."""
    return render_template("cellule_logistique.html")


@teams_bp.route("/cellule_conception")
def cellule_conception():
    """Cellule Conception page route."""
    return render_template("cellule_conception.html")


@teams_bp.route("/cellule_media")
def cellule_media():
    """Cellule Media page route."""
    return render_template("cellule_media.html")


@teams_bp.route("/cellule_sponsoring")
def cellule_sponsoring():
    """Cellule Sponsoring page route."""
    return render_template("cellule_sponsoring.html")


@teams_bp.route("/cellule_communication_externe")
def cellule_communication():
    """Cellule Communication Externe page route."""
    return render_template("cellule_communication_externe.html")


@teams_bp.route("/cellule_formation")
def cellule_formation():
    """Cellule Formation page route."""
    return render_template("cellule_formation.html")
