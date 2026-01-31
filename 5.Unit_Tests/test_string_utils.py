import unittest
import string_utils

class TestStringUtils (unittest.TestCase):
    
    def test_reverse_string(self):
        result = string_utils.reverse_string('mochi')
        self.assertEqual(result,'ihcom')
        
    def test_capitalize_string(self):
        result_cap = string_utils.capitalize_string('mochi')
        self.assertEqual(result_cap,'Mochi')
    
    def test_is_capitalized(self):
        result_CAP = string_utils.is_capitalized('mochi')
        self.assertEqual(result_CAP,'MOCHI')
        
if __name__ == '__main__':
    unittest.main()