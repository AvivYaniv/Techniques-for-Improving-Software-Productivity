some sig InitialState extends State{}

sig State
{
    successors : set State
}

// some states have more than one successor;
pred NonDeterministicMachine(initialStates: set InitialState) {
	 
	some x: univ| 
	some y:univ-x|
	some p:univ-x-y|
	 x in p.successors and x in p.successors
}

run NonDeterministicMachine for 5
