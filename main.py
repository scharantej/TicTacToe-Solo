 
from flask import Flask, render_template, request

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
computer_player = 'X'

# Define the human player
human_player = 'O'

# Define the current player
current_player = human_player


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    # Get the move from the human player
    if request.method == 'POST':
        move = request.form.get('move')
        board[int(move[0])][int(move[1])] = human_player

        # Check if the human player has won
        if check_winner(board, human_player):
            return render_template('winner.html', winner=human_player)

        # Get the move from the computer player
        move = get_computer_move(board)
        board[int(move[0])][int(move[1])] = computer_player

        # Check if the computer player has won
        if check_winner(board, computer_player):
            return render_template('winner.html', winner=computer_player)

    # Check if the game is a draw
    if check_draw(board):
        return render_template('winner.html', winner='Draw')

    # Render the game board
    return render_template('game.html', board=board)


def check_winner(board, player):
    for winning_combination in winning_combinations:
        if all(board[i][j] == player for i, j in winning_combination):
            return True
    return False


def check_draw(board):
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


def get_computer_move(board):
    for winning_combination in winning_combinations:
        if board[winning_combination[0]][winning_combination[1]] == computer_player and board[winning_combination[2]][winning_combination[3]] == '-':
            return winning_combination[2], winning_combination[3]
        if board[winning_combination[0]][winning_combination[2]] == computer_player and board[winning_combination[1]][winning_combination[3]] == '-':
            return winning_combination[1], winning_combination[3]
        if board[winning_combination[1]][winning_combination[2]] == computer_player and board[winning_combination[0]][winning_combination[3]] == '-':
            return winning_combination[0], winning_combination[3]

    for winning_combination in winning_combinations:
        if board[winning_combination[0]][winning_combination[1]] == human_player and board[winning_combination[2]][winning_combination[3]] == '-':
            return winning_combination[2], winning_combination[3]
        if board[winning_combination[0]][winning_combination[2]] == human_player and board[winning_combination[1]][winning_combination[3]] == '-':
            return winning_combination[1], winning_combination[3]
        if board[winning_combination[1]][winning_combination[2]] == human_player and board[winning_combination[0]][winning_combination[3]] == '-':
            return winning_combination[0], winning_combination[3]

    for i in range(3):
        if board[i][0] == '-' and board[i][1] != '-' and board[i][2] != '-':
            return i, 0
        if board[i][1] == '-' and board[i][0] != '-' and board[i][2] != '-':
            return i, 1
        if board[i][2] == '-' and board[i][0] != '-' and board[i][1] != '-':
            return i, 2

    for j in range(3):
        if board[0][j] == '-' and board[1][j] != '-' and board[2][j] != '-':
            return 0, j
        if board[1][j] == '-' and board[0][j] != '-' and board[2][j] != '-':
            return 1, j
        if board[2][j] == '-' and board[0][j] != '-' and board[1][j] != '-':
            return 2, j

    return 1, 1


if __name__ == '__main__':
    app.run(debug=True)
