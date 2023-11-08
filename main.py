 
from flask import Flask, render_template, request

app = Flask(__name__)

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

    # Render the game page
    return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner', methods=['POST'])
def winner():
    # Get the winner
    winner = request.form.get('winner')

    # Render the winner page
    return render_template('winner.html', winner=winner)

def get_computer_move(move):
    # Get the available moves
    available_moves = get_available_moves(move)

    # Choose a random move
    computer_move = random.choice(available_moves)

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

    # Check if the game is a draw
    elif move == computer_move:
        winner = 'Draw'

    # Otherwise, the game is still in progress
    else:
        winner = None

    return winner

def get_available_moves(move):
    # Get the available moves
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))

    return available_moves

if __name__ == '__main__':
    app.run(debug=True)


HTML files:

index.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <div id="board">
        <div class="cell" id="00"></div>
        <div class="cell" id="01"></div>
        <div class="cell" id="02"></div>
        <div class="cell" id="10"></div>
        <div class="cell" id="11"></div>
        <div class="cell" id="12"></div>
        <div class="cell" id="20"></div>
        <div class="cell" id="21"></div>
        <div class="cell" id="22"></div>
    </div>
    <form action="/game" method="post">
        <input type="hidden" name="move" id="move">
        <input type="submit" value="Make Move">
    </form>
</body>
</html>


game.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <div id="board">
        <div class="cell" id="00">{{ move }}</div>
        <div class="cell" id="01">{{ computer_move }}</div>
        <div class="cell" id="02"></div>
        <div class="cell" id="10"></div>
        <div class="cell" id="11"></div>
        <div class="cell" id="12"></div>
        <div class="cell" id="20"></div>
        <div class="cell" id="21"></div>
        <div class="cell" id="22"></div>
    </div>
    <form action="/winner" method="post">
        <input type="hidden" name="winner" id="winner">
        <input type="submit" value="Declare Winner">
    </form>
</body>
</html>


winner.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <div id="winner">
        {{ winner }}
    </div>
</body>
</html>


CSS file:

style.css:

css
body {
    font-family: sans-serif;
}

#board {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
}

.cell {
    width: 100px;
    height: 100px;
    border: 1px solid black;
    text-align: center;
    font-size: 50px;
}


JavaScript file:

script.js:

javascript
// Get the board elements
const cells = document.querySelectorAll('.cell');

// Add event listeners to the board elements
cells.forEach(cell => {
    cell.addEventListener('click', () => {
        // Get the cell's ID
        const id = cell.id;

        // Make the move
        makeMove(id);
    });
});

// Make a move
function makeMove(id) {
    // Get the cell's value
    const value = cells[id].innerHTML;

    // Check if the cell is empty
    if (value === '') {
        // Set the cell's value to 'X'
        cells[id].innerHTML = 'X';

        // Make the computer's move
        computerMove();
    }
}

// Make the computer's move
function computerMove() {
    // Get the available moves
    const availableMoves = getAvailableMoves();

    // Choose a random move
    const randomMove = availableMoves[Math.floor(Math.random() * availableMoves.length)];

    // Make the move
    cells[randomMove].innerHTML = 'O';
}

// Get the available moves
function getAvailableMoves() {
    const availableMoves = [];

    // Loop through the cells
    cells.forEach(cell => {
        // Check if the cell is empty
        if (cell.innerHTML === '') {
            // Add the cell's ID to the list of available moves
            availableMoves.push(cell.id);
        }
    });

    // Return the list of available moves
    return availableMoves;
}
