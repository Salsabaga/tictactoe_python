from board_game import BoardGame
from player import Player

player_one = Player(0, holder="X", current_turn=True)
player_two = Player(0, holder="O", current_turn=False)

new_game = BoardGame()
game_start = True
board = new_game.board
rounds = new_game.game_rounds
current_player = None

while game_start:
    # Current player if the players turn is true
    if player_one.current_turn is True:
        current_player = player_one
    else:
        current_player = player_two
    print(*board, sep="\n")
    user_row_input = int(input("Which row will you choose? ")) - 1
    print(board[user_row_input])
    position = board[user_row_input]
    user_space_input = int(input("Where you gonna land? ")) - 1
    for idx, x in enumerate(position):
        if user_space_input == idx:
            position[idx] = current_player.holder
    # Check if game is over after round 5
    new_game.add_rounds()
    if new_game.game_rounds >= 5:
        if BoardGame.horizontal_checker(board) is False:
            game_start = False
        elif BoardGame.vertical_checker(board) is False:
            game_start = False
        elif BoardGame.diagonal_checker(board) is False:
            game_start = False
        else:
            pass
    # Toggle Player turn
    if player_one.current_turn is True:
        player_two.current_turn = True
        player_one.current_turn = False
    else:
        player_one.current_turn = True
        player_two.current_turn = False
