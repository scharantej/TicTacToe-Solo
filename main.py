 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
  # Get the user's move.
  move = request.form.get('move')

  # Make the computer's move.
  computer_move = get_computer_move()

  # Check if the game is over.
  winner = check_winner()

  # Render the game page.
  return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner', methods=['POST'])
def winner():
  # Get the winner.
  winner = request.form.get('winner')

  # Render the winner page.
  return render_template('winner.html', winner=winner)

def get_computer_move():
  # Get the available moves.
  available_moves = get_available_moves()

  # Choose a random move.
  computer_move = random.choice(available_moves)

  return computer_move

def check_winner():
  # Check if there is a winner.
  winner = None

  # Check if there is a row with three of the same symbol.
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2]:
      winner = board[row][0]

  # Check if there is a column with three of the same symbol.
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col]:
      winner = board[0][col]

  # Check if there is a diagonal with three of the same symbol.
  if board[0][0] == board[1][1] == board[2][2]:
    winner = board[0][0]
  elif board[0][2] == board[1][1] == board[2][0]:
    winner = board[0][2]

  return winner

if __name__ == '__main__':
  app.run()


main.py


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
  # Get the user's move.
  move = request.form.get('move')

  # Make the computer's move.
  computer_move = get_computer_move()

  # Check if the game is over.
  winner = check_winner()

  # Render the game page.
  return render_template('game.html', move=move, computer_move=computer_move, winner=winner)

@app.route('/winner', methods=['POST'])
def winner():
  # Get the winner.
  winner = request.form.get('winner')

  # Render the winner page.
  return render_template('winner.html', winner=winner)

def get_computer_move():
  # Get the available moves.
  available_moves = get_available_moves()

  # Choose a random move.
  computer_move = random.choice(available_moves)

  return computer_move

def check_winner():
  # Check if there is a winner.
  winner = None

  # Check if there is a row with three of the same symbol.
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2]:
      winner = board[row][0]

  # Check if there is a column with three of the same symbol.
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col]:
      winner = board[0][col]

  # Check if there is a diagonal with three of the same symbol.
  if board[0][0] == board[1][1] == board[2][2]:
    winner = board[0][0]
  elif board[0][2] == board[1][1] == board[2][0]:
    winner = board[0][2]

  return winner

if __name__ == '__main__':
  app.run()
