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

@app.route('/assignments', methods=['GET', 'POST'])
def assignments():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Aucun fichier sélectionné')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('Nom de fichier vide')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('Fichier téléchargé avec succès !')
            return redirect(url_for('assignments'))

        flash('Type de fichier non autorisé.')
        return redirect(request.url)

    # ✅ Get list of files from Python, then send to template
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('assignments.html', uploaded_files=uploaded_files)


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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
