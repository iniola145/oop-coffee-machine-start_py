from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while True:
    choice = menu.get_items()
    check = input(f"What would you like? {choice}: ")
    if check == "off":
        break
    elif check == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(check)
        print(menu.find_drink(check))
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
