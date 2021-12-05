import random
from unittest import TestCase
from utils.generate_chain import generate_chain


class TestGenerateChain(TestCase):

    def test_chain_generation(self):
        random.seed(1)
        data = {
            'a': ['b', 'c', 'd'],
            'b': ['c'],
            'c': ['a', 'd'],
            'd': ['a', 'c']
        }
        expected_chain = {
            'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'a'
        }
        actual_chain = generate_chain(data)
        self.assertEqual(expected_chain, actual_chain)
