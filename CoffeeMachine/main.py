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
moneyInMachine = 0


def check_enough_resources(drinkIngredients):
    for ingredient in drinkIngredients:
        if drinkIngredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(total, drinkCost):
    global moneyInMachine
    if total < drinkCost:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif total > drinkCost:
        moneyInMachine += drinkCost
        change = total - drinkCost
        print(f"Here is ${round(change, 2)} dollars in change")
    else:
        moneyInMachine += drinkCost
    return True


def make_coffee(drinkName, drinkIngredients):
    for ingredient in drinkIngredients:
        resources[ingredient] -= drinkIngredients[ingredient]
    print(f"Here's your {drinkName}. Enjoy it!!")


def print_report():
    for ingredient in resources:
        print(f"{ingredient.capitalize()}: {resources[ingredient]}ml")
    print(f"Money: ${moneyInMachine}")


isMachineOn = True
while isMachineOn:
    userChoice = input("What would you like? (espresso/latte/cappuccino): ")

    if userChoice == "off":
        isMachineOn = False
    elif userChoice == "report":
        print_report()
    else:
        drink = MENU[userChoice]
        if check_enough_resources(drink["ingredients"]):
            totalPayment = process_coins()
            if check_transaction(totalPayment, drink["cost"]):
                make_coffee(userChoice, drink["ingredients"])
