"""
k-clique exercise.
"""

from z3 import *

Petersen_V = range(10)
Petersen_E = [
    (0 , 1),
    (1 , 2),
    (2 , 3),
    (3 , 4),
    (4 , 0),

    (0 , 5),
    (1 , 6),
    (2 , 7),
    (3 , 8),
    (4 , 9),

    (5 , 7),
    (7 , 9),
    (9 , 6),
    (6 , 8),
    (8 , 5),
 ]

simple_V = [0, 1, 2, 3]
simple_E = [
    (0, 1),
    (1, 2),
    (2, 0),
    (2, 3),
]

up_five_V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
up_five_E = [
	(1,0),
	(2,0),
	(2,1),
    (2,7),
	(3,1),
	(5,4),
	(6,4),
	(6,5),
	(7,4),
	(7,5),
	(7,6),
	(8,4),
	(8,5),
	(8,6),
	(8,7),
]

def get_k_clique(k, V, E):
    #
    # Your solution here...
    #
    assert V == range(len(V))
    clique = range(k)
    variables = [[Bool('v_{}_clique_{}'.format(v, j)) for j in clique] for v in V]

    s = Solver()

    # Some node is the j-ish node of the clique (1<=j<=k)
    for j in clique:
        s.add(Or([variables[v][j] for v in V]))

    # Every node is participating in the clique at most once
    for v in V:
        for j1 in range(k):
            for j2 in range(j1 + 1, k):
                s.add(Or(Not(variables[v][j1]),
                         Not(variables[v][j2])))

    EE = set()
    for v1, v2 in E:
        EE.add((v1, v2))
        EE.add((v2, v1))
    # Non edges cannot be part of the clique
    for v1 in V:
        for v2 in V:
            if (v1, v2) not in EE:
                for j1 in range(k):
                    for j2 in range(j1 + 1, k):
                        s.add(Or(Not(variables[v1][j1]),
                                 Not(variables[v2][j2])))
            
    print "Solver is:"
    print s
    print

    print "Checking SAT"
    res = s.check()
    if res == unsat:
        print "UNSAT, No K clique"
        return None
    elif res == unknown:
        print "Unknown"
        return None
    else:
        assert res == sat
        print "SAT, Found K clique"
        m = s.model()
        clique_nodes = dict()
        for v in V:
            for j in clique:
                if is_true(m[variables[v][j]]):
                    clique_nodes[v] = j
                    break
        return clique_nodes

def draw_graph(V, E, clique=[], filename='graph', engine='circo'):
    try:
        from graphviz import Graph, Digraph
    except ImportError:
        print "You don't have graphviz python interface installed. Sorry."
        return

    dot = Graph(engine=engine)
    for v in V:
        if v in clique:
            dot.node(str(v), style="filled", fillcolor='red')
        else:
            dot.node(str(v))
    for v1, v2 in E:
        dot.edge(str(v1), str(v2))
    dot.render(filename, cleanup=True, view=True)


if __name__ == '__main__':
    #
    # Your tests here...
    #

	"""
	c = get_k_clique(2, simple_V, simple_E)
	if c:
		draw_graph(simple_V, simple_E, c, 'simple')
	"""

	c = get_k_clique(5, up_five_V, up_five_E)
	if c:
		draw_graph(up_five_V, up_five_E, c, 'up_five')

	"""
	c = get_k_clique(3, Petersen_V, Petersen_E)
	if c:
		draw_graph(Petersen_V, Petersen_E, c, 'Petersen')
	"""
    
	print "Sabich"
	pass
