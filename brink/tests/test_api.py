from unittest import TestCase

import brink
from brink.client import BrinkAPI

class TestApi(TestCase):

    def test_set_token(self):
        
        api = BrinkAPI('token1')
        self.assertTrue( api.token == 'token1' )
