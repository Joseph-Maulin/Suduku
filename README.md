# App - SUDOKU PUZZLE IN ACTION!
https://sudoku-jm.herokuapp.com/

# Sudoku
A sudoku puzzle solver and web interface.


# Introduction
This is a web app Sukoku puzzle. It is a heroku hosted flask app using Python, Flask, and JQuery. Click the app below to view..

# What is here?

## Sudoku.py
Sudoku.py is the class that does the suduku puzzle solving. It takes a string of the puzzle delimited by "\n" and "0"s for blanks. It then assembles a two dimensional array of ints to represent the puzzle. The solver then moves throught the blanks in the puzzle and checks for possible solutions. This is done dynamically by reverting to a previous cell if options are eliminated later in the program. A cache is kept for blank cells of what values are possible and what values have been tried. The solution is then saved in the self.solution class variable as a dictionary of {cell_number:value}. Cell numbers are 0-80 row by row.

## app.py
app.py is a simple flask app to run Sudoku.py and then display the puzzle in the web app. Puzzle interaction is done with JQuery in templates/sudoku_puzzle.html

## templates/sudoku_puzzle.html
sudoku_puzzle.html is front end of the app. The interactive puzzle is displayed and interactions are controlled with JQuery/javascript scripting.
