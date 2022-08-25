from board_game import BoardGame
from player import Player

player_one = Player(name="player_one", holder="X", current_turn=True)
player_two = Player(name="player_two", holder="O", current_turn=False)

new_game = BoardGame()
game_start = True
board = new_game.board
rounds = new_game.game_rounds
current_player = player_one
player_switch = False

while game_start:
    # Set Player
    if player_one.current_turn is True:
        current_player = player_one
    else:
        current_player = player_two
    # Show Scoreboard
    while player_switch is False:
        new_game.show_board()
        user_row_input = new_game.user_input("Which row you gonna choose?")
        new_game.show_row(user_row_input)
        board_row = board[user_row_input]
        player_position = new_game.user_input("Which position are you gonna choose?")
        # Place counter on board
        player_switch = new_game.place_counter(board_row, player_position, current_player)
    # Toggle Player turn
    if player_one.current_turn is True:
        player_two.current_turn = True
        player_one.current_turn = False
    else:
        player_one.current_turn = True
        player_two.current_turn = False

        # Check if game is over after round 5
    new_game.add_rounds()
    if new_game.game_rounds >= 5:
        if BoardGame.horizontal_checker(board) is False:
            print(current_player.name, "is the winner")
            current_player.add_point()
            game_start = new_game.replay_game()
            board = new_game.reset_board()
            new_game.show_scoreboard(player_one)
            new_game.show_scoreboard(player_two)
        elif BoardGame.vertical_checker(board) is False:
            print(current_player.name, "is the winner")
            current_player.add_point()
            game_start = new_game.replay_game()
            board = new_game.reset_board()
            new_game.show_scoreboard(player_one)
            new_game.show_scoreboard(player_two)
        elif BoardGame.diagonal_checker(board) is False:
            print(current_player.name, "is the winner")
            current_player.add_point()
            game_start = new_game.replay_game()
            board = new_game.reset_board()
            new_game.show_scoreboard(player_one)
            new_game.show_scoreboard(player_two)
        else:
            pass
    player_switch = False

