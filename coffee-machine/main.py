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

currency = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

profit = 0.00

#Procedural programming

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def handle_payment():
    print('Please insert coins.')
    quarters = input('How many quarters?: ')
    dimes = input('How many dimes?: ')
    nickels = input('How many nickels?: ')
    pennies = input('How many pennies?: ')

    payment = round(float(quarters) * currency["quarter"] + float(dimes) * currency["dime"] + float(nickels) * currency["nickel"] + float(pennies) * currency["penny"], 2)
    drink = MENU[prompt]
    price = drink["cost"]

    if payment < price:
        print('Sorry that\'s not enough money. Money refunded.')
    else:
        global profit
        profit += price
        print('Here is $' + str(round(payment - price, 2)) + ' in change.')
        print('Here is your ' + prompt + '.' + ' Enjoy!')

state = True
while state:
    prompt = input('What would you like? (espresso/latte/cappuccino):').lower()
    if prompt == 'off':
        state = False
    elif prompt == 'report':
        print_report()
    elif prompt == 'latte' or prompt == 'espresso' or prompt == 'cappuccino':
        handle_payment()
    else:
        print('Please enter \'espresso\',\'latte\'\'cappuccino\'')

            
        

        
    
