 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        difficulty = request.form.get('difficulty')
        return redirect(url_for('game', difficulty=difficulty))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    difficulty = request.args.get('difficulty')
    if request.method == 'POST':
        move = request.form.get('move')
        # Make the computer's move
        computer_move = make_computer_move(difficulty)
        # Check if the game is over
        winner = check_winner()
        if winner:
            return redirect(url_for('winner', winner=winner))
        # Render the game board
        return render_template('game.html', difficulty=difficulty, board=board, move=move, computer_move=computer_move)
    return render_template('game.html', difficulty=difficulty, board=board)

@app.route('/winner', methods=['GET'])
def winner():
    winner = request.args.get('winner')
    return render_template('winner.html', winner=winner)

def make_computer_move(difficulty):
    # Choose a random move
    if difficulty == 'easy':
        move = random.choice(available_moves())
    # Choose the best move
    elif difficulty == 'hard':
        move = minimax(board, depth=3)
    return move

def check_winner():
    # Check if there is a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
        if board[0][row] == board[1][row] == board[2][row] != ' ':
            return board[0][row]
        if board[row][0] == board[1][1] == board[2][2] != ' ':
            return board[row][0]
        if board[2][0] == board[1][1] == board[0][2] != ' ':
            return board[2][0]
    return None

def available_moves():
    # Return a list of available moves
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

def minimax(board, depth, alpha=-float('inf'), beta=float('inf')):
    # Check if the game is over
    winner = check_winner()
    if winner:
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    # Check if the current player is maximizing or minimizing
    if depth % 2 == 0:
        # Maximizing player
        best_score = -float('inf')
        for move in available_moves():
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, alpha, beta)
            board[move[0]][move[1]] = ' '
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        # Minimizing player
        best_score = float('inf')
        for move in available_moves():
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, alpha, beta)
            board[move[0]][move[1]] = ' '
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

if __name__ == '__main__':
    app.run(debug=True)
