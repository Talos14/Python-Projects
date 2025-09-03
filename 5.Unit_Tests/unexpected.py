import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b


class TestUnexpected(unittest.TestCase):
    
    def test_get_sqrt(self):
        result = get_sqrt(64)
        self.assertEqual(result,8)
    
    def test_get_negative_sqrt(self):
        with self.assertRaises(ValueError):
            get_sqrt(-64)
    
    def test_divide(self):
        result = divide(144, 12)
        self.assertEqual(result,12)
        
    def test_by_zero_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(144,0)
    
    
if __name__ == '__main__':
    unittest.main()