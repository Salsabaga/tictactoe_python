from board_game import BoardGame
from player import Player

player_one = Player(name="player_one", holder="X", current_turn=True)
player_two = Player(name="player_two", holder="O", current_turn=False)

new_game = BoardGame()
game_start = True
board = new_game.board
rounds = new_game.game_rounds
current_player = Player.players[0]
player_switch = False

while game_start:
    if player_one.current_turn is True:
        current_player = player_one
    else:
        current_player = player_two
    while player_switch is False:
        print("Current Player Turn", current_player.name)
        print(current_player == player_one)
        print(current_player == player_two)
        new_game.show_board()
        user_row_input = int(input("Which row will you choose? ")) - 1
        new_game.show_row(user_row_input)
        board_row = board[user_row_input]
        player_position = int(input("Where you gonna land? ")) - 1
        # Place counter on board
        player_switch = new_game.place_counter(board_row, player_position, current_player)
        print("Output was", player_switch)
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

    player_switch = False
