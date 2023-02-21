from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

state = True
options = menu.get_items()
while state:
    answer = input('What would you like? (espresso/latte/cappuccino/):').lower()
    if answer == 'off':
        state = False
    elif answer == 'report':
        coffee_maker.report()
        money_machine.report()
    elif answer == 'espresso' or answer == 'latte' or answer == 'cappuccino':
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print('Please enter \'espresso\', \'latte\', or \'cappuccino\'')