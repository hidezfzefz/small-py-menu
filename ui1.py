player_list = {"name": "blue",
               "gold": 100,
               "potions": 3}


def buy_potion(stat):
    print("--Potion--Menu--")
    print("1. yes (25 Gold)")
    print("2. no")

    chouce = int(input("do you wanna by a potion: "))

    if chouce == 1:
        if stat["gold"] >= 25:
            stat["gold"] -= 25
            stat["potions"] += 1
        elif stat["gold"] < 25:
            print("not enough monney")
    
    if chouce == 2:
        print("Okie")

while player_list["gold"] > 0:
    buy_potion(player_list)        