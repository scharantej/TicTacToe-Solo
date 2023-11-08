 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's move
        move = request.form.get('move')

        # Make the computer's move
        computer_move = get_computer_move(move)

        # Check if the game is over
        winner = check_winner(move, computer_move)

        # Render the game board
        return render_template('game.html', move=move, computer_move=computer_move, winner=winner)
    else:
        # Render the home page
        return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # Get the user's move
        move = request.form.get('move')

        # Make the computer's move
        computer_move = get_computer_move(move)

        # Check if the game is over
        winner = check_winner(move, computer_move)

        # Render the game board
        return render_template('game.html', move=move, computer_move=computer_move, winner=winner)
    else:
        # Render the game board
        return render_template('game.html')

@app.route('/winner', methods=['GET'])
def winner():
    # Get the winner
    winner = request.args.get('winner')

    # Render the winner page
    return render_template('winner.html', winner=winner)

def get_computer_move(move):
    # Get the computer's move
    computer_move = 'X' if move == 'O' else 'O'

    # Return the computer's move
    return computer_move

def check_winner(move, computer_move):
    # Check if the user has won
    if move == 'X' and computer_move == 'O':
        winner = 'X'
    elif move == 'O' and computer_move == 'X':
        winner = 'O'

    # Check if the computer has won
    elif move == 'O' and computer_move == 'X':
        winner = 'X'
    elif move == 'X' and computer_move == 'O':
        winner = 'O'

    # Check if the game is a draw
    elif move == 'X' and computer_move == 'X':
        winner = 'Draw'
    elif move == 'O' and computer_move == 'O':
        winner = 'Draw'

    # Return the winner
    return winner

if __name__ == '__main__':
    app.run(debug=True)
