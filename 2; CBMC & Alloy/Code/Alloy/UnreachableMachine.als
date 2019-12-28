some sig InitialState extends State{}

sig State
{
    successors : set State
}

pred isReachable(root: InitialState, s: State){
	s in root.*successors
}


// a machine with unreachable states
pred unreachableMachine(initialStates: set InitialState) {
	some n:univ|
	all s: InitialState|
	n not in s.*successors 
	}

run unreachableMachine for 5
