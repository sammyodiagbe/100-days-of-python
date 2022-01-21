# implement the same code in Object oriented programming


class CoffeeMachine:
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
        "money": 0
    }

    coin_values = {
        'pennies': 0.01,
        'nickles': 0.05,
        'dimes': 0.10,
        'quarters': 0.5
    }

    def __init__(self):
        self.serve_customer()

    def process_customer_order(self, customer_response):
        preffered_drink = self.MENU[customer_response]
        preffered_drink_ingredients = preffered_drink['ingredients']
        for key in preffered_drink_ingredients:
            if preffered_drink_ingredients[key] > self.resources[key]:
                print(f'Sorry there isn\'t enough {key}')
                return self.serve_customer()
        return self.process_coin(preffered_drink, customer_response)
        pass

    def process_coin(self, preffered_drink, coffee_drink):
        number_of_pennies = float(input("Insert number of pennies: "))
        number_of_nickles = float(input("Insert number of nickles: "))
        number_of_dimes = float(input("Inset number of dimes: "))
        number_of_quarters = float(input("Insert number of quarters: "))
        total_in_dollars = self.coin_values['pennies'] * number_of_pennies
        total_in_dollars += self.coin_values['nickles'] * number_of_nickles
        total_in_dollars += self.coin_values['dimes'] * number_of_dimes
        total_in_dollars += self.coin_values['quarters'] * number_of_quarters
        if total_in_dollars < preffered_drink['cost']:
            print('Sorry that is not enough money. Money refunded')
            return self.serve_customer()
        change = round(total_in_dollars - preffered_drink['cost'], 2)
        self.resources['money'] = self.resources['money'] + preffered_drink['cost'] if self.resources['money'] >= 0 else preffered_drink['cost']
        self.print_report()
        if change > 0:
            print(f'Here is ${change} dollars in change.')
        print(f'Here is your {coffee_drink}. Enjoy!')
        return self.serve_customer()

    def print_report(self):
        list_of_keys = list(self.resources.keys())
        measurement = ['ml', 'ml', 'g']
        for key in range(len(list_of_keys) - 1):
            print(f'{list_of_keys[key]} : {self.resources[list_of_keys[key]]}{measurement[key]}')
        print(f'money : ${self.resources["money"]}')
        return self.serve_customer()

    def serve_customer(self):
        customer_response = input('What would you like? (espresso/latte/cappuccino):')
        if customer_response in ['espresso', 'latte', 'cappuccino']:
            self.process_customer_order(customer_response)

        elif customer_response == 'off':
            return

        elif customer_response == 'report':
            self.print_report()
        else:
            self.serve_customer()

    pass


coffeeMachine = CoffeeMachine()