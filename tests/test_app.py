# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # Home page content and navigation
        assert "Meet the Team" in html
        assert "Adam Maatouk" in html
        assert "Amar Kanakamedala" in html
        assert "Gabriel Changamire" in html
        assert "Home" in html
        assert "Work" in html
        assert "Hobbies" in html
        assert "Map" in html
        assert "Education" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # POST a new timeline post
        post_response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!",
        })
        assert post_response.status_code == 200
        assert post_response.is_json
        post_json = post_response.get_json()
        assert post_json["name"] == "John Doe"
        assert post_json["email"] == "john@example.com"
        assert post_json["content"] == "Hello world, I'm John!"

        # GET should now return the post we created
        get_response = self.client.get("/api/timeline_post")
        assert get_response.status_code == 200
        get_json = get_response.get_json()
        assert len(get_json["timeline_posts"]) == 1
        assert get_json["timeline_posts"][0]["name"] == "John Doe"
        assert get_json["timeline_posts"][0]["email"] == "john@example.com"
        assert get_json["timeline_posts"][0]["content"] == "Hello world, I'm John!"

        # Timeline page (Timeline page didn't exist yet, so I created it for this test)
        page_response = self.client.get("/timeline")
        assert page_response.status_code == 200
        page_html = page_response.get_data(as_text=True)
        assert "<title>Timeline</title>" in page_html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
