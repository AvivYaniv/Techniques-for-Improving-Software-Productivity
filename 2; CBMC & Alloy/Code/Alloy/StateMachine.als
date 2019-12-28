some sig InitialState extends State{}

sig State
{
    successors : set State
}

// acyclic
//fact { no s: State | s in s.^successors } 

// state machine is connected
// fact { State in InitialState.*successors }

// fact { no x:InitialState | x in State.^successors }

 //  each state has at most one successor
pred DeterministicMachine(initialStates: set InitialState) {
	 all s: initialStates |
	 all x: s.*successors |
	 lone (x.successors)
}

run DeterministicMachine for 5


