"""
Constraint propagation
"""

from queue import Queue
import copy


def AC3(sudoku, queue=None, removals=None):
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
    q = Queue()
    unitList = [sudoku.boxes, sudoku.rows, sudoku.cols]

    for unit in unitList:
        for u in unit:
            for i, val in enumerate(u):
                if val == 0:
                    cpyU = copy.deepcopy(u)
                    cpyU.pop(i)
                    for j in cpyU:
                        q.put(u(i), u(j))
    while not q.empty():
        (xi, xj) = q.get()  # get binary constraint
        if revise(sudoku.csp, xi, xj):
            if sudoku.csp.domains(xi) is None:
                return False
            else:
                cpyNeighbors = copy.deepcopy(sudoku.csp.neighbors)
                cpyNeighbors.remove(xj)
                for xk in cpyNeighbors:
                    q.put(xk, xi)
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
    for x in csp.domains(xi):
        conHeld = False
        for y in csp.domains(xj):
            conHeld = (x != y)
            if conHeld:
                break
        if not conHeld:
            csp.domains(xi).remove(x)
            revised = True
    return revised

    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x

