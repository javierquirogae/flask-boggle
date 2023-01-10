from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('game', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
     

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess["game"] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/guess?word=cat')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/guess?word=impossible')
        self.assertEqual(response.json['result'], 'not-found-on-board')

    def non_english_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get('/guess?word=fsjdakfkldsfjdslkfjdlksf')
        self.assertEqual(response.json['result'], 'not-a-valid-word')

