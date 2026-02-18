

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resources(choice):
    for item in MENU[choice]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))

    total = (quarters * 0.25 +
             dimes * 0.10 +
             nickels * 0.05 +
             pennies * 0.01)

    return total


def make_coffee(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]


making = True

while making:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        making = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice in MENU:

        if check_resources(choice):

            payment = process_coins()
            cost = MENU[choice]["cost"]

            if payment >= cost:
                change = round(payment - cost, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy! ☕")

                profit += cost
                make_coffee(choice)

            else:
                print("Sorry that's not enough money. Money refunded.")