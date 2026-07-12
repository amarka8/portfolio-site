import logging
import os

from flask import Flask, render_template
from dotenv import load_dotenv

# Hobby content lives in its own module so teammates can update images and names
# without touching route or template logic (Single Responsibility).
from .hobbies_data import TEAM_HOBBIES
from .work_history_data import TEAM_WORK_HISTORY
from .places_data import TEAM_PLACES
from .education_data import TEAM_EDUCATION
from .about_us_data import TEAM_ABOUT_US

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# New nav items only need an entry here once a matching route exists.
NAV_PAGES = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "work", "label": "Work"},
    {"endpoint": "hobbies", "label": "Hobbies"},
    {"endpoint": "map_page", "label": "Map"},
    {"endpoint": "education", "label": "Education"},
]

app = Flask(__name__)

mydb = 
MYSQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)


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
        team_about=TEAM_ABOUT_US,
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


@app.route("/education")
def education():
    logger.info("Serving education page")
    return render_template("education.html", title="Education", team_education=TEAM_EDUCATION)


@app.errorhandler(404)
def page_not_found(error):
    logger.warning("Page not found: %s", error)
    return "Page not found", 404


@app.errorhandler(500)
def internal_server_error(error):
    logger.error("Internal server error: %s", error)
    return "Internal server error", 500
