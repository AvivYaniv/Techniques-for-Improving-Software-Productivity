"""
k-vertex-cover exercise.
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

upp_five_V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
upp_five_E = [
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

up_five_V = range(6)
up_five_E = [
    (1,0),
    (2,0),
    (2,1),
    (3,1),
    (3,2),
    (4,2),
    (5,4),
]

younis_V = range(6)
younis_E = [
    (1,0),
    (2,0),
    (2,1),
    (3,1),
    (3,2),
    (4,2),
    (5,4),
]

def get_k_vertex_cover(k, V, E):
    #
    # Your solution here...
    #

    assert V == range(len(V))
    cover = range(k)
    variables = [[Bool('v_{}_cover_{}'.format(v, c)) for c in cover] for v in V]

    s = Solver()

    n = len(V)


    # At most K vertices 
    for c in cover:
        for v1 in range(n):
            for v2 in range(v1+1, n):
                s.add(Or(Not(variables[v1][c]),
                         Not(variables[v2][c])))


 
	#check that every edge is covered
	edge_variables = [Bool(str(E[i])) for i in range(len(E))]
	for i in range(len(E)):
		v1 , v2 = E[i]
		s.add(Or([variables[v1][c] for c in cover] +[variables[v2][c] for c in cover] + [Not(edge_variables[i])]))   #one vertix at least -> edge satisfied
		s.add(Or(Not(Or([variables[v1][c] for c in cover] +[variables[v2][c] for c in cover])), edge_variables[i]))  #edge satisfied -> one vertix at least
	

                             
    print "Solver is:"
    print s
    print

    print "Checking SAT"
    res = s.check(edge_variables)
    if res == unsat:
		ans = []
		print "UNSAT, No K vertex cover"
		core = s.unsat_core()
		print "UNSAT core:", core
		
		for i in core:
			ans.append(i)
		return ans
    elif res == unknown:
        print "Unknown"
        return None
    else:
        assert res == sat
        print "SAT, Found K vertex cover"
        m = s.model()
        vertex_cover = []
        for c in cover:
            for v in V:
                if is_true(m[variables[v][c]]):
                    vertex_cover.append(v)
                    break
        return vertex_cover

    pass


def draw_graph(V, E, cover=[], filename='graph', engine='circo'):
    try:
        from graphviz import Graph, Digraph
    except ImportError:
        print "You don't have graphviz python interface installed. Sorry."
        return

    dot = Graph(engine=engine)
    for v in V:
        if v in cover:
            dot.node(str(v), style="filled", fillcolor='green')
        else:
            dot.node(str(v))
    for v1, v2 in E:
        if (v1, v2) in cover:
            dot.edge(str(v1), str(v2), color='red')
        else:
            dot.edge(str(v1), str(v2))
        
    dot.render(filename, cleanup=True, view=True)

if __name__ == '__main__':
    #
    # Your tests here...
    #
    k = 4
    cover = get_k_vertex_cover(k, upp_five_V, upp_five_E)
    if cover:
       # draw_graph(upp_five_V, upp_five_E, cover, 'up_five'+str(k))
	print cover
    
    pass





