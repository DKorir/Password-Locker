import unittest # Importing the unittest module
from account import Account # Importing the account class
class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Domie","Korir","123456","domi@gmail.com") # create Account object