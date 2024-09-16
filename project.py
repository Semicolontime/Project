import re
import cowsay
import sys
import requests
import json
import pyttsx3
class Wallet:
    def __init__(self , balance =0  , amount = 0) -> None:
        self._balance = balance
        self._amount = amount
    def __str__(self) -> str:
        return self._balance
    def all(self):
        return self._amount
    def deposit(self , n):
        self._balance = self._balance + n 
    def withdraw(self , n):
        if n <= self._balance:
            self._balance -= n
        else:
            print("Insufficient funds")
    @property
    def balnce(self):
         return self._balance  
    @balnce.setter
    def balnce(self , balance):
        self._balance = balance
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self , amount):
        self._amount = amount
class Jar:
    def __init__(self , capacity = 0 , size = 0) -> None:
        self._capacity = capacity
        self._size = size
    def __str__(self) -> str:
        return self._size * "🍪"
    def all(self):
        return self._capacity
    def deposite(self , n):
        self._size += n
    def withraw(self , n):
        self._size -= n
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self , capacity):
        self._capacity = capacity
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self , size):
        self._size = size
def main():
    sign_up()
    options()
def sign_up():
    global user_information
    user_information = {}
    username_input = input("Enter Username:\n ")
    user_information.setdefault("username" , username_input)
    while True:
        password_input = input("Enter Password: \n")
        if re.search(r'^(?=.*\d)(?=.*[@!#$%^&*()_+{}|:"<>?`~\[\];,./\-]).{8,}$' , password_input):
            user_information.setdefault("password" , password_input)
            break
        else:
            print("Password must be at least 8 characters long and contain at least one number and one symbol (such as !, @, #, etc.)")
            continue
def log_in():
    global user_information
    while True:
        print("Please Log in to your account!")
        username_input = input("Enter Username:\n ")
        if username_input == user_information["username"]:
            while True:
                password_input = input("Enter Password:\n ")
                if password_input == user_information["password"]:
                    options()
                    break
                else:
                    print("Your password incorrect , pls re enter password")
                    forget_pass = int(input("If you forgot your password pls press 1 and enter! or you want enter your password agian press 2! \n"))
                    if forget_pass == 1:
                        forgot_password()
                    elif forget_pass == 2:
                        continue
        else:
            print("your username has not register pls register first! you go to register page!")
            sign_up()
            break
def forgot_password():
    global user_information
    phone_option = input("Please enter your phone number to send an sms to your phone like +989123456789 \n")
    test_phonenumber = re.search(r'^(\+98|0)?9\d{9}$' , phone_option)
    if test_phonenumber:
        sms_verification = int(input(f"Please enter the code we sent to your phone number : {phone_option} , if you want edit phone number enter number 1 ! (The code we sent: 232323) \n"))
        if sms_verification == 232323:
            print(f"your password is {user_information["password"]}")
        elif sms_verification == 1:
            forgot_password()
def options():
    wallet = Wallet() 
    jar = Jar()
    while True:
        print(line())
        print("choose any option!")
        print(line())
        print("1-use calcultor!")
        print("2-draw ypur word in shape of animal!")
        print("3-charge your wallet")
        print("4-cookie maker")
        print("5-The current price of Bitcoin")
        print("6-Log out")
        print(line())
        try:
            choose_input = int(input("what will you choose?\n"))
        except ValueError:
            print(line())
            print("Please enter number not string!")
            continue   
        if choose_input == 1:
            print(line())
            print("1-multiplication")
            print("2-division")
            print("3-plural")
            print("4-subtraction")
            print("5-Back to the main menu")
            print(line())
            try:
                user_cal_input:str = input("What calculations do you want?")
                if user_cal_input == "5":
                    options()
            except Exception:
                print("Just enter the number")
                continue
            print( use_calculator(user_cal_input))
                
                
        elif choose_input == 2:
            print(line())
            print("Say somthing and choose animal to drow with your words")
            print("1-cow")
            print("2-t-rex")
            print("3-daemon")
            print("4-dragon")
            print("5-octopus")
            print(line())
            cow_input : str = input("number you want: ")
            cow_string : str = input("enter your words: ")
            cow_say(cow_input , cow_string )
        elif choose_input == 3:
            print(line())
           
            while True:
                print("Welcome to virtual bank!")
                print("What do you want to do?")
                print("1-view Balance")
                print("2-deposite balance")
                print("3-withdraw balance")
                print("4-Back to the main menu")
                print(line())
                wallet_input = int(input())
                print(line())
                if wallet_input == 1:
                    print(f"wallet balance : {wallet.__str__()}")
                    print(line())
                elif wallet_input ==2:
                    Increase_account_money = int(input("Please enter the amount you want to add to your account: \n"))
                    wallet.deposit(Increase_account_money)
                    print(line())
                    print(f"wallet balance : {wallet.__str__()}")
                    print(line())
                elif wallet_input ==3:
                    decrese_account_money = int(input("Please enter the amount you want to withdraw to your account: \n"))
                    wallet.withdraw(decrese_account_money)
                    print(line())
                    print(f"wallet balance : {wallet.__str__()}")
                    print(line())
                elif wallet_input == 4:
                    break
            
        elif choose_input == 4:
            while True:
                print(line())
                print("Welcome to cookie bank!")
                print(line())
                print("1-cookie bank")
                print("2-deposite cookie!")
                print("3-withdraw cookie")
                print("4-Back to the main menu")
                print(line())
                print("What will you choose?")
                cookie_input = int(input())
                if cookie_input == 1:
                    print(line())
                    print(f"amount cookie you have: {len(jar.__str__())}")
                elif cookie_input ==2:
                    print(line())
                    cookie_deposite =int(input("How much you want deposite: "))
                    print(line())
                    jar.deposite(cookie_deposite)
                    print(f"Amount of cookies you have: {jar}")
                elif cookie_input == 3:
                    cookie_withdraw =int(input("How much you want withdraw: "))
                    print(line())
                    jar.withraw(cookie_withdraw)
                    print(f"Amount of cookies you have: {jar}")
                elif cookie_input == 4:
                    break
        elif choose_input == 5:
            while True:
                print(line())
                print("Welcome to bitcoin price")
                print(line()) 
                print("1-Print Botcoin price!") 
                print("2-Read Bitcoin price!")
                print("3-Back to the main menu")
                print(line())
                bitcoin_input = int(input("What wil you choose?\n"))
                if bitcoin_input ==1:
                    print(line())
                    print(f"{bitcoin()} $")
                elif bitcoin_input ==2:
                    engine = pyttsx3.init()
                    print(line())
                    print(f"{bitcoin()} $")
                    engine.say(f"{bitcoin()} dollars")
                    engine.runAndWait()
        elif choose_input == 6:
            log_in()
def use_calculator(user_cal_input : str) -> int:
    if re.search("[0-9]+" , user_cal_input):
        user_cal_input = int(user_cal_input)
        if user_cal_input not in [1,2,3,4]:
            return "Please choose between 1 and 4"
        if user_cal_input ==1:
            number1 , number2 = input("enter your numbers with space: \n").split(" ")
            number1 = int(number1)
            number2 = int(number2)
            return number1 * number2
        if user_cal_input ==2:
            number1 , number2 = input("enter your numbers with space: \n").split(" ")
            number1 = int(number1)
            number2 = int(number2)
            return number1  / number2
        if user_cal_input ==3:
            number1 , number2 = input("enter your numbers with space: \n").split(" ")
            number1 = int(number1)
            number2 = int(number2)
            return number1 + number2
        if user_cal_input ==4:
            number1 , number2 = input("enter your numbers with space: \n").split(" ")
            number1 = int(number1)
            number2 = int(number2)
            return number1 - number2
    else:
         return "Please enter number not str"
def cow_say(cow_input: str, cow_string: str) -> str:
    try:
        cow_input = int(cow_input)
    except ValueError:
        print(print(line()))
        return "First input must be an integer"

    if cow_input not in [1, 2, 3, 4, 5]:
        return "Please choose a valid option between 1 and 5"
    elif not isinstance(cow_string, str):
        return "'Enter your words:' must be a string"
    elif cow_input == 1:
        return cowsay.cow(cow_string)
    elif cow_input == 2:
        return cowsay.trex(cow_string)
    elif cow_input == 3:
        return cowsay.daemon(cow_string)
    elif cow_input == 4:
        return cowsay.dragon(cow_string)
    elif cow_input == 5:
        return cowsay.octopus(cow_string)

def line() -> str: 
    return "---------------------------------------------"
def bitcoin() -> str:
    get = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if get.status_code != 200:
        sys.exit("error 404")
    to_json = json.loads(get.text )
    data = float(to_json["bpi"]["USD"]["rate_float"])
    return data
if __name__ == "__main__":

    main()