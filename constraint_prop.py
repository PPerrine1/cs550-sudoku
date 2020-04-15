"""
Constraint propagation
"""

from queue import Queue
import copy


def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    Pseudocode:
    AC3(CSP):
        “CSP(variables X, domains D, constraints C)”

        # Generate Queue using the constraint function
        in CSP. Binary arcs are binary tuples. The Queue
        should contain every possible combination of squares
        for each empty square's row and column. This function 
        will weed out any values that have been used on the same
        row and column and remove them from the domain of the 
        empty square.

        q = Queue(binary arcs in CSP)
        while not q.empty():
            (Xi, Xj) = q.dequeue() # get binary constraint
            if revise(CSP, Xi, Xj):
                if domain(Xi) =  return False
                else:
                    for each Xk in {neighbors(Xi)‐ Xj}:
                        q.enqueue(Xk, Xi)
        return True
    """
    if not queue:
        queue = Queue()
    if not removals:
        removals = []

    for i in csp.neighbors:
        for j in csp.neighbors[i]:
            queue.put(i, j)
    while not queue.empty():
        (xi, xj) = queue.get()  # get binary constraint
        if revise(csp, xi, xj):
            if csp.domains(xi) is None:
                return False
            else:
                for xk in {csp.neighbors[xi] - xj}:
                    queue.put(xk, xi)
    return True

    """
    revise(CSP, Xi, Xj):
        revised = False
        for each x in domain(Xi):
            if not ydomain(Xj) such that constraint holds between x & y:
            delete x from domain(Xi)
            revised = True
        
        return revised

    """


def revise(csp, xi, xj):
    revised = False
    for x, v in enumerate(csp.domains[xi]):
        conHeld = False
        for y, val in enumerate(csp.domains[xj]):
            conHeld = csp.constraints(None, v, None, val)
            if conHeld:
                break
        if not conHeld:
            csp.removals.put(csp.domains[xi].pop(x))
            revised = True
    return revised

    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x

