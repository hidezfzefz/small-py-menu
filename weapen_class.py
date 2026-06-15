class weapon:
    def __init__(self, name, base_damage, durability):
        self.name = name
        self.base_damage = base_damage
        self.durability = 100

    def attack(self):
        self.durability -= 10
        print("you deal", self.base_damage, "with ", self.name, "the durabilty is: ", self.durability)

my_weapon = weapon("iron_sword", 10, 100)

while my_weapon.durability > 0:
    input("\n entre to attack:")
    my_weapon.attack()

print("congratualate you break the sword")