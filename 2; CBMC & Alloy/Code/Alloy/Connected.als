
some sig InitialState extends State{}

sig State
{
    successors : set State
}

// every state is reachable from every other state
pred connected(initialStates: set InitialState) {
	 all n:univ |
	some s1:InitialState|
	some s2:InitialState|
	(n in s1.*successors) and (s2 in n.*successors)
}

run connected for 5
