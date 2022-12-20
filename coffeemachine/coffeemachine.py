# print('''
# Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!
# ''')

# print("Write how many cups of coffee you will need:")
# user_input = int(input())
# water = 200
# milk = 50
# coffee_beens = 15
# print("For",user_input,"cups of coffee you will need\n"
# ,user_input * water,"ml of water\n"
# ,user_input * milk,"ml of milk\n"
# ,user_input * coffee_beens,"g of coffee beans"
# )

# water = 200
# milk = 50
# coffee_beens = 15
# print("Write how many ml of water the coffee machine has:")
# water_left = int(input())
# print("Write how many ml of milk the coffee machine has:")
# milk_left = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# coffee_beens_left = int(input())
# print("Write how many cups of coffee you will need:")
# cups_left = int(input())
# water_cups = int(water_left/water)
# milk_cups = int(milk_left/milk)
# coffee_beens_cups = int(coffee_beens_left/coffee_beens)
# total_cups = min(water_cups,milk_cups,coffee_beens_cups)
# if cups_left > total_cups:
#     print("No, I can make only",total_cups,"cups of coffee")
# elif cups_left < total_cups:
#     print("Yes, I can make that amount of coffee (and even",total_cups - cups_left,"more than that)")
# elif cups_left == total_cups:
#     print("Yes, I can make that amount of coffee")

# water = 400
# milk = 540
# coffee_beens = 120
# cups = 9
# money = 550
# print(f'''
# The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_beens} of coffee beans
# {cups} of disposable cups
# {money} of money
# ''')
# print("Write action (buy, fill, take):")
# user_input = input()
# while user_input != "buy" and user_input != "fill" and user_input != "take":
#     print("Write action (buy, fill, take):")
#     user_input = input()
# if user_input == "buy":
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
#     user_input = int(input())
#     while user_input != 1 and user_input != 2 and user_input != 3:
#         print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
#         user_input = int(input())
#     if user_input == 1:
#         water = water - 250
#         coffee_beens = coffee_beens - 16
#         cups = cups - 1
#         money = money + 4
#         print(f'''
#         The coffee machine has:
#         {water} of water
#         {milk} of milk
#         {coffee_beens} of coffee beans
#         {cups} of disposable cups
#         {money} of money
#         ''')
#     if user_input == 2:
#         water = water - 350
#         milk = milk - 75
#         coffee_beens = coffee_beens - 20
#         cups = cups - 1
#         money = money + 7
#         print(f'''
#          The coffee machine has:
#          {water} of water
#          {milk} of milk
#          {coffee_beens} of coffee beans
#          {cups} of disposable cups
#          {money} of money
#          ''')
#     if user_input == 3:
#         water = water - 200
#         milk = milk - 100
#         coffee_beens = coffee_beens - 12
#         cups = cups - 1
#         money = money + 6
#         print(f'''
#         The coffee machine has:
#         {water} of water
#         {milk} of milk
#         {coffee_beens} of coffee beans
#         {cups} of disposable cups
#         {money} of money
#         ''')
# if user_input == "fill":
#     print("Write how many ml of water you want to add:")
#     water = water + int(input())
#     print("Write how many ml of milk you want to add:")
#     milk = milk + int(input())
#     print("Write how many grams of coffee beans you want to add:")
#     coffee_beens = coffee_beens + int(input())
#     print("Write how many disposable coffee cups you want to add:")
#     cups = cups + int(input())
#     print(f'''
# The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_beens} of coffee beans
# {cups} of disposable cups
# {money} of money
# ''')
# if user_input == "take":
#     print("I gave you",money)
#     print(f'''
# The coffee machine has:
# {water} of water
# {milk} of milk
# {coffee_beens} of coffee beans
# {cups} of disposable cups
# {0} of money
# ''')
class Coffeemachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beens = 120
        self.cups = 9
        self.money = 550

    def start(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            user_input = input()
            while user_input != "buy" and user_input != "fill" and user_input != "take" and user_input != "remaining" \
                    and user_input != "exit":
                print("Write action (buy, fill, take, remaining, exit, back – to main menu:")
                user_input = input()
            if user_input == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
                user_input = input()
                while user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'back':
                    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                    user_input = input()
                if user_input == "back":
                    continue
                if user_input == '1':
                    if self.water < 250:
                        print("Sorry, not enough water!")
                        continue
                    if self.coffee_beens < 16:
                        print("Sorry, not enough coffee beens!")
                        continue
                    if self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    self.water = self.water - 250
                    self.coffee_beens = self.coffee_beens - 16
                    self.cups = self.cups - 1
                    self.money = self.money + 4
                if user_input == '2':
                    if self.water < 350:
                        print("Sorry, not enough water!")
                        continue
                    if self.milk < 75:
                        print("Sorry, not enough milk!")
                        continue
                    if self.coffee_beens < 20:
                        print("Sorry, not enough coffee beens!")
                        continue
                    if self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    self.water = self.water - 350
                    self.milk = self.milk - 75
                    self.coffee_beens = self.coffee_beens - 20
                    self.cups = self.cups - 1
                    self.money = self.money + 7
                if user_input == '3':
                    if self.water < 200:
                        print("Sorry, not enough water!")
                        continue
                    if self.milk < 100:
                        print("Sorry, not enough milk!")
                        continue
                    if self.coffee_beens < 12:
                        print("Sorry, not enough coffee beens!")
                        continue
                    if self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    self.water = self.water - 200
                    self.milk = self.milk - 100
                    self.coffee_beens = self.coffee_beens - 12
                    self.cups = self.cups - 1
                    self.money = self.money + 6
                print("I have enough resources, making you a coffee!")

            if user_input == "fill":
                self.fill()

            if user_input == "take":
                self.take()

            if user_input == "remaining":
                self.remaining()

            if user_input == "exit":
                break

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water = self.water + int(input())
        print("Write how many ml of milk you want to add:")
        self.milk = self.milk + int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.coffee_beens = self.coffee_beens + int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.cups = self.cups + int(input())

    def take(self):
        print("I gave you", self.money)
        self.money = 0

    def remaining(self):
        print(f'''
                # The coffee machine has:
                # {self.water} of water
                # {self.milk} of milk
                # {self.coffee_beens} of coffee beans
                # {self.cups} of disposable cups
                # {self.money} of money
                # ''')


coffeemachine = Coffeemachine()
coffeemachine.start()
