from data import LOGO, MENU
import os
import time

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
end = False
money = {
    "payment": 0,
    "bank":0,
    "exit":False,
         }

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#global variables


#todo print a report shows how many resources are available in the machine

def show_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("You pull a little handle on the side of the machine, to unlock the side panel...")
    time.sleep(2)
    print("hmm...Lets see...")
    time.sleep(2)
    amount = money["bank"]
    print(f"Water: {water}ml remaining,\nMilk: {milk}ml remaining,\nCoffee: {coffee}g remaining.\n${amount} in bank account." )

def show_menu():
    print(MENU)

def espresso():
    water = resources["water"]
    coffee = resources["coffee"]
    ingredients = MENU["espresso"]["ingredients"]
    if water >= ingredients['water'] and coffee >= ingredients['coffee']:
        if transaction("espresso") == True:
            water -= ingredients['water']
            coffee -= ingredients['coffee']
            resources["water"] = water
            resources["coffee"] = coffee
            print("The machine WRRs to life, your coffee is brewing...")
            time.sleep(3)
            print("You see your cup filling with coffee and you can smell the extra strong aroma.")
            time.sleep(3)
            print(
                "You hear a dial spin and a sign appears 'Enjoy your coffee!'\nYou carefully pick up your espresso from the machine.")
    else:
        print(f"You hear a dial spin and a sign appears. 'Insufficient ingredients detected'")

def latte():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    ingredients = MENU["latte"]["ingredients"]
    if water >= ingredients['water'] and coffee >= ingredients['coffee'] and milk >= ingredients['milk']:
        if transaction("latte") == True:
            water -= ingredients['water']
            milk -= ingredients['milk']
            coffee -= ingredients['coffee']
            resources["water"] = water
            resources["milk"] = milk
            resources["coffee"] = coffee
            print("The machine WRRs to life, your coffee is brewing...")
            time.sleep(3)
            print("You see your cup filling with coffee, You can smell the aroma.")
            time.sleep(3)
            print("You see the milk pouring into your cup. You hear a dial spin and a sign appears 'Enjoy your coffee!'\nYou carefully pick up your Latte from the machine.")
    else:
        print(f"You hear a dial spin and a sign appears. 'Insufficient ingredients detected'")

def cappuccino():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    ingredients = MENU["cappuccino"]["ingredients"]
    if water >= ingredients['water'] and coffee >= ingredients['coffee'] and milk >= ingredients['milk']:
        if transaction("cappuccino") == True:
            water -= ingredients['water']
            milk -= ingredients['milk']
            coffee -= ingredients['coffee']
            resources["water"] = water
            resources["milk"] = milk
            resources["coffee"] = coffee
            print("The machine WRRs to life, your coffee is brewing...")
            time.sleep(3)
            print("You see your cup filling with coffee, You can smell the aroma.")
            time.sleep(3)
            print("You see a container filled with some milk, after another couple of WRRing noises you can see the milk foaming up.")
            time.sleep(3)
            print("You see the milk pouring into your cup. You hear a dial spin and a sign appears 'Enjoy your coffee!'\nYou carefully pick up your cappuccino from the machine.")
    else:
        time.sleep(3)
        print(f"You hear a dial spin and a sign appears. 'Insufficient ingredients detected'")

def transaction(product):
    total = 0
    quarters = input("How many quarters?")
    dimes = input("How many dimes?")
    nickels = input("How many nickels?")
    pennies = input("How many pennies?")
    if quarters.isdigit() == True:
        total += int(quarters)*0.25
    if dimes.isdigit() == True:
        total += int(dimes)*0.1
    if nickels.isdigit() == True:
        total += int(nickels)*0.05
    if pennies.isdigit() == True:
        total += int(pennies)*0.01
    cost = MENU[product]["cost"]
    change = total - cost
    if total >= cost:
        money["payment"] = cost
        time.sleep(2)
        print(f"Your change drops into the holder: {change}")
        time.sleep(1)
        return True
    else:
        print(f"You hear a dial spin and a sign appears. 'Insufficient funds inserted'\n Your coins drop down into the holder: {total}")
        return False

def refill_machine():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("You pull a little handle on the side of the machine, to unlock the side panel...")
    time.sleep(2)
    print("hmm...Lets see...")
    time.sleep(2)
    print("You refill all the little containers in the little coffee machine.")
    time.sleep(2)
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    money["payment"] = -1.5
    print(f"Water: {water}ml,\nMilk: {milk}ml,\nCoffee: {coffee}g. \nRefill cost $1.50" )


def command_processor():
    command = input("Enter command:").lower()
    print(command)
    if command == "off" or command == "turn off":
        clearConsole()
        print("Coffee machine WRR's to a halt and powers down")
        time.sleep(2)
        input("press 'return' to switch on the coffee machine")
        coffee_machine()
    if command == 'report' or command == 'print report' or command == 'show report':
        show_report()
        input("Press 'return' to proceed.")
    if command == 'clear' or command == 'back':
        clearConsole()
    if command == "show menu" or command == "menu":
        show_menu()
        input("Press 'return' to proceed.")
    if command == "espresso":
        espresso()
        input("Press 'return' to proceed.")
    if command == "latte":
        latte()
        input("Press 'return' to proceed.")
    if command == "cappuccino":
        cappuccino()
        input("Press 'return' to proceed.")
    if command == "refill" or command=="refill coffee machine" or command =="refill the coffee machine":
        refill_machine()
        input("Press 'return' to proceed.")
    if command == "?":
        print("-turn off\n-report\n-show menu\n-back\n-espresso\n-latte\n-cappuccino\n-refill")
        input("Press 'return' to proceed.")
    if command == "exit":
        money["exit"] = True



def coffee_machine():
    while money["exit"] == False:
        income = money["payment"]
        bank = money["bank"]
        money["bank"] = income + bank
        money["payment"] = 0
        bank = money["bank"]
        clearConsole()
        print(LOGO)
        print(f"Available funds: ${bank}")
        print("The coffee machine spins to life.\nEspresso:  $1.50 \nLatte:  $2.50 \nCappuccino:  $3.00\n\n\nType '?' for a a list of commands")
        command_processor()


coffee_machine()





#todo check transaction. Ask the user for money and check whether the user added enough money.

#todo process coins. add money to inventory and give the user change.

#todo make coffee. subtract resources from inventory, hand the user their coffee.

#todo add a sign to coffee options as resources get empty.

#todo Select a cool ascii art for the coffee machine.

