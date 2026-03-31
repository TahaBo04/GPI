"""Main routes blueprint - home and about pages."""
from pathlib import Path

from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

SPECIALIZATION_DOMAINS = [
    {
        "tag": "Simulation",
        "title": "Procédés & simulation industrielle",
        "description": (
            "Bilans matière et énergie, conception d'unités, simulation et "
            "optimisation des procédés."
        ),
        "focus": "Aspen HYSYS, thermodynamique, dimensionnement, performance",
        "filename": "procedes-simulation.pdf",
    },
    {
        "tag": "Énergie",
        "title": "Énergie & utilités de production",
        "description": (
            "Production vapeur, efficacité énergétique, intégration des "
            "utilités et valorisation des ressources."
        ),
        "focus": "Thermique, réseaux utilités, décarbonation, sobriété",
        "filename": "energie-utilites.pdf",
    },
    {
        "tag": "Environnement",
        "title": "Eau, environnement & traitement",
        "description": (
            "Traitement des eaux, dépollution, dessalement et solutions "
            "durables pour l'industrie."
        ),
        "focus": "Environnement, traitement, réglementation, impact",
        "filename": "eau-environnement-traitement.pdf",
    },
    {
        "tag": "Qualité",
        "title": "Matériaux, formulation & qualité",
        "description": (
            "Développement produit, contrôle qualité et amélioration continue "
            "dans les industries de transformation."
        ),
        "focus": "Matériaux, formulation, contrôle, optimisation",
        "filename": "materiaux-formulation-qualite.pdf",
    },
]

PROCESS_SPECIALTY_DOMAINS = [
    {
        "tag": "Cimenterie",
        "title": "Cimenterie",
        "description": (
            "Un document de référence pour présenter les procédés, les enjeux "
            "industriels et la chaîne de valeur autour de la cimenterie."
        ),
        "focus": "Production, transformation, industrie lourde, procédés",
        "filename": "cimenterie.pdf",
    },
    {
        "tag": "Énergie",
        "title": "Énergie et environnement",
        "description": (
            "Une fiche dédiée aux systèmes énergétiques, aux utilités et aux "
            "enjeux environnementaux dans l'industrie des procédés."
        ),
        "focus": "Thermique, utilités, environnement, décarbonation",
        "filename": "energie-et-environnement.pdf",
    },
    {
        "tag": "Pétrochimie",
        "title": "Pétrochimie",
        "description": (
            "Une rubrique prête à accueillir vos fichiers sur le raffinage, les "
            "transformations chimiques et les chaînes pétrochimiques."
        ),
        "focus": "Raffinage, hydrocarbures, procédés, sécurité industrielle",
        "filename": "petrochimie.pdf",
    },
]


def build_domain_cards(domain_definitions):
    """Create domain cards with automatic file detection."""
    domains = []
    for domain in domain_definitions:
        pdf_path = STATIC_DIR / "pdfs" / "domains" / domain["filename"]
        domains.append(
            {
                **domain,
                "pdf_exists": pdf_path.exists(),
                "static_path": f"pdfs/domains/{domain['filename']}",
                "storage_hint": f"app/static/pdfs/domains/{domain['filename']}",
            }
        )
    return domains


def build_specialization_domains():
    """Create the specialization cards shown on the homepage."""
    return build_domain_cards(SPECIALIZATION_DOMAINS)


def build_process_specialty_domains():
    """Create the domain cards shown on the about/process page."""
    return build_domain_cards(PROCESS_SPECIALTY_DOMAINS)


@main_bp.route("/")
def home():
    """Home page route."""
    video_path = STATIC_DIR / "media" / "club-presentation.mp4"
    poster_path = STATIC_DIR / "media" / "club-presentation-poster.jpg"

    presentation_video = {
        "exists": video_path.exists(),
        "static_path": "media/club-presentation.mp4",
        "storage_hint": "app/static/media/club-presentation.mp4",
        "poster_exists": poster_path.exists(),
        "poster_static_path": "media/club-presentation-poster.jpg",
        "poster_hint": "app/static/media/club-presentation-poster.jpg",
    }

    return render_template(
        "index.html",
        presentation_video=presentation_video,
        specialization_domains=build_specialization_domains(),
    )


@main_bp.route("/process")
def process():
    """About/process page route."""
    return render_template(
        "process.html",
        process_domains=build_process_specialty_domains(),
    )
