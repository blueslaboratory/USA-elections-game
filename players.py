# Date: 23/12/2024

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.score = 0  # Para registrar votos acumulados

    def add_score(self, votos):
        self.score += votos