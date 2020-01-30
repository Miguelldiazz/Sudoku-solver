from flask import Flask, render_template
from sudoku import Sudoku

app =  Flask(__name__)

@app.route('/')
def index():
    sud = Sudoku(9, 9, 20)
    return render_template('index.html', board = sud.board)


if __name__ == '__main__':
    app.run(debug=True)