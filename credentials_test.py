import unittest #importing unnittest module
from credentials import Credentials # impoting the credentials class

class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Domie","Korir","dk2030","dk@gmail.com") # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"domie")
        self.assertEqual(self.new_credentials.usr_name,"korir")
        self.assertEqual(self.new_credentials.password,"dk2030")
        self.assertEqual(self.new_credentials.email,"dk@gmail.com")

if __name__ == '__main__':
    unittest.main()