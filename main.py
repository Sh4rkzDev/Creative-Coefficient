import unittest
import triangle

class TestTriangle(unittest.TestCase):

    def test_single_color(self):
        self.assertEqual(triangle.triangle("B"), "B")
    
    def test_two_colors(self):
        self.assertEqual(triangle.triangle("GB"), "R")
        self.assertEqual(triangle.triangle("BB"), "B")
        self.assertEqual(triangle.triangle("RG"), "B")
    
    def test_three_colors(self):
        self.assertEqual(triangle.triangle("RRR"), "R")
        self.assertEqual(triangle.triangle("RRB"), "B")
        self.assertEqual(triangle.triangle("RGB"), "G")

    def test_medium_row(self):
        self.assertEqual(triangle.triangle("RBRGBRB"), "G")

    def test_large_row(self):
        self.assertEqual(triangle.triangle("RBRGBRBGGRRRBGBBBGG"), "G")

if __name__ == "__main__":
    unittest.main()