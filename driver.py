from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, \
    lcv, forward_checking, \
    num_legal_values, mac
from backtrack import backtracking_search

for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)  # construct a Sudoku problem
    s.display(s.infer_assignment())
    solution = backtracking_search(s, select_unassigned_variable=mrv,
                                   order_domain_values=lcv,
                                   inference=mac)
    print()
    s.display(s.infer_assignment())
