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

    while queue:
        (xi, xj) = queue.pop()  # get binary constraint
        if revise(csp, xi, xj, removals):
            if not csp.curr_domains[xi]:
                return False
            else:
                csp.neighbors[xi].remove(xj)
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

