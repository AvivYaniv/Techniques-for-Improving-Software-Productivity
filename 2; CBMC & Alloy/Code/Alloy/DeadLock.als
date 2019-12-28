
some sig InitialState extends State{}

sig State
{
    successors : set State
}

pred isReachable(root: InitialState, s: State){
	s in root.*successors
}

//a reachable state that has no successors;
pred deadlock(initialStates: set InitialState) {
	some  s: initialStates |
	some x: s.*successors |
	no n:State | n in x.successors
}

run deadlock for 5
