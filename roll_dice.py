import random
import time

dice_list = []
time_rerolled = 0

def dice_menu():
    print("--Dice--Menue")
    print("1. Roll dice")
    print("2. view total rerrol")
    print("3. Dice History")
    print("4. exit")

def dice_mechanism():
    global time_rerolled
    global choose
    dice_menu()
    computer_roll = random.randint(1,6)

    choose = int(input("entre an option: "))
    if choose == 1:
        print("your lucky roll is: " + str(computer_roll))
        dice_list.append(computer_roll)
        time_rerolled += 1
    elif choose == 2:
        print("your total score is: " + str(time_rerolled))
    elif choose == 3:
        for n in dice_list:
            print("_ " + str(n)) 
    

while True:
    dice_mechanism()
    if choose == 4:
        print("exiting...")
        time.sleep(1.5)
        break
    else: print("invalid option")