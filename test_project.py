import project
from project import Jar , Wallet
import cowsay
import requests
import json
def test_use_calculator():
    assert project.use_calculator("ALI") == "Please enter number not str"
    assert project.use_calculator("12") == "Please choose between 1 and 4"
def test_cow_say():
    assert project.cow_say(12 , "asd") == "Please choose a valid option between 1 and 5"
    assert project.cow_say(1 , "asd") == cowsay.cow("asd")
    assert project.cow_say(2 , "asd") == cowsay.trex("asd")
    assert project.cow_say(3 , "asd") == cowsay.daemon("asd")
    assert project.cow_say(4 , "asd") == cowsay.dragon("asd")
    assert project.cow_say(5 , "asd") == cowsay.octopus("asd")
    assert project.cow_say("invalid", "Hello!") == "First input must be an integer"
    assert project.cow_say(12 , 12) == "Please choose a valid option between 1 and 5"
    assert project.cow_say(1 , 12) == "'Enter your words:' must be a string"
def test_line():
    x =project.line()
    assert  x=="---------------------------------------------"
def test_bitcoin():
    get = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    to_json = json.loads(get.text )
    data = float(to_json["bpi"]["USD"]["rate_float"])
    assert project.bitcoin() == data
def test_jar():
    jar = Jar()
    jar.deposite(5)
    assert jar.__str__() =="🍪🍪🍪🍪🍪"
    jar.withraw(2)
    assert jar.__str__() == "🍪🍪🍪"
    assert jar.all()== 0
def test_wallet():
    wallet = Wallet()
    wallet.deposit(20)
    assert wallet.__str__() == 20
    wallet.withdraw(10)
    assert wallet.__str__() == 10
    assert wallet.all() == 0