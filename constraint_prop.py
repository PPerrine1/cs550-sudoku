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
    # the neighbors list from the CSP
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

        # Return false if Xi is found to have no elements in curr_domains
        # after revise() is called.
        if revise(csp, xi, xj, removals):
            if not csp.curr_domains[xi]:
                return False
            # If revise() returns True and there are elements in curr_domains,
            # Remove Xj from Xi's neighbors, then add binary constraint (Xk, Xi)
            # to the queue for each Xk in Xi, add Xj back to Xi's neighbors
            else:
                csp.neighbors[xi].remove(xj)
                for xk in csp.neighbors[xi]:
                    queue.append((xk, xi))
                csp.neighbors[xi].add(xj)
    return True


def revise(csp, xi, xj, removals):
    """AC3 revise function"""

    revised = False

    # For each domain value of Xi, verify the constraint holds with
    # at least 1 domain value in Xj. If not, delete the value from Xi's domain
    for x in csp.curr_domains[xi][:]:
        conHeld = False
        for y in csp.curr_domains[xj][:]:
            conHeld = csp.constraints(xi, x, xj, y)
            if conHeld:
                break
        # Prune any domain value of Xi in which the constraint is not held.
        if not conHeld:
            csp.prune(xi, x, removals)
            revised = True
    return revised
