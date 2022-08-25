class Player:
    players = []

    def __init__(self, name, holder, current_turn):
        self.name = name
        self.holder = holder
        self.current_turn = current_turn
        self.points = 0
        self.players.append(self)
