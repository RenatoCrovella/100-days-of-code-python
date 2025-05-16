from fruit import Fruit
from random import randint

market_01 = {}
market_02 = {}

def set_market_stock(_fruits, market):
    for fruit in _fruits:
        fruit_stock = randint(0, 5)
        fruit.stock += fruit_stock
        if fruit_stock != 0:
            to_add = fruit
            market[fruit] = to_add
            print(f"{fruit.name} was added to the market.")

def buy_fruit(fruit, quantity):
    try:
        if fruit.stock >= quantity:
            fruit.stock -= quantity
            print(f"You bought {quantity} of {fruit.name}.")
        else:
            print(f"There's no {fruit.name} enough in the market.")
    except KeyError:
        print(f"The {fruit.name} doesn't exist in the market.")

apple = Fruit("Apple", 20)
pineapple = Fruit("Pineapple", 30)
strawberry = Fruit("Strawberry", 18)
grapes = Fruit("Grapes", 26)
fruits = [apple, pineapple, strawberry, grapes]
set_market_stock(fruits, market_01)
set_market_stock(fruits, market_02)

satisfied = False

while not satisfied:
    print("Would you like to buy some fruit?")
    print("1) Yes")
    print("2) No")
    choice_01 = input("Type your choice: ")
    if choice_01 == "1" or choice_01.lower() == "y":
        print("Excelent! We have fresh fruit for you. Check out each market stock for today:")
        market_01_stock = ""
        market_02_stock = ""
        for item in market_01:
            market_01_stock += f" {item.name} |"
        for item in market_02:
            market_02_stock += f" {item.name} |"
        print(f"Market 01 stock:{market_01_stock}")
        print(f"Market 02 stock: {market_02_stock}")
        choice_02 = input("From which market would you like to buy fruit?: ")
        if choice_02 == "1":
            print(f"Which fruit would you like to buy? {market_01_stock}")
            fruit_to_buy = input("Type your choice: ")
            if fruit_to_buy in market_01_stock:
                for item in market_01:
                    if item.name == fruit_to_buy:
                        fruit_to_buy = item
            else:
                print(f"The {fruit_to_buy} doesn't exist in the market.")
            qtt_to_buy = int(input("How many fruits would you like to buy? "))
            buy_fruit(fruit_to_buy, qtt_to_buy)
            satisfied = True
        elif choice_02 == "2":
            print(f"Which fruit would you like to buy? {market_02_stock}")
            fruit_to_buy = input("Type your choice: ")
            if fruit_to_buy in market_02_stock:
                for item in market_02:
                    if item.name == fruit_to_buy:
                        fruit_to_buy = item
                qtt_to_buy = int(input("How many fruits would you like to buy? "))
                buy_fruit(fruit_to_buy, qtt_to_buy)
                satisfied = True
            else:
                print(f"The {fruit_to_buy} doesn't exist in the market.")
        else:
            print(f"The {choice_02} isn't a valid choice.")
    elif choice_01 == "2" or choice_01.lower() == "n":
        print("Okay, see you next time!")
        satisfied = True
    else:
        print("That's not a valid choice.")
