 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/game')
def game():
  return render_template('game.html')

@app.route('/winner')
def winner():
  return render_template('winner.html')

if __name__ == '__main__':
  app.run()


HTML files

html
<!DOCTYPE html>
<html>
<head>
  <title>TicTacToe</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>TicTacToe</h1>
  <button onclick="startGame()">Start Game</button>

  <script src="/static/script.js"></script>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>TicTacToe</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>TicTacToe</h1>

  <div id="game-board">
    <div class="square" onclick="placePiece(0, 0)"></div>
    <div class="square" onclick="placePiece(0, 1)"></div>
    <div class="square" onclick="placePiece(0, 2)"></div>
    <div class="square" onclick="placePiece(1, 0)"></div>
    <div class="square" onclick="placePiece(1, 1)"></div>
    <div class="square" onclick="placePiece(1, 2)"></div>
    <div class="square" onclick="placePiece(2, 0)"></div>
    <div class="square" onclick="placePiece(2, 1)"></div>
    <div class="square" onclick="placePiece(2, 2)"></div>
  </div>

  <script src="/static/script.js"></script>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
  <title>TicTacToe</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>TicTacToe</h1>

  <p>You won!</p>

  <button onclick="startGame()">Start a new game</button>

  <script src="/static/script.js"></script>
</body>
</html>


CSS

css
body {
  font-family: sans-serif;
}

h1 {
  font-size: 36px;
}

button {
  font-size: 16px;
  padding: 8px 16px;
  background-color: #000;
  color: #fff;
}

.square {
  width: 50px;
  height: 50px;
  border: 1px solid #000;
  float: left;
  margin: 4px;
}


JavaScript

javascript
function startGame() {
  // Initialize the game board.
  var gameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null]
  ];

  // Render the game board.
  renderGameBoard(gameBoard);
}

function placePiece(row, col) {
  // Check if the square is already occupied.
  if (gameBoard[row][col] !== null) {
    return;
  }

  // Place the piece on the game board.
  gameBoard[row][col] = 'X';

  // Render the game board.
  renderGameBoard(gameBoard);

  // Check if the game is over.
  if (checkGameOver(gameBoard)) {
    // The game is over. Display the winner.
    alert('You won!');
  }
}

function renderGameBoard(gameBoard) {
  // Get the game board element.
  var gameBoardElement = document.getElementById('game-board');

  // Clear the game board element.
  gameBoardElement.innerHTML = '';

  // Loop through the game board and create a square for each element.
  for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      var square = document.createElement('div');
      square.className = 'square';
      square.onclick = function() {
        placePiece(i, j);
      };

      // Set the square's inner HTML to the value of the game board element.
      square.innerHTML = gameBoard[i][j];

      // Append the square to the game board element.
      gameBoardElement.appendChild(square);
    }
  }
}

function checkGameOver(gameBoard) {
  // Check if there is a winner.
  for (var i = 0; i < 3; i++) {
    if (gameBoard[i][0] === 'X' && gameBoard[i][1] === 'X' && gameBoard[i][2] === 'X') {
      return true;
    }
    if (gameBoard[0][i] === 'X' && gameBoard[1][i] === 'X' && gameBoard[2][i] === 'X') {
      return true;
    }
    if (gameBoard[i][0] === 'X' && gameBoard[1][1] === 'X' && gameBoard[2][2] === 'X') {
      return true;
    }
    if (gameBoard[0][2] === 'X' && gameBoard[1][1] === 'X' && gameBoard[2][0] === 'X') {
      return true;
    }
  }

  // Check if there is a tie.
  for (var i = 0; i < 3; i++) {
    if (gameBoard[i][0] !== null && gameBoard[i][1] !== null && gameBoard[i][2] !== null) {
      return false;
    }
    if (gameBoard[0][i] !== null && gameBoard[1][i] !== null && gameBoard[2][i] !== null) {
      return false;
    }
    if (gameBoard[i][0] !== null && gameBoard[1][1] !== null && gameBoard[2][2] !== null) {
      return false;
    }
    if (gameBoard[0][2] !== null && gameBoard[1][1] !== null && gameBoard[2][0] !== null) {
      return false;
    }
  }

  return true;
}


main.py


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/game')
def game():
  return render_template('game.html')

@app.route('/winner')
def winner():
  return render_template('winner.html')

if __name__ == '__main__':
  app.run()
