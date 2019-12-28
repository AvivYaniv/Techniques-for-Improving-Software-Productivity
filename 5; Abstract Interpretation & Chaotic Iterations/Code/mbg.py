bottom = "bottom"
top = "top"

def join(a, b):
    if a == bottom:
        return b
    elif b == bottom:
        return a
    elif a == b:
        return a
    else: return a | b

def meet(a, b):
    if a == top:
        return b
    elif b == top:
        return a
    elif a == b:
        return a
    else: return a & b

# Function returns whether tree contains may-be-garbage variable
# In:
#    rhs    =    Tree expression of variables to examine
#    mbg    =    May-be-garbage variables
def isContainingGarbageVars(rhs, mbg):
    for v in args(rhs):
        if v in mbg:
            return True
    return False

def args(expr_tree):
     yield expr_tree[0]
     for subtree in expr_tree[1]:
             for children in args(subtree):
                     yield children
    
# Transformer for the assignment operation
def assign(mbg, lhs, rhs):
    # If right hand has variables that may-be-garbage
    if (isContainingGarbageVars(rhs, mbg)):
        # Returning union, adding lhs to may-be-garbage
        return mbg | set([lhs])
    # Else lhs after assignment won't be garbage 
    else:
        # Returning difference
        return mbg - set([lhs])
