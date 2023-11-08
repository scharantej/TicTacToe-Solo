 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    # Get the user's move from the request.
    move = request.form.get('move')

    # Make the computer's move.
    computer_move = get_computer_move(move)

    # Check if the game is over.
    winner = get_winner(move, computer_move)

    # Render the game page with the updated game state.
    return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner', methods=['POST'])
def winner():
    # Get the winner from the request.
    winner = request.form.get('winner')

    # Render the winner page with the winner's name.
    return render_template('winner.html', winner=winner)

if __name__ == '__main__':
    app.run()


html code

html
<!DOCTYPE html>
<html>
<head>
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <div id="game-board">
        <div class="square" data-move="1"></div>
        <div class="square" data-move="2"></div>
        <div class="square" data-move="3"></div>
        <div class="square" data-move="4"></div>
        <div class="square" data-move="5"></div>
        <div class="square" data-move="6"></div>
        <div class="square" data-move="7"></div>
        <div class="square" data-move="8"></div>
        <div class="square" data-move="9"></div>
    </div>
    <div id="controls">
        <button id="new-game">New Game</button>
    </div>
    <script src="/static/js/script.js"></script>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Tic Tac Toe</h1>
    <div id="game-board">
        <div class="square" data-move="1">{{ move }}</div>
        <div class="square" data-move="2">{{ computer_move }}</div>
        <div class="square" data-move="3"></div>
        <div class="square" data-move="4"></div>
        <div class="square" data-move="5"></div>
        <div class="square" data-move="6"></div>
        <div class="square" data-move="7"></div>
        <div class="square" data-move="8"></div>
        <div class="square" data-move="9"></div>
    </div>
    <div id="controls">
        <button id="new-game">New Game</button>
    </div>
    <script src="/static/js/script.js"></script>
</body>
</html>


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
        {{ winner }} has won!
    </div>
    <div id="controls">
        <button id="new-game">New Game</button>
    </div>
    <script src="/static/js/script.js"></script>
</body>
</html>


css
body {
    font-family: sans-serif;
}

#game-board {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
}

.square {
    width: 100px;
    height: 100px;
    border: 1px solid black;
    text-align: center;
    font-size: 30px;
}

#controls {
    text-align: center;
}

#new-game {
    padding: 10px 20px;
    background-color: #000;
    color: #fff;
    border: 1px solid #000;
    cursor: pointer;
}


javascript
// Get the game board element.
const gameBoard = document.getElementById('game-board');

// Get the squares on the game board.
const squares = gameBoard.querySelectorAll('.square');

// Add a click event listener to each square.
squares.forEach(square => {
    square.addEventListener('click', () => {
        // Get the move number for the square.
        const move = square.dataset.move;

        // Make a request to the server to make the move.
        fetch('/game', {
            method: 'POST',
            body: JSON.stringify({ move }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            // Update the game board with the new state.
            square.innerHTML = data.move;
            gameBoard.querySelector(`[data-move="${data.computer_move}"]`).innerHTML = data.computer_move;

            // Check if the game is over.
            if (data.winner) {
                // Display the winner.
                alert(`${data.winner} has won!`);

                // Reset the game.
                resetGame();
            }
        });
    });
});

// Add a click event listener to the new game button.
document.getElementById('new-game').addEventListener('click', () => {
    // Reset the game.
    resetGame();
});

// Reset the game.
function resetGame() {
    // Clear the game board.
    squares.forEach(square => {
        square.innerHTML = '';
    });

    // Make a request to the server to start a new game.
    fetch('/game', {
        method: 'POST',
        body: JSON.stringify({}),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        // Update the game board with the new state.
        square.innerHTML = data.move;
        gameBoard.querySelector(`[data-move="${data.computer_move}"]`).innerHTML = data.computer_move;
    });
}
