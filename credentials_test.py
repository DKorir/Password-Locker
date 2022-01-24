import unittest #importing unnittest module
from credentials import Credentials # impoting the credentials class

class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("github","DKorir","0798286377Dd","dommykiprono76@gmail.com") # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"github")
        self.assertEqual(self.new_credentials.user_name,"DKorir")
        self.assertEqual(self.new_credentials.password,"0798286377Dd")
        self.assertEqual(self.new_credentials.email,"dommykiprono76@gmail.com")


    def test_save_credentials(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credentials.save_credentials() # saving the new account
        self.assertEqual(len(Credentials.credentials_list),1) 

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","123456","user@gmail.com") # new credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credentials(self):
        """
        test delete credentials to test if we can remove fromof credential list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","123456","user@gmail.com") # credentials
        test_credentials.save_credentials()
        self.new_credentials.     delete_credentials()# Deleting an credentials object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_credentials_name(self):
        """
        test to check if we can find an credebtials by credentials_name and display information
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","123456","user@gmail.com") # new credentials
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_name("Test")
        self.assertEqual(found_credentials.email,test_credentials.email)
    

if __name__ == '__main__':
    unittest.main()