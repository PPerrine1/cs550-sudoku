"""
Filename: constraint_prop.py

Contains the AC3 function for the Sudoku AI.

Implements the AC-3 Arc Consistency Algorithm from the 
Russell & Norvig text. This function allows for a given 
CSP object to obtain network arc consistency.

Also contains a helper function, revise, to prune any
pairs in which the constraint is not held. 

CS 550, Spring 2020, Marie Roch
@author: mroch, nmill, pperr
"""

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation"""

    # If there is no given queue, populate the queue using 
    # the neightbors list from the CSP
    if not queue:
        queue = []
        for i in csp.neighbors:
            for j in csp.neighbors[i]:
                queue.append((i, j))

    # Initialize an empty removals list if not given
    if not removals:
        removals = []

    # Iterate through the queue to call revise on each binary constraint.
    while queue:
        (xi, xj) = queue.pop()  # get binary constraint
        # Return false if a variable is found to have no domains in curr_domains
        if revise(csp, xi, xj, removals):
            if not csp.curr_domains[xi]:
                return False
            # Remove xj from xi's neighbors, add
            # every other neighbor to the queue, then add
            # xj back to the list of xi's neightbors
            else:
                csp.neighbors[xi].remove(xj)
                for xk in csp.neighbors[xi]:
                    queue.append((xk, xi))
                csp.neighbors[xi].add(xj)
    return True


def revise(csp, xi, xj, removals):
    """AC3 revise function"""

    revised = False

    # For every domain value of xi, verify the constraint 
    # with every domain value of xj. 
    for x in csp.curr_domains[xi][:]:
        conHeld = False
        for y in csp.curr_domains[xj][:]:
            conHeld = csp.constraints(xi, x, xj, y)
            if conHeld:
                break
        # Prune any pair in which the constraint is not held. 
        if not conHeld:
            csp.prune(xi, x, removals)
            revised = True
    return revised

