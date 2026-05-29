import time
import random

inventory = ["Helmet"]



def menu():
    print("")
    print("---n--menu----")
    print("1. View inventory")
    print("2. open chest")
    print("3. exit the game")
    print("")


def bag():
    print("")
    print("---Inventory---")
    print("1. remouve item from inventory")
    print("2. exist")
    print("")
    

def bag_options():
    choose = int(input("pick an option: "))
    if choose == 1:
        remove_item = int(input("wish item you wanna remouve: "))
        remove_item -= 1
        remove = inventory.pop(remove_item) 
        print("you succesfully remouve: " + str(remove))

        if not inventory:
            print("list is emty")
        
    elif choose == 2:
        print("exiting...")
        time.sleep(1)
    else:
        print("invalid option")
      


def chest():
    global random_item
    global inventory

    chest_items = ["Iron sword", "Poison Dagger", "Crystal Staff", "Golden chield", "Shodow Cloack"]
    random_item = random.choice(chest_items)
    inventory.append(random_item)
    print("")
    print("you got: " + str(random_item))


while True:
    menu()
    choise = int(input("enter an option: "))
    if choise == 1:
        for items in inventory:
            print(items)
        bag()
        bag_options()
        time.sleep(1)

    elif choise == 2:
        chest() 

    elif choise == 3:
        print("exiting...")
        time.sleep(1)
        break
    else: 
        print("invalid option")