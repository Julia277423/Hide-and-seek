import random

class GameEngine:
    def __init__(self):
        self.game_code = None
        self.players = []
        self.role = None # 'seeker' lub 'hider'

    def generate_code(self):
        self.game_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return self.game_code

    def assign_roles(self, players_list):
        # Losujemy szukającego
        seeker = random.choice(players_list)
        return seeker # Zwraca nick szukającego