# GPI - Club Génie des Procédés

A professional Flask web application for the Club Génie des Procédés at EMI (École Mohammadia d'Ingénieurs).

## Features

- **Project Management**: Upload, view, and manage student projects (PFE, Hackathons, Course projects)
- **Resource Center**: Course materials and resources for Génie des Procédés students
- **Team Pages**: Dedicated pages for each cellule (team) within the club
- **Partner Network**: Internship and sponsor information
- **Responsive Design**: Mobile-friendly interface with modern styling

## Architecture

The application follows Flask best practices with:
- **Blueprint Pattern**: Modular route organization
- **App Factory**: Flexible application initialization
- **Configuration Management**: Environment-based settings
- **Template Inheritance**: DRY principle with base templates
- **Modular CSS**: Separated styling concerns

## Project Structure

```
GPI/
├── app/
│   ├── __init__.py          # App factory
│   ├── config.py            # Configuration management
│   ├── routes/              # Blueprint modules
│   │   ├── main.py          # Home & about routes
│   │   ├── projects.py      # Project management routes
│   │   ├── resources.py     # Course resources routes
│   │   ├── partners.py      # Partners & internships routes
│   │   └── teams.py         # Cellule team pages routes
│   ├── utils/               # Helper functions
│   │   └── validators.py    # File validation utilities
│   ├── templates/           # Jinja2 templates
│   │   ├── base.html        # Base template
│   │   └── ...              # Page templates
│   └── static/              # Static assets
│       ├── css/             # Modular CSS files
│       │   ├── base.css     # Base styles & variables
│       │   ├── navbar.css   # Navigation styling
│       │   ├── sections.css # Content sections
│       │   ├── components.css # Reusable components
│       │   └── responsive.css # Mobile responsiveness
│       └── uploads/         # User-uploaded files
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TahaBo04/GPI.git
   cd GPI
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Environment Variables

Create a `.env` file with the following variables:

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
UPLOAD_ACCESS_CODE=your-upload-code
SPONSOR_PASSWORD=your-sponsor-password
PORT=5000
```

## Development

### Running in Development Mode
```bash
export FLASK_ENV=development
python run.py
```

### CSS Customization
All styling is organized into modular CSS files in `app/static/css/`:
- Modify `base.css` for color schemes and global styles
- Update `components.css` for buttons, forms, and UI elements
- Edit `responsive.css` for mobile breakpoints

### Adding New Routes
1. Create a new blueprint in `app/routes/`
2. Register it in `app/__init__.py`
3. Create corresponding templates in `app/templates/`

## Deployment

The application is designed to be deployed on platforms like:
- Vercel
- Heroku
- Railway
- Any platform supporting Python/Flask

Make sure to:
1. Set environment variables in your platform's dashboard
2. Configure the `PORT` variable if required
3. Set `FLASK_ENV=production` for production deployments

## Security

- Access codes protect sensitive routes (project uploads, sponsors)
- File upload validation restricts allowed file types
- Session-based authentication for protected features
- Environment variables for sensitive configuration

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

© 2025 Club Génie des Procédés – EMI

## Contact

- **LinkedIn**: [emi-process](https://www.linkedin.com/in/emi-process-b2b0b1292/)
- **Instagram**: [@emi_process](https://www.instagram.com/emi_process/)
- **Email**: clubgenie@emi.ac.ma Class Website

A Flask-based academic portal for students in Génie des Procédés Industriels.
Includes course materials, assignment submissions, and career info.
