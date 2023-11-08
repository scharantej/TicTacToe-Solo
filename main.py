 
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

# Define the computer player
computer_player = 'O'

# Define the human player
human_player = 'X'

# Define the current player
current_player = human_player


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['POST'])
def game():
    # Get the move from the human player
    human_move = request.form.get('move')

    # Update the game board
    board[int(human_move[0])][int(human_move[1])] = human_player

    # Check if the human player has won
    if has_won(human_player):
        return redirect(url_for('winner'))

    # Check if the game is a tie
    if is_tie():
        return redirect(url_for('tie'))

    # Get the move from the computer player
    computer_move = get_computer_move()

    # Update the game board
    board[int(computer_move[0])][int(computer_move[1])] = computer_player

    # Check if the computer player has won
    if has_won(computer_player):
        return redirect(url_for('winner'))

    # Check if the game is a tie
    if is_tie():
        return redirect(url_for('tie'))

    # Return the updated game board
    return render_template('game.html', board=board)


@app.route('/winner')
def winner():
    return render_template('winner.html', winner=current_player)


@app.route('/tie')
def tie():
    return render_template('tie.html')


@app.route('/reset')
def reset():
    # Reset the game board
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    # Reset the current player
    current_player = human_player

    # Redirect to the home page
    return redirect(url_for('index'))


def has_won(player):
    # Check if the player has won
    for winning_combination in winning_combinations:
        if all(board[i][j] == player for i, j in winning_combination):
            return True
    return False


def is_tie():
    # Check if the game is a tie
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


def get_computer_move():
    # Get the computer's move
    for winning_combination in winning_combinations:
        if all(board[i][j] == computer_player for i, j in winning_combination):
            return winning_combination[0], winning_combination[1]
        if all(board[i][j] == human_player for i, j in winning_combination):
            return winning_combination[0], winning_combination[1]
    for i in range(3):
        if board[i][0] == '-' and board[i][1] == '-' and board[i][2] == '-':
            return i, 0
        if board[0][i] == '-' and board[1][i] == '-' and board[2][i] == '-':
            return 0, i
        if board[i][0] == '-' and board[1][1] == '-' and board[2][2] == '-':
            return i, i
        if board[0][2] == '-' and board[1][1] == '-' and board[2][0] == '-':
            return i, 2
    return 1, 1


if __name__ == '__main__':
    app.run(debug=True)
