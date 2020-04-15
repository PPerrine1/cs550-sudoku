"""
Filename: driver.py

Driver class for Sudoku AI

Demonstrates functionality of the Sudoku class, the backtracking
search function, and the AC3 function. Contains an easy and hard
puzzle for the AI solve.

CS 550, Spring 2020, Marie Roch
@author: mroch, nmill, pperr
"""

from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import (mrv, lcv, forward_checking, mac)
from backtrack import backtracking_search

for puzzle in [easy1, harder1]:
    print("")
    print("Initial sudoku state:")
    s = Sudoku(puzzle)  # construct a Sudoku problem
    s.display(s.infer_assignment())
    print("")

    AC3(s)
    if not s.goal_test(s.curr_domains):
        print("AC3 fails. Running a backtracking search to solve puzzle:")
        solution = backtracking_search(s, select_unassigned_variable=mrv,
                                       order_domain_values=lcv,
                                       inference=mac)
    else:
        print("After AC3 constraint propagation:")
    s.display(s.infer_assignment())
