# starting learning class

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def add_points(self, amount):
        self.score += amount
    def reset(self):
        self.score = 0
    def __str__(self):
        return f"{self.name} Score:{self.score}"

player1 = Player("Tiago")
player2 = Player("Juliana")

player1.add_points(100)
player1.reset()
player2.add_points(500)
print(player2)
print(player1)
