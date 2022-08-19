import unittest
from huffman_algo import HuffmanAlgo

class TestHuffmanAlgo(unittest.TestCase):
    def setUp(self):
        self.huffman_algo_encoding = HuffmanAlgo("AAABBC")
        self.huffman_algo_decoding = HuffmanAlgo(b'001B1C1A  \x07\xe0\x01')
    
    def test_calculate_propability(self):
        test_symbols = {
          "A": 3,
          "B": 2,
          "C": 1
        }
        self.assertEqual(self.huffman_algo_encoding.calculate_probability(), test_symbols)

    def test_huffman_encoding(self):
        encoding, tree = self.huffman_algo_encoding.huffman_encoding()
        self.assertEqual(encoding, b'\x07\xe0\x01')
        self.assertEqual(tree, b'001B1C1A  ')

    def test_huffman_decoding(self):
        self.assertEqual(self.huffman_algo_decoding.huffman_decoding(), "AAABBC")