 
from flask import Flask, render_template, request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    # Get the user's move
    move = request.form.get('move')

    # Make the computer's move
    computer_move = get_computer_move(move)

    # Check if the game is over
    winner = check_winner(move, computer_move)

    # Render the game board
    return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner', methods=['POST'])
def winner():
    # Get the winner
    winner = request.form.get('winner')

    # Render the winner page
    return render_template('winner.html', winner=winner)

# Functions
def get_computer_move(move):
    # Get the computer's move
    computer_move = random.choice(['X', 'O'])

    # Make sure the computer's move is not the same as the user's move
    while computer_move == move:
        computer_move = random.choice(['X', 'O'])

    return computer_move

def check_winner(move, computer_move):
    # Check if the user has won
    if move == 'X' and computer_move == 'O':
        winner = 'X'
    elif move == 'O' and computer_move == 'X':
        winner = 'O'

    # Check if the computer has won
    elif computer_move == 'X' and move == 'O':
        winner = 'X'
    elif computer_move == 'O' and move == 'X':
        winner = 'O'

    # Check if the game is a tie
    else:
        winner = 'Tie'

    return winner

# Main
if __name__ == '__main__':
    app.run(debug=True)
