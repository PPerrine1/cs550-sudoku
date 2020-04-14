# cs550-sudoku
####Repo for Sudoku AI Project in Python


The code package for this assignment on Blackboard contains a partially implemented
constraint satisfaction problem class for solving Sudoku puzzles. The sudoku module
implements the class Sudoku that is derived from a CSP class (both in module csp_lib).
The code and comments explain the data structures that are used and contain a sample
instantiation of a Sudoku puzzle. The module also provides two sample puzzles, one that
can be solved with constraint satisfaction, the other without.

There is no work to do in the sudoku and csp modules other than to read them and
understand how they work. The task in this assignment is to implement AC3 constraint
propagation in module , backtracking search, and a driver. Template functions are
provided for AC3 in mo and backtracking_search in modules constraint_prop and
backtrack. Both of these operate on a sudoku puzzle and update the current assignments.
When calling your backtrack search, use the minimum remaining values heuristic (which
is implemented in csp_lib.backtrack_util).

Your driver program should create both the easy and hard sudoku problems and then
solve them.

Output: Your code should show for each puzzle:

• Initial sudoku state

• The state of the puzzle after running AC3.

• If the puzzle is not in a goal state (the Sudoku class provides a goal test that can
be used on the instances current domains), then run a backtracking search and
show the solution.