class CoffeeMachine:
    def __init__(self):
        self.resources = {
            'water': 300, 
            'milk': 200,   
            'coffee': 100, 
            'money': 0     
        }
        
        self.drinks = {
            'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'price': 1.50},
            'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'price': 2.50},
            'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'price': 3.00}
        }
        
    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']:.2f}")
        
    def check_resources(self, drink):
        if self.resources['water'] < self.drinks[drink]['water']:
            print("Sorry, there is not enough water.")
            return False
        if self.resources['milk'] < self.drinks[drink]['milk']:
            print("Sorry, there is not enough milk.")
            return False
        if self.resources['coffee'] < self.drinks[drink]['coffee']:
            print("Sorry, there is not enough coffee.")
            return False
        return True
    
    def process_coins(self):
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total_money = quarters + dimes + nickels + pennies
        return total_money
    
    def make_coffee(self, drink):
        self.resources['water'] -= self.drinks[drink]['water']
        self.resources['milk'] -= self.drinks[drink]['milk']
        self.resources['coffee'] -= self.drinks[drink]['coffee']
        self.resources['money'] += self.drinks[drink]['price']
        print(f"Here is your {drink}. Enjoy!")
    
    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            
            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choice == "report":
                self.report()
            elif choice in self.drinks:
                if self.check_resources(choice):
                    print(f"The {choice} costs ${self.drinks[choice]['price']}")
                    inserted_money = self.process_coins()
                    
                    if inserted_money < self.drinks[choice]['price']:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        change = round(inserted_money - self.drinks[choice]['price'], 2)
                        if change > 0:
                            print(f"Here is ${change} in change.")
                        self.make_coffee(choice)
                else:
                    print("Sorry, there are not enough resources to make that drink.")
            else:
                print("Invalid choice. Please choose espresso, latte, or cappuccino.")


coffee_machine = CoffeeMachine()


coffee_machine.run()
