from flask import Flask, render_template
from Suduku import sudoku_solver



app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def puzzle_display():

    p="""
    000100502
    000090000
    098500070
    000061000
    005000040
    920050030
    000704008
    000000709
    350000006
    """

    solver = sudoku_solver(p)
    solver.search()

    return render_template("suduku_puzzle.html", solver=solver)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
