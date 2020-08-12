class CoffeeMachine():
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water  
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
    def menu(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            option = input()
            print()
            if option == 'buy':
                self.buy()
            elif option == 'fill':
                self.fill()
            elif option == 'take':
                self.take()
            elif option == 'remaining':
                self.display()
            elif option == 'exit':
                break
            print()
    
    
    
    def buy(self):
    
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        choice = input()
        #espresso need 250ml of water and 16g of coffee_beans --- cost = 4$
        #latte need 350ml of water, 75ml of milk and 20g of coffee_beans --- cost = 7$
        #cappuccino need 200ml of water, 100ml of milk and 12g of coffee_beans --- cost = 7$

        if choice == 'back':
            return
        else:
            msg = self.check(choice)
            if msg == True:
                self.make(choice)
            else:
                print(msg)
        
    def make(self, item_no):
        print('I have enough resources, making you a coffee!')
        if item_no == 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif item_no == 2:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        else:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
        self.cups -= 1
    def check(self, coffee_type):
        if coffee_type == '1':
            if self.water < 250:
                return 'Sorry, not enough water!'
            elif self.coffee_beans < 16:
                return 'Sorry, not enough coffee beans!'
        elif coffee_type == '2':
            if self.water < 350:
                return 'Sorry, not enough water!'
            elif self.coffee_beans < 20:
                return 'Sorry, not enough coffee beans!'
            elif self.milk < 75:
                return 'Sorry, not enough milk!'
        else:
            if self.water < 200:
                return 'Sorry, not enough water!'
            elif self.coffee_beans < 12:
                return 'Sorry, not enough coffee beans!'
            elif self.milk < 100:
                return 'Sorry, not enough milk!'
        return True
        


    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0

    def display(self):
        print('The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n{} of money'.format(self.water, self.milk, self.coffee_beans, self.cups, self.money))

    
if __name__ == '__main__':
    obj = CoffeeMachine(400, 540, 120, 9, 550)
    obj.menu()
