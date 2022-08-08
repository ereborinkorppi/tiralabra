import unittest
from lz_seventyeight import LzSeventyeight

class TestLzSeventyeight(unittest.TestCase):
    def setUp(self):
        self.compress = "AAABBC"
        self.decompress = b'\x80\x03]q\x00(X\x01\x00\x00\x00Aq\x01M\x00\x01X\x01\x00\x00\x00Bq\x02h\x02X\x01\x00\x00\x00Cq\x03e.'
        self.lz_seventyeight_compress = LzSeventyeight(self.compress)
        self.lz_seventyeight_decompress = LzSeventyeight(self.decompress)

    def test_compress(self):
        self.assertEqual(self.lz_seventyeight_compress.compress(),
                         b'\x80\x03]q\x00(X\x01\x00\x00\x00Aq\x01M\x00\x01X\x01\x00\x00\x00Bq\x02h\x02X\x01\x00\x00\x00Cq\x03e.')

    def test_decompress(self):
        self.assertEqual(self.lz_seventyeight_decompress.decompress(), "AAABBC")