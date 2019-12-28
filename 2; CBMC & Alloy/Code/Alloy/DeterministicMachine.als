some sig InitialState extends State{}

sig State
{
    successors : set State
}



 //  each state has at most one successor
pred DeterministicMachine(initialStates: set InitialState) {
	 all n:univ | lone(n.successors)
	// all s: initialStates |
	 //all x: s.*successors |
	 //lone (x.successors)
}

run DeterministicMachine for 5


