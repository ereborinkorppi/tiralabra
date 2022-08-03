import unittest
from huffman_algo import HuffmanAlgo

class TestHuffmanAlgo(unittest.TestCase):
    def setUp(self):
        self.data = "AAABBC"
        self.huffman_algo = HuffmanAlgo(self.data)
    
    def test_calculate_propability(self):
        test_symbols = {
          "A": 3,
          "B": 2,
          "C": 1
        }
        self.assertEqual(self.huffman_algo.calculate_probability(), test_symbols)

    def test_huffman_encoding(self):
        encoding, tree = self.huffman_algo.huffman_encoding()
        self.assertEqual(encoding, b'\x07\xe0\x01')

    def test_encode_tree(self):
        encoding, tree = self.huffman_algo.huffman_encoding()
        self.assertEqual(self.huffman_algo.encode_tree(tree), "001B1C1A")

    def test_huffman_decoding(self):
        encoding, tree = self.huffman_algo.huffman_encoding()
        self.assertEqual(self.huffman_algo.huffman_decoding(encoding, tree), "AAABBC")