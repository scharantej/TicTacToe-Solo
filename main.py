 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the game board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Define the possible winning combinations
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                       [0, 3, 6], [1, 4, 7], [2, 5, 8],
                       [0, 4, 8], [2, 4, 6]]

# Define the computer's move
computer_move = None


# Define the game state
game_state = 'in progress'


# Define the current player
current_player = 'X'


# Define the route for the home page
@app.route('/')
def index():
    # Reset the game board
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'

    # Reset the game state
    game_state = 'in progress'

    # Reset the current player
    current_player = 'X'

    # Return the home page
    return render_template('index.html')


# Define the route for the game page
@app.route('/game')
def game():
    # Get the player's move
    player_move = request.args.get('move')

    # Update the game board
    board[int(player_move[0])][int(player_move[1])] = current_player

    # Check if the player has won
    if check_winner(current_player):
        game_state = 'won'
        return render_template('winner.html', winner=current_player)

    # Check if the game is a draw
    if check_draw():
        game_state = 'draw'
        return render_template('winner.html', winner='Draw')

    # Update the current player
    current_player = 'O' if current_player == 'X' else 'X'

    # Get the computer's move
    computer_move = get_computer_move()

    # Update the game board
    board[int(computer_move[0])][int(computer_move[1])] = current_player

    # Check if the computer has won
    if check_winner(current_player):
        game_state = 'won'
        return render_template('winner.html', winner=current_player)

    # Check if the game is a draw
    if check_draw():
        game_state = 'draw'
        return render_template('winner.html', winner='Draw')

    # Return the game page
    return render_template('game.html', board=board, current_player=current_player)


# Define the route for the winner page
@app.route('/winner')
def winner():
    # Return the winner page
    return render_template('winner.html', winner=winner)


# Define the route for resetting the game
@app.route('/reset')
def reset():
    # Reset the game board
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'

    # Reset the game state
    game_state = 'in progress'

    # Reset the current player
    current_player = 'X'

    # Redirect to the home page
    return redirect(url_for('index'))


# Define the function to check if a player has won
def check_winner(player):
    for winning_combination in winning_combinations:
        if all(board[i][j] == player for i, j in winning_combination):
            return True
    return False


# Define the function to check if the game is a draw
def check_draw():
    for i in range(3):
        if board[i][0] != '-' and board[i][1] != '-' and board[i][2] != '-':
            return False
        if board[0][i] != '-' and board[1][i] != '-' and board[2][i] != '-':
            return False
        if board[i][0] != '-' and board[1][1] != '-' and board[2][2] != '-':
            return False
        if board[0][2] != '-' and board[1][1] != '-' and board[2][0] != '-':
            return False
    return True


# Define the function to get the computer's move
def get_computer_move():
    for winning_combination in winning_combinations:
        if board[winning_combination[0]][winning_combination[1]] == '-' and board[winning_combination[1]][winning_combination[2]] == '-' and board[winning_combination[2]][winning_combination[0]] == '-':
            return winning_combination[0], winning_combination[1]
        if board[winning_combination[0]][winning_combination[2]] == '-' and board[winning_combination[1]][winning_combination[0]] == '-' and board[winning_combination[2]][winning_combination[1]] == '-':
            return winning_combination[0], winning_combination[2]
        if board[winning_combination[1]][winning_combination[0]] == '-' and board[winning_combination[2]][winning_combination[1]] == '-' and board[winning_combination[0]][winning_combination[2]] == '-':
            return winning_combination[1], winning_combination[0]
        if board[winning_combination[1]][winning_combination[2]] == '-' and board[winning_combination[0]][winning_combination[1]] == '-' and board[winning_combination[2]][winning_combination[0]] == '-':
            return winning_combination[1], winning_combination[2]
        if board[winning_combination[2]][winning_combination[0]] == '-' and board[winning_combination[0]][winning_combination[2]] == '-' and board[winning_combination[1]][winning_combination[0]] == '-':
            return winning_combination[2], winning_combination[0]
        if board[winning_combination[2]][winning_combination[1]] == '-' and board[winning_combination[1]][winning_combination[2]] == '-' and board[winning_combination[0]][winning_combination[1]] == '-':
            return winning_combination[2], winning_combination[1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return i, j


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
