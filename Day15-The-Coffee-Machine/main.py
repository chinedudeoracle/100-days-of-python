FLAVOURS = {
    "espresso": {"water": 50, "coffee": 18},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
}

PRICES = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappuccino": 3.00,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

COINS = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1, 
}


def print_report():
    """Prints the current values of the available resources."""
    for item in resources:
        if item != "money":
            print(f"{item}: {resources[item]}ml")
        else:
            print(f"{item}: ${resources[item]:.2f}")

def check_resources_sufficient(flavour):
    """Retuens True when order can be made, False when resources are insufficient"""
    for resource in FLAVOURS[flavour]:
        if FLAVOURS[flavour][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    amount = 0
    for item in COINS:
        coin = int(input(f"How many {item}s? "))
        total = coin * COINS[item] * 0.01
        amount += total
    return amount

def check_transaction_successful(choice):
    """Return True when payment is successful, or False when money is insufficient"""
    cash = process_coins()
    price = PRICES[choice]
    if cash >= price:
        change = cash - price
        print(f"Here is ${change:.2f} in change.")
        resources["money"] += price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(choice):
    """Deduct the required flavours from the resources."""
    for resource in FLAVOURS[choice]:
        resources[resource] -= FLAVOURS[choice][resource]
    print(f"Here is your {choice} ☕ Enjoy!")

def coffee_machine():
    process_request = True
    while process_request:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if user_choice == 'off':
            process_request = False
        elif user_choice == "report":
            print_report()
        elif user_choice in FLAVOURS:
            if check_resources_sufficient(user_choice):
                if check_transaction_successful(user_choice):
                    make_coffee(user_choice)

coffee_machine()
