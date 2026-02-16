"""Projects/assignments routes blueprint."""
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    current_app,
)
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename

from app.utils.validators import allowed_file

projects_bp = Blueprint("projects", __name__)


def load_projects():
    """Load projects from JSON file."""
    projects_db_path = current_app.config["PROJECTS_DB_PATH"]
    if not os.path.exists(projects_db_path):
        return []
    try:
        with open(projects_db_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def save_projects(projects):
    """Save projects to JSON file."""
    projects_db_path = current_app.config["PROJECTS_DB_PATH"]
    with open(projects_db_path, "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)


@projects_bp.route("/assignments", methods=["GET", "POST"])
def assignments():
    """Handle project assignments page and submissions."""
    projects = load_projects()

    # Unlock upload with access code
    if request.method == "POST" and request.form.get("action") == "unlock":
        code = request.form.get("access_code", "").strip()
        if code == current_app.config["UPLOAD_ACCESS_CODE"]:
            session["can_upload"] = True
            flash("Accès autorisé. Vous pouvez déposer un projet.")
        else:
            flash("Code incorrect.")
        return redirect(url_for("projects.assignments"))

    # Upload project (only if unlocked)
    if request.method == "POST" and request.form.get("action") == "upload":
        if not session.get("can_upload"):
            flash("Accès refusé. Entrez le code d'accès pour déposer un projet.")
            return redirect(url_for("projects.assignments"))

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()

        if not title:
            flash("Titre obligatoire.")
            return redirect(url_for("projects.assignments"))

        if category not in ["PFE", "Hackathon", "Course project"]:
            flash("Catégorie invalide.")
            return redirect(url_for("projects.assignments"))

        if "file" not in request.files:
            flash("Aucun fichier sélectionné.")
            return redirect(url_for("projects.assignments"))

        file = request.files["file"]
        if file.filename == "":
            flash("Nom de fichier vide.")
            return redirect(url_for("projects.assignments"))

        if not allowed_file(file.filename, current_app.config["ALLOWED_EXTENSIONS"]):
            flash("Type de fichier non autorisé.")
            return redirect(url_for("projects.assignments"))

        safe_name = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_name = f"{timestamp}_{safe_name}"
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], final_name)
        file.save(filepath)

        projects.insert(
            0,
            {
                "title": title,
                "description": description,
                "category": category,
                "filename": final_name,
                "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            },
        )
        save_projects(projects)

        flash("Projet ajouté avec succès.")
        return redirect(url_for("projects.assignments"))

    # GET
    can_upload = bool(session.get("can_upload"))
    return render_template("assignments.html", projects=projects, can_upload=can_upload)


@projects_bp.route("/delete_project/<filename>", methods=["POST"])
def delete_project(filename):
    """Delete a project by filename."""
    if not session.get("can_upload"):
        flash("Accès refusé.")
        return redirect(url_for("projects.assignments"))

    projects = load_projects()

    # Remove project from list
    updated_projects = [p for p in projects if p["filename"] != filename]

    if len(updated_projects) == len(projects):
        flash("Projet introuvable.")
        return redirect(url_for("projects.assignments"))

    # Delete file from disk
    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    save_projects(updated_projects)
    flash("Projet supprimé avec succès.")
    return redirect(url_for("projects.assignments"))
