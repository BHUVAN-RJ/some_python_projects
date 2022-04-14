import resources

water = 300
milk = 200
coffee = 100


def resources_print():
    print(f"There is still {water}ml of water, {milk}ml of milk, {coffee}g of coffee left in the machine")


def resource_update(order2):
    global water, milk, coffee
    water = water - int(resources.MENU[order2]["ingredients"]["water"])
    milk = milk - int(resources.MENU[order2]["ingredients"]["milk"])
    coffee = coffee - int(resources.MENU[order2]["ingredients"]["coffee"])


def coins():
    penny = int(input("How many Pennies did you insert?:"))
    nickle = int(input("How many Nickles did you insert?:"))
    dime = int(input("How many Dimes did you insert?:"))
    quarter = int(input("How many pennies did you insert?:"))
    total = (penny*0.01) + (nickle*0.05) + (dime*0.1) + (quarter*0.25)
    return total


def transaction(order1):
    cost = resources.MENU[order1]["cost"]
    total = coins()
    if total >= cost:
        print(f"Here is your {order1}!!!")
        resource_update(order1)
        if total > cost:

            returns = total - cost
            print(f"Here is your change of ${returns}, have a Great day")
        else:
            print("You have inserted exact amount, have a Great day")
    else:
        print(f"Your order costs {cost}, but you have inserted {total}. Sorry cannot serve you coffee!!! ")


def resource_check(order0):
    global water, milk, coffee
    if water >= resources.MENU[order0]["ingredients"]["water"] and \
            coffee >= resources.MENU[order0]["ingredients"]["coffee"] and \
            milk >= resources.MENU[order0]["ingredients"]["milk"]:
        transaction(order0)
    else:
        if water < resources.MENU[order0]["ingredients"]["water"]:
            print("Sorry theres not enough water!!")
        elif milk < resources.MENU[order0]["ingredients"]["milk"]:
            print("Sorry theres not enough milk!!")
        else:
            print("Sorry theres not enough coffee!!")


while True:
    order = input("What would you like to have?latte/espresso/cappuccino:")
    if order == "off":
        break
    elif order == "report":
        resources_print()
    else:
        resource_check(order)

