# Education content, kept out of __init__.py so teammates can add degrees
# without touching route or template logic (same pattern as work_history_data.py).
#
# Each member has a list of degrees, newest first. Each degree needs:
#   - institution:  school name
#   - degree:       degree type and field (e.g. "B.S. Computer Science")
#   - dates:        human-readable date range
#   - location:     where the school is based
#   - gpa:          optional GPA string
#   - highlights:   list of short bullet strings (awards, clubs, relevant coursework, etc.)
#   - link:         optional {"label", "url"} for the school or program

TEAM_EDUCATION = [
    # {
    #     "member": "Adam Maatouk",
    #     "color": "#4ecdc4",
    #     "degrees": [
    #         {
    #             "institution": "Concordia University",
    #             "degree": "B.Eng. Computer Engineering",
    #             "dates": "May 2025 – May 2029",
    #             "location": "Montreal, Quebec, Canada",
    #             "highlights": [
    #                 "Relevant coursework: Operating Systems, Distributed Systems, Software Architecture",
    #                 "Member of Concordia's Software Engineering Student Society",
    #             ],
    #             "link": {"label": "concordia.ca", "url": "https://www.concordia.ca"},
    #         },
    #         {
    #             "institution": "College Maisonneuve",
    #             "degree": "Techniques de l'Informatique - Developpement D'Applications",
    #             "dates": "August 2022 – May 2025",
    #             "location": "Montreal, Quebec, Canada",
    #             "highlights": [
    #                 "Relevant coursework: Programming, Database, Networking, Web Development",
    #                 "91% average GPA in the program and mandatory internship",
    #             ],
    #             "link": {"label": "cmaisonneuve.qc.ca", "url": "https://www.cmaisonneuve.qc.ca"},
    #         },
    #     ],
    # },
    {
        "member": "Amar Kanakamedala",
        "color": "#ff6b6b",
        "degrees": [
            {
                "institution": "Rice University",
                "degree": "B.S. Computer Science",
                "dates": "Aug 2023 – May 2027",
                "location": "Houston, Texas",
                "gpa": "3.71 / 4.0",
                "highlights": [
                    "Relevant coursework: Algorithms, Systems, Machine Learning, Databases",
                    "Publication at ICLR proposing a new way to train LLMs",
                ],
                "link": {"label": "rice.edu", "url": "https://www.rice.edu"},
            },
        ],
    }
    # ,
    # {
    #     "member": "Gabriel Changamire",
    #     "color": "#c792ea",
    #     "degrees": [
    #         {
    #             "institution": "Bellevue College",
    #             "degree": "B.S. Computer Science",
    #             "dates": "2025 – 2027",
    #             "location": "Bellevue, Washington",
    #             "gpa": "3.8 / 4.0",
    #             "highlights": [
    #                 "Mentors in Tech (MinT) Fellow",
    #                 "Relevant coursework: Data Structures, Java, Python, Discrete Mathematics",
    #                 "Academic Excellence Award recipient",
    #             ],
    #             "link": {"label": "bellevuecollege.edu", "url": "https://www.bellevuecollege.edu"},
    #         },
    #         {
    #             "institution": "Bellevue College",
    #             "degree": "A.S. Computer Science",
    #             "dates": "Sep 2023 – Jun 2025",
    #             "location": "Bellevue, Washington",
    #             "highlights": [
    #                 "Mentors in Tech (MinT) Fellow",
    #                 "Relevant coursework: Data Structures, Java, Python, Discrete Mathematics",
    #                 "Academic Excellence Award recipient",
    #             ],
    #             "link": {"label": "bellevuecollege.edu", "url": "https://www.bellevuecollege.edu"},
    #         },
    #     ],
    # },
]