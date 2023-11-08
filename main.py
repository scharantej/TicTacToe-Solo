 
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

# Define the computer's level of difficulty
difficulty = 'easy'

# Start a new game
def new_game():
    global board
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

# Check for a winner
def check_winner():
    for winning_combination in winning_combinations:
        if all(board[i][j] == 'X' for i, j in winning_combination):
            return 'X'
        elif all(board[i][j] == 'O' for i, j in winning_combination):
            return 'O'
    return None

# Make a move
def make_move(player, position):
    board[position[0]][position[1]] = player

# Get the computer's next move
def get_computer_move():
    if difficulty == 'easy':
        # Choose a random move
        while True:
            position = (random.randint(0, 2), random.randint(0, 2))
            if board[position[0]][position[1]] == '-':
                break
    elif difficulty == 'hard':
        # Choose the move that gives the computer the best chance of winning
        best_move = None
        best_score = -1000
        for position in range(9):
            if board[position[0]][position[1]] == '-':
                board[position[0]][position[1]] = 'O'
                score = minimax(False)
                board[position[0]][position[1]] = '-'
                if score > best_score:
                    best_move = position
                    best_score = score
        return best_move

# Minimax algorithm
def minimax(maximizing):
    winner = check_winner()
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif all('-' not in row for row in board):
        return 0

    if maximizing:
        best_score = -1000
        for position in range(9):
            if board[position[0]][position[1]] == '-':
                board[position[0]][position[1]] = 'O'
                score = minimax(False)
                board[position[0]][position[1]] = '-'
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 1000
        for position in range(9):
            if board[position[0]][position[1]] == '-':
                board[position[0]][position[1]] = 'X'
                score = minimax(True)
                board[position[0]][position[1]] = '-'
                if score < best_score:
                    best_score = score
        return best_score

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # Get the player's move
        position = (int(request.form['row']), int(request.form['column']))

        # Make the player's move
        make_move('X', position)

        # Check for a winner
        winner = check_winner()

        # If there is a winner, redirect to the winner page
        if winner:
            return redirect(url_for('winner', winner=winner))

        # If there is no winner, make the computer's move
        position = get_computer_move()
        make_move('O', position)

        # Check for a winner
        winner = check_winner()

        # If there is a winner, redirect to the winner page
        if winner:
            return redirect(url_for('winner', winner=winner))

    return render_template('game.html', board=board)

@app.route('/winner', methods=['GET'])
def winner():
    winner = request.args.get('winner')
    return render_template('winner.html', winner=winner)

@app.route('/reset', methods=['GET'])
def reset():
    new_game()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
