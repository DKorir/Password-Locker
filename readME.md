# Password Locker

## Built By [Dominic Korir](https://github.com/DKorir/Password-Locker)

## Description
Password Locker is a terminal run python application that allows users to store details: usernames and passwords of their various accounts.

## User Stories
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display guides for navigation | **In terminal: $./run.py** | Hello Welcome to your Pass Word Locker. What is your name? (once you enter your nname):Use these known short codes to operate : SU -> SIGN UP.  DA -> Display your account.  LN ->LOGIN.  ex ->exit Pass Word Locker. |
| Display prompt for creating an account | **Enter: SU** | Enter account name, user name password and email .|
| Display prompt for login in | **Enter: LN** | Enter your account password to login |
| Once logged in | **You are now logged in to your  account** |  Use these short codes:CA -> Create new credential.DC -> Display your credentials list.  ex ->Log out your credentials account. |
| Display prompt for creating a credential | **Enter: CA** | Create new credential, Credential name: and password |
| Display a list of credentials | **Enter: DC** | Prints a list of saved credentials |
| Log out account  | **Enter: ex** | You have logged out your  account |

* To completely interact with this application,you will need to sign up to have an account,then login to your account and work in there.

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* internet connection
* For linux/ubuntu users : Git


### Cloning
* In your terminal:
        
        $ git clone https://github.com/DKorir/Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ ./run.py
      
        
## Testing the Application
* To run the tests for the class file and check if it functions well:

        $ python3.6 credentials_test.py
        
## Technologies Used
* Python3.8.10

## License
MIT &copy;2022 [Dominic Korir](https://github.com/DKorir/Password-Locker)
