class Credentials:
    """
    class that generates new instances of users
    """
    credentials_list = [] #empty credentials list

    def __init__(self,credentials_name,user_name,
    password,email):
        self.credentials_name = credentials_name
        self.usr_name = user_name
        self.password = password
        self.email = email