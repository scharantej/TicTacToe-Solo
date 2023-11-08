 
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
    return render_template('index.html')


# Define the route for the game page
@app.route('/game', methods=['GET', 'POST'])
def game():
    global board, winning_combinations, computer_move, game_state, current_player

    # Handle the GET request
    if request.method == 'GET':
        return render_template('game.html', board=board, game_state=game_state, current_player=current_player)

    # Handle the POST request
    if request.method == 'POST':
        # Get the player's move
        player_move = request.form.get('move')

        # Update the game board
        board[int(player_move[0])][int(player_move[1])] = current_player

        # Check if the player has won
        if any(all(board[i][j] == current_player for j in winning_combinations[i]) for i in range(len(winning_combinations))):
            game_state = 'won'
            return render_template('game.html', board=board, game_state=game_state, current_player=current_player)

        # Check if the game is a draw
        if all('-' not in row for row in board):
            game_state = 'draw'
            return render_template('game.html', board=board, game_state=game_state, current_player=current_player)

        # Update the current player
        current_player = 'O' if current_player == 'X' else 'X'

        # Get the computer's move
        computer_move = get_computer_move(board)

        # Update the game board
        board[int(computer_move[0])][int(computer_move[1])] = current_player

        # Check if the computer has won
        if any(all(board[i][j] == current_player for j in winning_combinations[i]) for i in range(len(winning_combinations))):
            game_state = 'lost'
            return render_template('game.html', board=board, game_state=game_state, current_player=current_player)

        # Check if the game is a draw
        if all('-' not in row for row in board):
            game_state = 'draw'
            return render_template('game.html', board=board, game_state=game_state, current_player=current_player)

        # Update the current player
        current_player = 'X' if current_player == 'O' else 'O'

        return render_template('game.html', board=board, game_state=game_state, current_player=current_player)


# Define the route for the results page
@app.route('/results')
def results():
    return render_template('results.html', game_state=game_state)


# Define the route for the reset page
@app.route('/reset')
def reset():
    global board, game_state, current_player
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    game_state = 'in progress'
    current_player = 'X'
    return redirect(url_for('index'))


# Define the function to get the computer's move
def get_computer_move(board):
    global winning_combinations

    # Check if the computer can win in one move
    for i in range(len(winning_combinations)):
        if board[winning_combinations[i][0]][winning_combinations[i][1]] == 'O' and board[winning_combinations[i][1]][winning_combinations[i][2]] == 'O' and board[winning_combinations[i][0]][winning_combinations[i][2]] == '-':
            return winning_combinations[i][0], winning_combinations[i][2]
        if board[winning_combinations[i][0]][winning_combinations[i][1]] == 'O' and board[winning_combinations[i][0]][winning_combinations[i][2]] == 'O' and board[winning_combinations[i][1]][winning_combinations[i][2]] == '-':
            return winning_combinations[i][1], winning_combinations[i][2]
        if board[winning_combinations[i][1]][winning_combinations[i][2]] == 'O' and board[winning_combinations[i][0]][winning_combinations[i][2]] == 'O' and board[winning_combinations[i][0]][winning_combinations[i][1]] == '-':
            return winning_combinations[i][0], winning_combinations[i][1]

    # Check if the player can win in one move
    for i in range(len(winning_combinations)):
        if board[winning_combinations[i][0]][winning_combinations[i][1]] == 'X' and board[winning_combinations[i][1]][winning_combinations[i][2]] == 'X' and board[winning_combinations[i][0]][winning_combinations[i][2]] == '-':
            return winning_combinations[i][0], winning_combinations[i][2]
        if board[winning_combinations[i][0]][winning_combinations[i][1]] == 'X' and board[winning_combinations[i][0]][winning_combinations[i][2]] == 'X' and board[winning_combinations[i][1]][winning_combinations[i][2]] == '-':
            return winning_combinations[i][1], winning_combinations[i][2]
        if board[winning_combinations[i][1]][winning_combinations[i][2]] == 'X' and board[winning_combinations[i][0]][winning_combinations[i][2]] == 'X' and board[winning_combinations[i][0]][winning_combinations[i][1]] == '-':
            return winning_combinations[i][0], winning_combinations[i][1]

    # Check if the computer can make a move in the center of the board
    if board[1][1] == '-':
        return 1, 1

    # Check if the computer can make a move in a corner of the board
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == '-':
                return i, j

    # Check if the computer can make a move on the edge of the board
    for i in range(3):
        if board[i][0] == '-':
            return i, 0
        if board[i][2] == '-':
            return i, 2
        if board[0][i] == '-':
            return 0, i
        if board[2][i] == '-':
            return 2, i

    # Return a random move
    return random.randint(0, 2), random.randint(0, 2)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
