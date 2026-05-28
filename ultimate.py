import time
import random
def game():
    options = ["rock", "paper", "siscer"]



    player_score = 0
    computer_score = 0


    while True:
        computer_pick = random.choice(options)

        print("------game------")
        print("1. rock")
        print("2. paper")
        print("3. siscer")
        print("4. view your score")
        print("5. exist game")

        choise = int(input("pick a choise: "))
        if choise == 1:
            if computer_pick == "siscer":
                print("you gain +1")
                player_score += 1
            elif computer_pick == "paper":
                print("you lose")
                computer_score += 1
            else: print("not one has won")
        elif choise == 2:
            if computer_pick == "rock":
                player_score += 1
                print("your gain +1")
            elif computer_pick == "siscer":
                print("you lose")
                computer_score += 1
            else: print("both equales")
        elif choise == 3:
            if computer_pick == "rock":
                print("you lose")
                computer_score += 1
            elif computer_pick == "paper":
                player_score += 1
                print("you gain +1")
            else: print("both eqauls")
        elif choise == 4:
            print("your score is: " + str(player_score))
            print("pc score is: " + str(computer_score))
        elif choise == 5:
            print("exist game...")
            time.sleep(2)
            break
        else: print("invalid choise")
             
def Bank():
    balence = 100
    choise = ""

    while True:
        print("----n-menu----")
        print("1. check balence")
        print("2. deposit moneey")
        print("3. whitdrow monney")
        print("4. exit")

        choise= int(input("entre your choise: "))
        if choise ==  1:
            print("your balence is: " + str(balence))
        elif choise == 2:
            amout = int(input("how much you wanna depostit: "))
            balence = amout + balence
            print(balence + amout)
            print("you deposit: " + str(amout))
        elif choise == 3:
            amout = int(input("how much you wanna withdrow: "))
            balence = balence - amout
            print("you whitrow: " + str(amout))
        elif choise == 4:
            print("you have been existed succesfully")
            break
        else: print("incorrect choice")


def menu():
    print("---Menue---")
    print("1. calculator")
    print("2. bank")
    print("3. game")
    
def calculator():
    print("---calculator---")
    op = input("entre the operation: ")
    if op == "+":
        add()
    elif op == "-":
        subtract()
    elif op == "*":
        multiply()
    elif op == "/":
        devision()
    else: print("invalid operation")
    
def add():
    a = int(input("entre the first number: "))
    b = int(input("entre the second number: "))
    result = a + b
    print("result is: " + str(result))
    
def subtract():
    a = int(input("entre the first number: "))
    b = int(input("entre the second number: "))
    result = a - b
    print("result is: " + str(result))

def multiply():
    a = int(input("entre the first number: "))
    b = int(input("entre the second number: "))
    result = a * b
    print("result is: " + str(result))

def devision():
    a = int(input("entre the first number: "))
    b = int(input("entre the second number: "))
    result = a / b
    print("result is: " + str(result))

while True:
    menu() 
    menu_choise = int(input("entre your choise: "))

    if menu_choise == 1:
        calculator()
        
    elif menu_choise == 2:
        print("---bank---")
        Bank()

    elif menu_choise == 3:
        print("---game---")
        game()
    else: print("invalid choise")
