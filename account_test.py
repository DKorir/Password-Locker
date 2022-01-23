import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("Domie","Dkorir","123456","dk@gmail.com")
    def test_init(self):
        self.assertEqual(self.new_account.account_name,"Domie")
        self.assertEqual(self.new_account.user_name,"Dkorir")
        self.assertEqual(self.new_account.password,"123456")
        self.assertEqual(self.new_account.email,"dk@gmail.com")

if __name__ == '__main__':
    unittest.main()




