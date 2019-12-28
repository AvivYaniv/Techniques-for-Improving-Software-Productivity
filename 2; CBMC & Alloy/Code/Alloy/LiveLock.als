some sig InitialState extends State{}

sig State
{
    successors : set State
}


pred isReachable(root: InitialState, s: State){
	s in root.*successors
}

// the possibility of an infinite execution in
// which a state that is always reachable is never reached.
pred livelock(initialStates: set InitialState) {
	some s:initialStates |
	some x : s.*successors| 
	all y : s.*successors |
	 isReachable[x , y] and all z : s.*successors |
	not lone(z.successors) and x in z.successors 
}
run livelock for 4
