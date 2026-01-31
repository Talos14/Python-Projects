import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount(initial_balance=100)
    
    def tearDown(self):
        self.account = None
    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance,100)
    
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance,150)
    
    def test_zero_deposit_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    
if __name__ == "__main__":
    unittest.main()