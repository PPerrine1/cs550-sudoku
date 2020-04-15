"""
Filename: backtrack.py

Contains the backtracking search function for the Sudoku AI.

Implements the Backtracking Search Algorithm from the 
Russell & Norvig text. It is modular in that it allows for differing 
functions for selecting unassigned variables, ordering domain
values, and inference finding to be passed as parameters.

CS 550, Spring 2020, Marie Roch
@author: mroch, nmill, pperr
"""

from csp_lib.backtrack_util import (first_unassigned_variable,
                                    unordered_domain_values,
                                    no_inference)


def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search"""

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """

        # Checks if the assignment is already complete
        if len(assignment) == 81:
            return assignment

        # Selects unassigned variable
        var = select_unassigned_variable(assignment, csp)
        if var is None:
            return assignment

        # For every domain value of the unassigned variable,
        # determine the conflicts, create the list of inferences,
        # and remove any that fail the constraint
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)

                # propagate new constraints 
                removals = csp.suppose(var, value)
                inferences = inference(csp, var, value, assignment, removals)

                # If inferences are found, determine a partial assignment,
                # add it to the assignment, and call backtrack recursively
                # on the new assignment
                if inferences:
                    infer = csp.infer_assignment()[var]
                    csp.assign(var, infer, assignment)
                    curr_result = backtrack(assignment)

                    # If the assignment was successful, return it.
                    # Else, continue.
                    if curr_result:
                        return curr_result

                # Value inconsistent / further exploration failed.
                # Restore assignment to its state at top of loop
                # and try next value (continue loop)
                csp.unassign(var, assignment)
                csp.restore(removals)

        # If no value was consistent with the , return none
        return None

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})

    # Determine the validity of the generated assignment
    # If a valid solution or no solution found, return result respectively
    success = csp.goal_test(result)
    assert result is None or csp.goal_test(result)
    return result
