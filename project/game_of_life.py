"""
"Conway's Game of Life"

Author: Nicole Rouleau
Reviewer: Nhat Le
    Grade (from reviewer): 95

Synopsis:

    This program will run "Conway's Game of Life" based on the of ticks
    and cells initialized into the terminal at the time the program is run.

    eg. python game_of_life.py 40 14:40 15:42
    would run for 40 ticks starting with cell at row 14 and column 40 &
    cell at row 15 and column 42 turned to the ON position.

Conway's game of life works like so:
    Using a 2-D grid of "cells" that begin in either the ON or OFF position
    the program will simulate a living system where cells interact
    with their immediate neighbors. The state of the cells change as time
    progresses; this is due to the number of "ticks", or generations.

    Rules:
        -If the cell is ON and has: less than two ON neighbors or more than
        3 ON neighbors it will turn OFF.
        -If the cell is ON and has 2 or 3 neighbors it will remain ON.
        -If the cell is OFF it will only turn ON if it has 3 neighbors.

    The idea of ON and OFF represent a live or dead cell.
    The neighbors would count as any adjacent cell.


"""
# imports arguments
from sys import argv

# function changes 0's to -'s and 1's to X's and prints
# function sets range of grid to start at 1:1
def print_g(grid, rows, col):
"""

param grid: 2D list of cells
type grid: array of integers that represent cells within the grid
param rows: number of rows in the grid
type rows: integer
param col: number of columns in the grid
type col: integer

"""
    for i in range(rows - 1):
        for j in range(col - 1):
            if grid[i][j] == 1:
                # the end = "" here is so the print does not
                # move on to the next cell over
                print("X", end = "")
            if grid[i][j] == 0:
                print("-", end = "")
        print()
    print()

# function allows for cells to be turned on trhu terminl argument
def on_off(grid, cell):
"""
param grid: 2D list of cells
type grid: array of integers that represent cells within the grid
param cell: specified cells to be acitivated within matrix
type cell: list

"""
    for on in cell:
        # split will split a string into a list
        # in this case allowing the entered numbered of cells in the
        # argument on the command line to be identified and utilized
        i, j = on.split(":")
        # inidcates a cell that is ON
        grid[int(i) - 1][int(j) - 1] = 1

# function defines: grid of neighbors
# and  how rules of grid are determinded based on number of neighbors
def play_game(grid, rows, col):
"""

param grid: 2D list of cells
type grid: array of integers that represent cells within the grid
param rows: number of rows in the grid
type rows: integer
param col: number of columns in the grid
type col: integer

"""
    # new_grid stores the grid of newly determined grid based on rules from ticks
    new_grid = [[0] * col for i in range(rows)]
    for i in range(rows - 1):
        for j in range(col - 1):
            # neighbors assigned based on integers
            # and general matrix neighbor rules of conway game
            neighbors = int(grid[i - 1][j - 1]) + int(grid[i][j - 1])+ \
            int(grid[i + 1][j - 1]) + int(grid[i - 1][j]) + int(grid[i + 1][j]) + \
            int(grid[i - 1][j + 1]) + int(grid[i][j + 1]) + int(grid[i + 1][j + 1])
            # new_grid[i][j] is reset with each cell based on statement above it
            # grid[i][j] here is used because 0 represents an already OFF cell
            # and 1 represents an ON cell
            if grid[i][j] == 1 and neighbors < 2:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and neighbors == 2:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors == 3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbors > 3:
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    # returns newly created grid after rules applied
    return(new_grid)


# function runs argument starting at first on
def main(argv):

    # runs argument starting at first one
    file = argv[0]
    # actually allows ticks to run thru
    ticks = int(argv[1])
    # allows for argument to affect cell indexes indivually
    cell = argv[2:]
    # number of rows (actually -1)
    rows = 31
    # number of columns (actually -1)
    col = 81
    # creates initial grid, storing 0's that will later be chnaged
    grid = [[0] * col for i in range(rows)]
    # creates very first tick
    initial_tick = 0

    # runs functions
    on_off(grid, cell)
    print_g(grid, rows, col)

    # allows arguments for ticks to be created and ran so it goes through
    while ticks > initial_tick:
        # grid is run trhough play_game function and allows new_grid
        # to be initialized in a similar fashion as grid was earlier
        grid = play_game(grid, rows, col)
        # runs function
        print_g(grid, rows, col)
        # takes the first tick at 0 and runs through until desired is achieved
        initial_tick += 1

# executes main in code, needed because of the global import
if __name__ == "__main__":
    main(argv)
