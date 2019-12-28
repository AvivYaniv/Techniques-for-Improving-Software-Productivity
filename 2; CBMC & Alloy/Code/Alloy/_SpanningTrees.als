
pred oneRoot [r: univ->univ] {
	one root: univ.r + r.univ | univ.r + r.univ = root.*r
}

pred acyclic  [r: univ->univ] {
	no n: univ.r + r.univ | n in n.^r
}

pred atMostOneParent[r: univ->univ] {
        all n:  univ.r + r.univ | lone parent: univ.r + r.univ | n in parent.^r
}
pred isTree [r: univ->univ] { 
	oneRoot[r]
	acyclic[r]
	atMostOneParent[r]
}

pred spans [r1, r2: univ->univ] {
	let nodes1=univ.r1 + r1.univ{
     	let nodes2=univ.r2 + r2.univ{
			nodes1=nodes2
		}
    }
}

pred show [r, t1, t2: univ->univ] {
spans [t1, r] and isTree [t1]
spans [t2, r] and isTree [t2]
t1 not = t2
}
run show for 4
