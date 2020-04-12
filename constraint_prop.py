'''
Constraint propagation
'''

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    Pseudocode:
    AC3(CSP):
        “CSP(variables X, domains D, constraints C)”
        q = Queue(binary arcs in CSP)
        while not q.empty():
        (Xi, Xj) = q.dequeue() # get binary constraint
        if revise(CSP, Xi, Xj):
            if domain(Xi) =  return False
            else:
                for each Xk in {neighbors(Xi)‐ Xj}:
                    q.enqueue(Xk, Xi)
        return True

    revise(CSP, Xi, Xj):
        revised = False
        for each x in domain(Xi):
            if not ydomain(Xj) such that constraint holds between x & y:
            delete x from domain(Xi)
            revised = True
        
        return revised

    """
    
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x
    
    raise NotImplemented


