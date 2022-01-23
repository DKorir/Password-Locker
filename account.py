import email
from typing_extensions import Self


class Account:
    """
    Class that generates instances of users.
    """
    account_list = [] #empty account list
    
    def __init__(self,account_name,user_name,password,email):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email