import unittest
from huffman_algo import HuffmanAlgo

class TestHuffmanAlgo(unittest.TestCase):
    def setUp(self):
        self.data = "aaabbc"
        self.huffman_algo = HuffmanAlgo(self.data)
    
    def test_calculate_propability(self):
        test_symbols = {
          "a": 3,
          "b": 2,
          "c": 1
        }
        self.assertEqual(self.huffman_algo.calculate_probability(), test_symbols)

    def test_huffman_encoding(self):
        encoding, tree = self.huffman_algo.huffman_encoding()
        self.assertEqual(encoding, "111000001")