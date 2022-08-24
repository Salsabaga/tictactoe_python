class BoardGame:
    def __init__(self):
        self.game_rounds = 0
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"],
        ]

    def add_rounds(self):
        self.game_rounds += 1

    @staticmethod
    def horizontal_checker(board_list):
        for x in board_list:
            if len(set(x)) == 1 and ("X" in x or "O" in x):
                print("Winner")
                return False

    @staticmethod
    def vertical_checker(board_list):
        flat_array = [choice for rows in board_list for choice in rows]
        for i in range(0, 3):
            choice_arr = []
            for j in range(i, len(flat_array), 3):
                if flat_array[j] == "X" or flat_array[j] == "O":
                    choice_arr.append(flat_array[j])
            if choice_arr.count("X") == 3 or choice_arr.count("O") == 3:
                print("Winner via Vertical Alignment")
                return False

    @staticmethod
    def diagonal_checker(board_list):
        diagonal = [r[i] for i, r in enumerate(board_list)]
        opposite_diagonal = [r[-i-1] for i, r in enumerate(board_list)]
        if diagonal.count("X") == 3 or diagonal.count("O") == 3:
            print("diagpnal win")
            return False
        elif opposite_diagonal.count("X") == 3 or opposite_diagonal.count("O") == 3:
            print("diagonal win")
            return False
