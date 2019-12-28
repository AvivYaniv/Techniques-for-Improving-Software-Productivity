some sig InitialState extends State{}

sig State
{
    successors : set State
}


pred isReachable(root: InitialState, s: State){
	s in root.*successors
}

// a machine without unreachable states;
pred reachableMachine(initialStates: set InitialState) {
	all n:univ |
	some s:InitialState|
	n in s.*successors
}

run reachableMachine for 5
