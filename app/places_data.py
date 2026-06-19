# Globe content. Coordinates are (lat, lng) in decimal degrees.
# Each member keeps the same colour as their work history so points, arcs, and
# the side panel all stay visually linked. The "tag" is a short nickname/fun fact
# for the place so the popup feels personal instead of generic.
#
# For country-only entries we pin the capital and label it by the country.

TEAM_PLACES = [
    {
        "member": "Amar Kanakamedala",
        "color": "#ff6b6b",
        "places": [
            {"name": "Houston, Texas", "lat": 29.7604, "lng": -95.3698, "tag": "Space City"},
            {"name": "New York City", "lat": 40.7128, "lng": -74.0060, "tag": "The city that never sleeps"},
            {"name": "Dallas, Texas", "lat": 32.7767, "lng": -96.7970, "tag": "Big D"},
            {"name": "Paris, France", "lat": 48.8566, "lng": 2.3522, "tag": "The City of Light"},
            {"name": "Antananarivo, Madagascar", "lat": -18.8792, "lng": 47.5079, "tag": "Highland capital of Madagascar"},
        ],
    },
    {
        "member": "Adam Maatouk",
        "color": "#4ecdc4",
        "places": [
            {"name": "Montreal, Canada", "lat": 45.5019, "lng": -73.5674, "tag": "Festival city of Quebec"},
            {"name": "Toronto, Canada", "lat": 43.6532, "lng": -79.3832, "tag": "The 6ix"},
            {"name": "Dominican Republic", "lat": 18.4861, "lng": -69.9312, "tag": "Oldest city in the Americas"},
            {"name": "Lebanon", "lat": 33.8938, "lng": 35.5018, "tag": "Beirut — Paris of the Middle East"},
            {"name": "Ottawa, Canada", "lat": 45.4215, "lng": -75.6972, "tag": "Canada's capital"},
        ],
    },
    {
        "member": "Gabriel Changamire",
        "color": "#c792ea",
        "places": [
            {"name": "Seattle, Washington", "lat": 47.6062, "lng": -122.3321, "tag": "The Emerald City"},
            {"name": "Hilo, Hawaii", "lat": 19.7297, "lng": -155.0900, "tag": "Big Island gateway to the volcanoes"},
            {"name": "Mazatlán, Mexico", "lat": 23.2494, "lng": -106.4111, "tag": "Pearl of the Pacific"},
            {"name": "Harare, Zimbabwe", "lat": -17.8252, "lng": 31.0335, "tag": "The Sunshine City"},
            {"name": "Edmonton, Canada", "lat": 53.5461, "lng": -113.4938, "tag": "Gateway to the North"},
        ],
    },
]
