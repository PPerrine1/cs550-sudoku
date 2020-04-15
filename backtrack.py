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
    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        if len(assignment) == 81:
            return assignment

        var = select_unassigned_variable(assignment, csp)
        if var is None:
            return assignment

        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                # propagate new constraints (will work without, but probably slowly)
                # What is an inference??
                removals = csp.suppose(var, value)
                inferences = inference(csp, var, value, assignment, removals)
                if inferences:
                    infer = csp.infer_assignment()[var]
                    csp.assign(var, infer, assignment)
                    curr_result = backtrack(assignment)
                    if curr_result:
                        return curr_result
        # either value inconsistent or further exploration failed
        # restore assignment to its state at top of loop and try next value
                csp.unassign(var, assignment)
                csp.restore(removals)
        # No value was consistent with the constraints
        return None

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})

    success = csp.goal_test(result)
    assert result is None or csp.goal_test(result)
    return result
