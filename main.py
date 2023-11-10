 
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the routes for the application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        # Initialize the game state
        game_state = {
            'board': [['', '', ''], ['', '', ''], ['', '', '']],
            'current_player': 'X',
            'winner': None
        }
        return render_template('game.html', game_state=game_state)
    elif request.method == 'POST':
        # Handle the user's move
        move = request.form.get('move')
        game_state['board'][move[0]][move[1]] = game_state['current_player']

        # Check if the game is over
        if check_winner(game_state['board']):
            game_state['winner'] = check_winner(game_state['board'])
            return render_template('winner.html', game_state=game_state)

        # Switch to the next player
        game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'

        return render_template('game.html', game_state=game_state)

@app.route('/winner', methods=['GET'])
def winner():
    game_state = request.args.get('game_state')
    return render_template('winner.html', game_state=game_state)

# Define the function to check for a winner
def check_winner(board):
    # Check for a winner in each row
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]

    # Check for a winner in each column
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]

    # Check for a winner in each diagonal
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None

# Run the application
if __name__ == '__main__':
    app.run()
