import time
import random

my_hp = 50
enemie_hp = 40 
potion = 3
def menu():
    print("---game---")
    print("1. attack ")
    print("2. potion")


def player_attack(enemie_hp): 
    damage = random.randint(1,15)
    print("player attack")
    time.sleep(0.5)
    print("player has deal: " + str(damage))
    enemie_hp -= damage 
    return enemie_hp

def enemie_attack(player_hp):
    damage = random.randint(1,15)
    print("enemie turn")
    time.sleep(0.5)
    print("enemie has deal: " + str(damage))
    player_hp -= damage
    return player_hp


while my_hp > 0 and enemie_hp > 0:
    time.sleep(0.5)
    menu()
    choice  =  int(input("\nPress Enter to strike!: "))


    if choice == 1:
     print("")
     enemie_hp = player_attack(enemie_hp)

     if enemie_hp <= 0:
         print("player has won")

     my_hp = enemie_attack(my_hp)

     if my_hp <= 0:
         print("enemie has won")
    elif choice == 2:
         hp_added = random.randint(1.20)
         hp_added =+ my_hp
         print("you healed: ", hp_added)



        
    
