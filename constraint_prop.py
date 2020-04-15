"""
Constraint propagation
"""


def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation"""

    if not queue:
        queue = []
        for i in csp.neighbors:
            for j in csp.neighbors[i]:
                queue.append((i, j))

    if not removals:
        removals = []

    while queue:
        (xi, xj) = queue.pop()  # get binary constraint
        if revise(csp, xi, xj, removals):
            if csp.domains[xi] is None:
                return False
            else:
                tmp = csp.neighbors[xi].remove(xj)
                for xk in csp.neighbors[xi]:
                    queue.append((xk, xi))
                csp.neighbors[xi].add(xj)
    return True


def revise(csp, xi, xj, removals):
    revised = False
    for x in csp.curr_domains[xi][:]:
        conHeld = False
        for y in csp.curr_domains[xj][:]:
            conHeld = csp.constraints(xi, x, xj, y)
            if conHeld:
                break
        if not conHeld:
            csp.prune(xi, x, removals)
            revised = True
    return revised

    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x

