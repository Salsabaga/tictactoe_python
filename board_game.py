class BoardGame:
    def __init__(self):
        self.game_rounds = 0
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.reset_board()

    def add_rounds(self):
        self.game_rounds += 1

    def show_board(self):
        print(*self.board, sep="\n")

    def show_row(self, idx):
        print(self.board[idx])

    def reset_board(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        return self.board

    @staticmethod
    def show_scoreboard(player_arr):
        scoreboard_dict = vars(player_arr)
        score_list = []
        for key, val in scoreboard_dict.items():
            if key != "current_turn":
                score_list.append(val)
        print(score_list[0], ":", score_list[2])
    @staticmethod
    def user_input(msg):
        global x
        bound = False
        while bound is False:
            x = int(input(msg)) - 1
            if x < 3:
                bound = True
            else:
                print("out of bounds try again")
        return x

    @staticmethod
    def place_counter(row, position, player):
        for idx, i in enumerate(row):
            if position == idx:
                if row[position] is None:
                    row[idx] = player.holder
                    return True
                else:
                    print("Already on")
                    return False

    def replay_game(self):
        choose_replay = input("Want to continue? Y or N?").capitalize()
        if choose_replay == "Y":
            return True
        elif choose_replay == "N":
            return False
        else:
            print("Invalid input, we gonna end it anyway")
            return False

    @staticmethod
    def horizontal_checker(board_list):
        for i in board_list:
            if len(set(i)) == 1 and ("X" in i or "O" in i):
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
                return False

    @staticmethod
    def diagonal_checker(board_list):
        diagonal = [r[i] for i, r in enumerate(board_list)]
        opposite_diagonal = [r[-i-1] for i, r in enumerate(board_list)]
        if diagonal.count("X") == 3 or diagonal.count("O") == 3:
            return False
        elif opposite_diagonal.count("X") == 3 or opposite_diagonal.count("O") == 3:
            return False
