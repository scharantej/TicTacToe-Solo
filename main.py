 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the POST request
        return render_template('game.html')
    else:
        # Handle the GET request
        return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # Handle the POST request
        return render_template('winner.html')
    else:
        # Handle the GET request
        return render_template('game.html')

@app.route('/winner', methods=['GET'])
def winner():
    # Handle the GET request
    return render_template('winner.html')

if __name__ == '__main__':
    app.run(debug=True)
