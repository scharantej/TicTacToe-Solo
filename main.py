 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Routes
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/game')
def game():
  return render_template('game.html')

@app.route('/winner/<winner>')
def winner(winner):
  return render_template('winner.html', winner=winner)

@app.route('/tie')
def tie():
  return render_template('tie.html')

@app.route('/move', methods=['POST'])
def move():
  # Get the move from the request
  move = request.form.get('move')

  # Update the game state

  # Check if the game has a winner
  winner = check_winner()

  # Check if the game is a tie
  tie = check_tie()

  # Redirect to the appropriate page
  if winner:
    return redirect(url_for('winner', winner=winner))
  elif tie:
    return redirect(url_for('tie'))
  else:
    return redirect(url_for('game'))

@app.route('/checkWinner', methods=['POST'])
def check_winner():
  # Get the game state from the request
  game_state = request.form.get('game_state')

  # Check if there is a winner
  winner = None
  for row in range(3):
    if game_state[row][0] == game_state[row][1] == game_state[row][2] != ' ':
      winner = game_state[row][0]
    elif game_state[0][row] == game_state[1][row] == game_state[2][row] != ' ':
      winner = game_state[0][row]
    elif game_state[row][0] == game_state[1][1] == game_state[2][2] != ' ':
      winner = game_state[row][0]
    elif game_state[2][0] == game_state[1][1] == game_state[0][2] != ' ':
      winner = game_state[2][0]

  # Return the winner
  return winner

@app.route('/checkTie', methods=['POST'])
def check_tie():
  # Get the game state from the request
  game_state = request.form.get('game_state')

  # Check if the game is a tie
  tie = True
  for row in range(3):
    if game_state[row][0] != ' ' or game_state[row][1] != ' ' or game_state[row][2] != ' ':
      tie = False
      break

  # Return the tie
  return tie

if __name__ == '__main__':
  app.run(debug=True)
