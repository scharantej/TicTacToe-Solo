 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=["POST"])
def game():
    # Get the user's move.
    move = request.form.get("move")

    # Make the computer's move.
    computer_move = "X" if move == "O" else "O"

    # Check if the game is over.
    winner = check_winner(move, computer_move)

    # Return the game state.
    return render_template("game.html", move=move, computer_move=computer_move, winner=winner)

@app.route("/winner", methods=["POST"])
def winner():
    # Get the winner's name.
    winner = request.form.get("winner")

    # Return the winner's name.
    return render_template("winner.html", winner=winner)

def check_winner(move, computer_move):
    # Check if the user has won.
    if move == "X" and (move in ["1", "2", "3"] or move in ["4", "5", "6"] or move in ["7", "8", "9"]):
        return "X"

    # Check if the computer has won.
    if computer_move == "O" and (computer_move in ["1", "2", "3"] or computer_move in ["4", "5", "6"] or computer_move in ["7", "8", "9"]):
        return "O"

    # Check if the game is a draw.
    if move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and computer_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return "Draw"

    # The game is not over yet.
    return None

if __name__ == "__main__":
    app.run()
