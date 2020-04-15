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
                                       inference=mac)
    else:
        print("After AC3 constraint propagation:")
    s.display(s.infer_assignment())
