from unittest import TestCase
from src.thearena.main import pick_a_pair

class TestPickapair(TestCase):

    def test_function_returns_random_pairs(self):
        self.assertNotEqual(pick_a_pair(), pick_a_pair())
        self.assertNotEqual(pick_a_pair(), pick_a_pair())
        self.assertNotEqual(pick_a_pair(), pick_a_pair())
        self.assertNotEqual(pick_a_pair(), pick_a_pair())
        self.assertNotEqual(pick_a_pair(), pick_a_pair())
