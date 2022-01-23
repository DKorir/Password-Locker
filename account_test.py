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

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1) 



if __name__ == '__main__':
    unittest.main()




