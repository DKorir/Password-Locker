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
    
    

if __name__ == '__main__':
    unittest.main()