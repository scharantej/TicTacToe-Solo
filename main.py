 
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
        # Otherwise, continue the game
        return render_template('game.html', difficulty=difficulty, move=move, computer_move=computer_move)
    return render_template('game.html', difficulty=difficulty)

@app.route('/winner', methods=['GET'])
def winner():
    winner = request.args.get('winner')
    return render_template('winner.html', winner=winner)

def make_computer_move(difficulty):
    # Choose a random move if the difficulty is easy
    if difficulty == 'easy':
        return random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    # Choose the best move if the difficulty is hard
    elif difficulty == 'hard':
        return '5'

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
    # Otherwise, return None
    return None

if __name__ == '__main__':
    app.run(debug=True)
