import unittest
import calc

class TestCalc (unittest.TestCase):
    
    def test_add(self):
        result = calc.add(3,7)
        self.assertEqual(result,10)
        
