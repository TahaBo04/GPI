from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flashing messages
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'zip', 'png', 'jpg'}

# Make sure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'zip', 'png', 'jpg', 'jpeg'}

# Access code for uploads (change it)
UPLOAD_ACCESS_CODE = os.environ.get("UPLOAD_ACCESS_CODE", "GPI2026")

# Where we store metadata
PROJECTS_DB_PATH = os.path.join("static", "projects.json")

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_projects():
    if not os.path.exists(PROJECTS_DB_PATH):
        return []
    try:
        with open(PROJECTS_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_projects(projects):
    os.makedirs(os.path.dirname(PROJECTS_DB_PATH), exist_ok=True)
    with open(PROJECTS_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

@app.route('/assignments', methods=['GET', 'POST'])
def assignments():
    projects = load_projects()

    # If user submits access code
    if request.method == 'POST' and request.form.get("action") == "unlock":
        code = request.form.get("access_code", "").strip()
        if code == UPLOAD_ACCESS_CODE:
            session["can_upload"] = True
            flash("Accès autorisé. Vous pouvez déposer un projet.")
        else:
            flash("Code incorrect.")
        return redirect(url_for("assignments"))

    # Upload project (only if unlocked)
    if request.method == 'POST' and request.form.get("action") == "upload":
        if not session.get("can_upload"):
            flash("Accès refusé. Entrez le code d’accès pour déposer un projet.")
            return redirect(url_for("assignments"))

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()

        if not title:
            flash("Titre obligatoire.")
            return redirect(url_for("assignments"))

        if category not in ["PFE", "Hackathon", "Course project"]:
            flash("Catégorie invalide.")
            return redirect(url_for("assignments"))

        if 'file' not in request.files:
            flash("Aucun fichier sélectionné.")
            return redirect(url_for("assignments"))

        file = request.files['file']
        if file.filename == '':
            flash("Nom de fichier vide.")
            return redirect(url_for("assignments"))

        if not allowed_file(file.filename):
            flash("Type de fichier non autorisé.")
            return redirect(url_for("assignments"))

        safe_name = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_name = f"{timestamp}_{safe_name}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], final_name)
        file.save(filepath)

        projects.insert(0, {
            "title": title,
            "description": description,
            "category": category,
            "filename": final_name,
            "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_projects(projects)

        flash("Projet ajouté avec succès.")
        return redirect(url_for("assignments"))

    # GET
    can_upload = bool(session.get("can_upload"))
    return render_template("assignments.html", projects=projects, can_upload=can_upload)

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/process')
def process():
    return render_template('process.html')

SPONSOR_PASSWORD = 'lchgr zyad'

@app.route('/sponsors_protect', methods=['GET', 'POST'])
def sponsors_protect():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == SPONSOR_PASSWORD:
            return redirect(url_for('internships'))
        else:
            return render_template('sponsors_protect.html', error=True)
    return render_template('sponsors_protect.html', error=False)

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/cellule_projet')
def cellule_projet():
    return render_template('cellule_projet.html')

@app.route('/cellule_logistique')
def cellule_logistique():
    return render_template('cellule_logistique.html')

@app.route('/cellule_conception')
def cellule_conception():
    return render_template('cellule_conception.html')

@app.route('/cellule_media')
def cellule_media():
    return render_template('cellule_media.html')

@app.route('/cellule_sponsoring')
def cellule_sponsoring():
    return render_template('cellule_sponsoring.html')

@app.route('/cellule_communication_externe')
def cellule_communication():
    return render_template('cellule_communication_externe.html')

@app.route('/cellule_formation')
def cellule_formation():
    return render_template('cellule_formation.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


