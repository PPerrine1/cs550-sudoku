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
    and a set of inferences, solve the CSP using backtrack search

    Pseudocode:
    def backtracking‐search(CSP):
        return backtrack({}, CSP); # call w/ no assignments

    def backtrack(assignment, CSP):
        if all variables assigned, return assignment
        var = select‐unassigned‐variable(CSP, assignment)
        for each value in order‐domain‐values(var, assignment, csp):
            if value consistent with assignment:
                assignment.add({var = value})
                # propagate new constraints (will work without, but probably slowly)
                inferences = inference(CSP, var, assignment)
                if inferences != failure:
                    assignment.add(inferences)
                    result = backtrack(assignment, CSP)
                    if result != failure, return result
        # either value inconsistent or further exploration failed
        # restore assignment to its state at top of loop and try next value
        assignment.remove({var = value}, inferences)
        # No value was consistent with the constraints
        return failure
    """

    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """

        if select_unassigned_variable is None:
            return assignment
        
        var = select_unassigned_variable(csp, assignment)
        for value in order_domain_values(var, assignment, csp):
            if not nconflicts(var, value, assignment):
                assignment.add({var = value})
                # propagate new constraints (will work without, but probably slowly)
                # What is an inference??
                inferences = inference(csp, var, assignment)
                if inferences:
                    assignment.add(inferences)
                    result = backtrack(assignment, csp)
                    if result: 
                        return result
        # either value inconsistent or further exploration failed
        # restore assignment to its state at top of loop and try next value
        assignment.remove({var = value}, inferences)
        # No value was consistent with the constraints
        return failure

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
