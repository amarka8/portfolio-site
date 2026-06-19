# Work-experience content, kept out of __init__.py so teammates can edit roles
# without touching route or template logic (same pattern as hobbies_data.py).
#
# Each member has a list of roles, newest first. Each role needs:
#   - title:    job title
#   - org:      company / organization
#   - kind:     employment type (Internship, Part-time, Seasonal, ...)
#   - dates:    human-readable date range
#   - location: where the role was based
#   - summary:  one short paragraph describing the work
#   - link:     optional {"label", "url"} shown as a reference

TEAM_WORK_HISTORY = [
    {
        "member": "Amar Kanakamedala",
        "color": "#ff6b6b",
        "roles": [
            {
                "title": "Software Engineer Intern",
                "org": "OmniScience",
                "kind": "Internship",
                "dates": "Jun 2026 – Present",
                "location": "Houston, Texas · Hybrid",
                "summary": "Building agentic applications for life science organizations.",
            },
            {
                "title": "Software Development Intern",
                "org": "Amazon Web Services (AWS)",
                "kind": "Internship",
                "dates": "Jun 2026 – Present",
                "location": "Bellevue, Washington · On-site",
                "summary": "Incoming Fall 2026.",
            },
            {
                "title": "Production Engineering Fellow",
                "org": "Meta & Major League Hacking",
                "kind": "Internship",
                "dates": "Jun 2026 – Present",
                "location": "Remote",
                "summary": "Selected for the highly competitive Meta–MLH Production Engineering "
                           "Fellowship (2.5% acceptance rate); committing 20 hrs/week to hands-on "
                           "systems development, open-source project contribution, mentorship, and "
                           "collaboration.",
            },
            {
                "title": "Research Assistant",
                "org": "RUSHLab",
                "kind": "Part-time",
                "dates": "Oct 2024 – Jun 2026",
                "location": "Houston, Texas · On-site",
                "summary": "Applied randomization and hashing algorithms to improve LLMs "
                           "(co-advised by Sahil Joshi and Professor Anshumali Shrivastava).",
                "link": {"label": "Paper on OpenReview", "url": "https://openreview.net/forum?id=RR8Lh8RHgA"},
            },
            {
                "title": "Software Engineer",
                "org": "Rice University's Baker Institute for Public Policy",
                "kind": "Internship",
                "dates": "Oct 2024 – May 2025",
                "location": "Houston, Texas · On-site",
                "summary": "Built semantic search capabilities around government documents for public use.",
                "link": {"label": "Project on GitHub", "url": "https://github.com/sahiljoshi515/Baker_Project/tree/main"},
            },
            {
                "title": "Research Intern",
                "org": "George Mason University – College of Science",
                "kind": "Internship",
                "dates": "Jun 2023 – Aug 2023",
                "location": "Fairfax County, Virginia · Hybrid",
                "summary": "Worked with one intern and two mentors to produce the paper "
                           "“Studying the Influence of Income Differences and Credit History on "
                           "Racial Disparities in the Mortgage Market using Machine Learning,” with "
                           "the abstract to be published in GMU's Journal of Student Scientists' Research.",
            },
            {
                "title": "Summer Intern",
                "org": "Lyne.ai",
                "kind": "Internship",
                "dates": "Jun 2022 – Jul 2022",
                "location": "United States · Remote",
                "summary": "Worked with CTO Saatvik Mohan and co-founder Hans Dekker to build a "
                           "lead-sheet formatter in Google Apps Script in 177 lines of code.",
            },
        ],
    },
    {
        "member": "Adam Maatouk",
        "color": "#4ecdc4",
        "roles": [
            {
                "title": "Meta Production Engineering Fellow",
                "org": "Meta & Major League Hacking",
                "kind": "Internship",
                "dates": "Jun 2026 – Present",
                "location": "North America · Remote",
                "summary": "Mastering core Production Engineering (PE) and Site Reliability Engineering "
                           "(SRE) concepts — system architecture, Linux internals, network protocols, "
                           "and scripting. Collaborating on open-source projects and simulated production "
                           "environments to optimize performance, reliability, and scalability, working "
                           "with mentors and peers using Git, code reviews, and post-mortems.",
            },
            {
                "title": "Founder",
                "org": "Stealth Startup",
                "kind": "Self-employed",
                "dates": "Mar 2025 – Present",
                "location": "Montreal, Quebec, Canada · Hybrid",
                "summary": "Building a new venture (currently in stealth).",
            },
            {
                "title": "Software Engineer",
                "org": "Athena AI",
                "kind": "Internship",
                "dates": "Mar 2025 – Jul 2025",
                "location": "Montreal, Quebec, Canada · Remote",
                "summary": "Shipped production React + TypeScript features for a startup with 3M+ users: "
                           "improved load times 35% and UI responsiveness 28%; built Python AI evaluation "
                           "pipelines (+18% accuracy) and real-time model tuning (−22% low-confidence "
                           "responses); cut recurring user-reported bugs 25%; supported live demos at "
                           "World Summit AI.",
            },
            {
                "title": "Material Handler",
                "org": "Tanguay",
                "kind": "Seasonal",
                "dates": "Jun 2021 – Sep 2025",
                "location": "Montreal, Quebec, Canada · On-site",
                "summary": "Reduced product damage 15% by standardizing loading for 50+ units/shift; "
                           "improved staging efficiency 20%; maintained 100% on-time shipment readiness; "
                           "increased loading throughput 18%.",
            },
            {
                "title": "Sales Associate",
                "org": "Best Buy",
                "kind": "Seasonal",
                "dates": "Oct 2018 – Feb 2021",
                "location": "Montreal, Quebec, Canada · On-site",
                "summary": "Increased accessory sales 25%, hit 110% of quarterly targets, and reduced "
                           "transaction errors 30% through careful POS verification.",
            },
            {
                "title": "Camp Instructor",
                "org": "Les Fourchettes de l'Espoir",
                "kind": "Seasonal",
                "dates": "Jun 2019 – Aug 2020",
                "location": "Montreal, Quebec, Canada · On-site",
                "summary": "Supervised groups of 20+ youth with zero safety incidents, improved engagement "
                           "20%, and streamlined daily setup workflows.",
            },
        ],
    },
    {
        "member": "Gabriel Changamire",
        "color": "#c792ea",
        "roles": [
            {
                "title": "Production Engineering Fellow",
                "org": "Meta × Major League Hacking (MLH)",
                "kind": "Fellowship",
                "dates": "Summer 2026 – Present",
                "location": "Remote",
                "summary": "Selected for the MLH Fellowship Production Engineering track, sponsored by "
                           "Meta. Hands-on PE/SRE work: infrastructure, monitoring, automation, and the "
                           "operational practices that keep large-scale systems reliable.",
            },
            {
                "title": "Computer Science Tutor",
                "org": "Bellevue College Academic Success Center & Writing Lab",
                "kind": "Part-time",
                "dates": "May 2025 – Present",
                "location": "Bellevue, Washington · On-site",
                "summary": "Tutor students in CS, Python, Java, data structures, math, English, and "
                           "economics, helping them build strong problem-solving skills and clear "
                           "technical reasoning.",
            },
            {
                "title": "Mentors in Tech (MinT) Fellow",
                "org": "Bellevue College MinT Program",
                "kind": "Fellowship",
                "dates": "2025 – Present",
                "location": "Bellevue, Washington",
                "summary": "Paired with industry mentors Spencer Nelson (Principal UX Engineer & Manager, "
                           "Microsoft) and Starlight Romero (Principal Platform Engineer) to build "
                           "technical skills and grow a professional network.",
            },
        ],
    },
]
