import logging
import os

from flask import Flask, render_template
from dotenv import load_dotenv

# Hobby content lives in its own module so teammates can update images and names
# without touching route or template logic (Single Responsibility).
from .hobbies_data import TEAM_HOBBIES
from .work_history_data import TEAM_WORK_HISTORY
from .places_data import TEAM_PLACES

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

TEAM_MEMBERS = [
    {"name": "Adam Maatouk", "photo": "adam-maatouk.png"},
    {"name": "Amar Kanakamedala", "photo": "amar-kanakamedala.png"},
    {"name": "Gabriel Changamire", "photo": "gabriel-changamire.png"},
]

# New nav items only need an entry here once a matching route exists.
NAV_PAGES = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "work", "label": "Work"},
    {"endpoint": "hobbies", "label": "Hobbies"},
    {"endpoint": "map_page", "label": "Map"},
]

app = Flask(__name__)


@app.context_processor
def inject_globals():
    # Shared across all templates so the nav bar stays in sync automatically.
    return {
        "nav_pages": NAV_PAGES,
        "url": os.getenv("URL"),
    }


@app.route("/")
def index():
    logger.info("Serving index page")
    return render_template(
        "index.html",
        title="MLH Fellow",
        team_members=TEAM_MEMBERS,
    )


@app.route("/work")
def work():
    logger.info("Serving work history page")
    return render_template("work.html", title="Work Experience", team_work=TEAM_WORK_HISTORY)


@app.route("/hobbies")
def hobbies():
    logger.info("Serving hobbies page")
    return render_template("hobbies.html", team_hobbies=TEAM_HOBBIES)


@app.route("/map")
def map_page():
    logger.info("Serving map page")
    return render_template("map.html", title="Around the World", team_places=TEAM_PLACES)


@app.errorhandler(404)
def page_not_found(error):
    logger.warning("Page not found: %s", error)
    return "Page not found", 404


@app.errorhandler(500)
def internal_server_error(error):
    logger.error("Internal server error: %s", error)
    return "Internal server error", 500
