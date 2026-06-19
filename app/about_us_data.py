# About Us content, kept out of __init__.py so teammates can update bios and links
# without touching route or template logic (same pattern as education_data.py).
#
# Each member needs:
#   - name:    full display name
#   - photo:   filename in app/static/img/
#   - role:    short title shown under the name
#   - bio:     one-paragraph personal summary
#   - color:   accent colour for the card top border
#   - links:   list of {"label", "url"} for GitHub, LinkedIn, etc.

TEAM_ABOUT_US = [
    {
        "name": "Amar Kanakamedala",
        "photo": "amar-kanakamedala.png",
        "role": "MLH Fellow · Software Engineer",
        "color": "#ff6b6b",
        "bio": (
            "Amar is a Computer Science student at Rice University with a passion for "
            "machine learning and systems programming. He has published research at ICLR "
            "on novel LLM training methods and loves building tools that make developers' "
            "lives easier."
        ),
        "links": [
            {"label": "GitHub", "url": "https://github.com/amarka8"},
            {"label": "LinkedIn", "url": "https://linkedin.com/in/amar-kanakamedala/"},
        ],
    },
    {
        "name": "Adam Maatouk",
        "photo": "adam-maatouk.png",
        "role": "MLH Fellow · Software Engineer",
        "color": "#4ecdc4",
        "bio": (
            "Adam is a Computer Engineering student at Concordia University in Montreal. "
            "He has a deep interest in building Software. "
            "Outside of code he can usually be found behind a camera lens or lifting."
        ),
        "links": [
            {"label": "GitHub", "url": "https://github.com/AdamMTK-NB"},
            {"label": "LinkedIn", "url": "https://www.linkedin.com/in/adammaatouk/"},
        ],
    },
    {
        "name": "Gabriel Changamire",
        "photo": "gabriel-changamire.png",
        "role": "MLH Fellow · Software Engineer",
        "color": "#c792ea",
        "bio": (
            "Gabriel is a Computer Science student at Bellevue College and a Mentors in Tech "
            "(MinT) Fellow. He enjoys exploring new "
            "places, reading broadly, and competing on the basketball court."
        ),
        "links": [
            {"label": "GitHub", "url": "https://github.com/gabrielchangamire-arch"},
            {"label": "LinkedIn", "url": "https://www.linkedin.com/in/gabriel-changamire/"},
        ],
    },
]