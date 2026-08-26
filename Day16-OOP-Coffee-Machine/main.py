from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower().strip()
    if choice == "off":
        is_on = False
    elif choice == "report":
        f"{coffee_maker.report()}\n{money_machine.report()}"
    else:
        drink = my_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            
  
   