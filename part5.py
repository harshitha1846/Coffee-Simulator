def start():
    global water, milk, coffee_beans, cups, money
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550
def menu():
    global water, milk, coffee_beans, cups, money
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        option = input()
        print()
        if option == 'buy':
            buy()
        elif option == 'fill':
            fill()
        elif option == 'take':
            take()
        elif option == 'remaining':
            display(water, milk, coffee_beans, cups, money)
        elif option == 'exit':
            break
        print()
    
    
    
def buy():
    
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    choice = input()
    if choice == 'back':
        return
    else:
        choice = int(choice)
        msg = check(choice)
        if msg == True:
            make(choice)
        else:
            print(msg)
        
def make(item_no):
    global water, milk, coffee_beans, cups, money
    print('I have enough resources, making you a coffee!')
    if item_no == 1:
        water -= 250
        coffee_beans -= 16
        money += 4
    elif item_no == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
    else:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
    cups -= 1
def check(coffee_type):
    if coffee_type == 1:
        if water < 250:
            return 'Sorry, not enough water!'
        elif coffee_beans < 16:
            return 'Sorry, not enough coffee beans!'
    elif coffee_type == 2:
        if water < 350:
            return 'Sorry, not enough water!'
        elif coffee_beans < 20:
            return 'Sorry, not enough coffee beans!'
        elif milk < 75:
            return 'Sorry, not enough milk!'
    else:
        if water < 200:
            return 'Sorry, not enough water!'
        elif coffee_beans < 12:
            return 'Sorry, not enough coffee beans!'
        elif milk < 100:
            return 'Sorry, not enough milk!'
    return True
        


def fill():
    global water, milk, coffee_beans, cups, money
    print('Write how many ml of water do you want to add:')
    water += int(input())
    print('Write how many ml of milk do you want to add:')
    milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    coffee_beans += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cups += int(input())
def take():
    global money
    print('I gave you ${}'.format(money))
    money = 0

def display(w, mi, cb, cu, mo):
    
    print('The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n{} of money'.format(w, mi, cb, cu, mo))

    
if __name__ == '__main__':
    start()
    menu()
