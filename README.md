[![HitCount](http://hits.dwyl.com/AvivYaniv/Techniques-for-Improving-Software-Productivity.svg)](http://hits.dwyl.com/AvivYaniv/Techniques-for-Improving-Software-Productivity)

# Techniques-for-Improving-Software-Productivity

Developing correct and reliable software is considered a very difficult task. <br/>
This is a unique course that teaches students novel testing and verification techniques for improving software productivity. <br/>
The techniques reduce the cost of software development and improve robustness of software. <br/>
These techniques have been developed in the last two decades and are becoming more mature. <br/>
Many of the techniques are now implemented in research and some commercial tools. <br/>

This course focuses on pragmatical aspects. <br/>
The students will gain more understanding on existing tools, their relevance, and limitations. <br/>

<p align="center">
    <img src="https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/logo/AbstractInterpretationOfIntegersBySigns.svg" width="50%"/>
<p/>

## Homeworks
[Homework 1](https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/1%3B%20SAT%20%26%20SMT/soft-prod_ex1.pdf) : <br/>
- [SAT](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#Unrestricted_satisfiability_(SAT)) : [K-Clique](https://en.wikipedia.org/wiki/Clique_problem) solving with [Z3](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) <br/>
- Unsat Core : [K-Vertex-Cover](https://en.wikipedia.org/wiki/Vertex_cover) solving with [Z3](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) <br/>
- [SMT](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories) solving [Kakuro](https://en.wikipedia.org/wiki/Kakuro) with [Z3](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) <br/>


[Homework 2](https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/2%3B%20CBMC%20%26%20Alloy/soft-prod_ex2.pdf) : [Bounded Model Checking](https://en.wikipedia.org/wiki/Model_checking) <br/>
- [CBMC](http://www.cs.cmu.edu/~modelcheck/cbmc/), a [model checking tool](https://en.wikipedia.org/wiki/Model_checking) <br/>
- [Alloy](https://en.wikipedia.org/wiki/Alloy_(specification_language)), a declarative specification language for expressing complex structural constraints and behavior in a software system <br/>


[Homework 3](https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/3%3B%20KLEE%20%26%20CBMC/soft-prod_ex3.pdf) : [Symbolic Execution](https://en.wikipedia.org/wiki/Symbolic_execution) & [Concolic Testing](https://en.wikipedia.org/wiki/Concolic_testing) <br/>
- [KLEE](https://klee.github.io/), versus [CBMC](http://www.cs.cmu.edu/~modelcheck/cbmc/); detecting bugs in a [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) procedure <br/>
- [KLEE](https://klee.github.io/), versus [CBMC](http://www.cs.cmu.edu/~modelcheck/cbmc/); generating a program bug that [KLEE](https://klee.github.io/) detects and [CBMC](http://www.cs.cmu.edu/~modelcheck/cbmc/) is blind to <br/>


[Homework 4](https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/4%3B%20Dafny/soft-prod_ex4.pdf) : [Deductive Verification Termination](https://en.wikipedia.org/wiki/Formal_verification) <br/>
- [Dafny](https://en.wikipedia.org/wiki/Dafny); an imperative compiled language that targets C# and supports formal specification through preconditions, postconditions, loop invariants and loop variants <br/> 


[Homework 5](https://github.com/AvivYaniv/Techniques-for-Improving-Software-Productivity/blob/master/5%3B%20Abstract%20Interpretation%20%26%20Chaotic%20Iterations/soft-prod_ex5.pdf) : [Abstract Interpretation](https://en.wikipedia.org/wiki/Abstract_interpretation) & [Chaotic Iterations](https://bitbucket.org/tausigplan/chaotic-iterations/) <br/>
- Implementing the May-Be-Grabage analysis <br/> 

## Tools
### Testing Tools
-[Random Testing](https://en.wikipedia.org/wiki/Random_testing) <br/>
-[Unit Testing](https://en.wikipedia.org/wiki/Unit_testing) <br/>
-[Fuzz Testing](https://en.wikipedia.org/wiki/Fuzz_testing) <br/>
-[Mutation Testing](https://en.wikipedia.org/wiki/Mutation_testing) <br/>
-[Delta Debugging](https://en.wikipedia.org/wiki/Delta_Debugging) <br/>

### Symbolic Tools and Verification
-[Bounded Model Checking](https://en.wikipedia.org/wiki/Model_checking) <br/>
-[Concolic Execution](https://en.wikipedia.org/wiki/Concolic_testing) <br/>
-[Floyd-Hoare Style Deductive Verification](https://en.wikipedia.org/wiki/Hoare_logic) <br/>
-[Static Analysis](https://en.wikipedia.org/wiki/Abstract_interpretation) <br/>
-[Proof Assistance](https://en.wikipedia.org/wiki/Coq) <br/>
-[Chaotic Iterations implementation in Python](https://bitbucket.org/tausigplan/chaotic-iterations/) <br/>

### Z3 python interface tutorial
-[Basic](http://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/guide-examples.htm) <br/>
-[Advanced](http://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/advanced-examples.htm) <br/>
-[Strategies](http://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/strategies-examples.htm) <br/>
-[Fixed-Points](http://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/fixedpoints-examples.htm)

### Dafny
-[Dafny Online](http://rise4fun.com/Dafny/) <br/>
-[Basic Tutorial](http://rise4fun.com/Dafny/tutorial) <br/>
-[Dafny Guide](https://research.microsoft.com/en-us/um/people/leino/papers/krml220.pdf) <br/>
-[Dafny Syntax Cheet Sheet](https://docs.google.com/document/d/1kz5_yqzhrEyXII96eCF1YoHZhnb_6dzv-K3u79bMMis/edit?pref=2&pli=1) <br/>
-[Quick Reference](https://www.microsoft.com/en-us/research/project/dafny-a-language-and-program-verifier-for-functional-correctness/) <br/>

### IVy
-[IVy Website](http://microsoft.github.io/ivy/) <br/>
-[Client-Server Tutorial](http://microsoft.github.io/ivy/examples/client_server_example.html) <br/>

### Sketch
-[The Sketch Programmers Manual](https://people.csail.mit.edu/asolar/manual.pdf) <br/>
