from flask import url_for
from flask_testing import TestCase

from service_two import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):

    def test_animal(self):
        animals = [b"Lion", b"Wolf", b"Crow", b"Elephant", b"Mouse", b"Snake", b"Frog"]
        response = self.client.get(url_for('animal'))
        self.assertIn(response.data, animals)

    def test_noise_lion(self):
        response = self.client.post(
            url_for('noise'),
            data="Lion",
            follow_redirects=True
        )
        self.assertIn(b'Roar', response.data)
    
    def test_noise_wolf(self):
        response = self.client.post(
            url_for('noise'),
            data="Wolf",
            follow_redirects=True
        )
        self.assertIn(b'Howl', response.data)

    def test_noise_elephant(self):
        response = self.client.post(
            url_for('noise'),
            data="Elephant",
            follow_redirects=True
        )
        self.assertIn(b'Trumpet', response.data)
    
    def test_noise_crow(self):
        response = self.client.post(
            url_for('noise'),
            data="Crow",
            follow_redirects=True
        )
        self.assertIn(b'Caw', response.data)

    def test_noise_mouse(self):
        response = self.client.post(
            url_for('noise'),
            data="Mouse",
            follow_redirects=True
        )
        self.assertIn(b'Squeak', response.data)

    def test_noise_snake(self):
        response = self.client.post(
            url_for('noise'),
            data="Snake",
            follow_redirects=True
        )
        self.assertIn(b'Hiss', response.data)

    def test_noise_frog(self):
        response = self.client.post(
            url_for('noise'),
            data="Frog",
            follow_redirects=True
        )
        self.assertIn(b'Croak', response.data)

    
     
