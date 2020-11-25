from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from service_two import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_lion(self):
        with patch('requests.get') as g:
            g.return_value.text = "0"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Lion', response.data)
    
    
    def test_wolf(self):
        with patch('requests.get') as g:
            g.return_value.text = "1"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Wolf', response.data)
            
    def test_crow(self):
        with patch('requests.get') as g:
            g.return_value.text = "2"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Crow', response.data)
    
    def test_elephant(self):
        with patch('requests.get') as g:
            g.return_value.text = "3"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Elephant', response.data)
     
     def test_mouse(self):
        with patch('requests.get') as g:
            g.return_value.text = "4"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Mouse', response.data)
      
      def test_snake(self):
        with patch('requests.get') as g:
            g.return_value.text = "5"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Snake', response.data)
            
       def test_frog(self):
        with patch('requests.get') as g:
            g.return_value.text = "6"

            response = self.client.get(url_for('animal'))
            self.assertIn(b'Frog', response.data)
     
     
