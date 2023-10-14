class Player:

    def __init__(self, name):

        self.name = name
        self.hp = 100
        self.score = 0
        self.heal = 25

    def show_info(self):
        print("name", self.name)
        print("hp", self.hp)
        print("score", self.score)

    def set_name(self,new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def add_score(self, amount):
        self.score += amount

    def damage(self,amount):
        self.hp -= amount

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.heal += amount


new_player = Player("Bob")
new_player.show_info()

import random

while new_player.is_alive():
    if new_player.hp < 30:
        num = random.randint(0, 1)
        if num:
            new_player.hp += random.randint(1,50)


    num = random.randint(1,2)
    if num == 1:
        new_player.add_score(random.randint(1,10))
    elif num == 2:
        new_player.damage(random.randint(1, 10))


new_player.show_info()