"""
Filename: driver.py

Driver class for the Sudoku AI

Demonstrates functionality of the Sudoku class, the backtracking
search function, and the AC3 function. Contains an easy and hard
puzzle for the AI to solve and then display results.

CS 550, Spring 2020, Marie Roch
@author: mroch, nmill, pperr
"""

from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import (mrv, lcv, forward_checking, mac)
from backtrack import backtracking_search

# Test both puzzles with Sudoku AI
for puzzle in [easy1, harder1]:
    print("")
    print("Initial sudoku state:")
    s = Sudoku(puzzle)  # Construct a Sudoku problem
    s.display(s.infer_assignment())  # Display initial puzzle state
    print("")

    # Utilize AC3 algorithm to solve puzzle
    AC3(s)

    print("After AC3 constraint propagation:")
    # Display solved puzzle
    s.display(s.infer_assignment())

    # If AC3 fails, run backtracking search to solve puzzle
    if not s.goal_test(s.curr_domains):
        print("")
        print("AC3 constraint propagation failed.")
        print("Running a backtracking search to solve puzzle.")
        solution = backtracking_search(s, select_unassigned_variable=mrv,
                                       inference=mac)
        if solution:
            print("Backtracking search successful:")
        else:
            print("Backtracking search failed.")

        s.display(s.infer_assignment())
