## Axiomatic Systems
An axiomatic system is a finite sequence of propositions $a_1, \dots, a_n$ which are called "axioms".

### Pre-Mathematical Numbers
An objection may immediately be raised about the definition of an axiomatic system just given. In it we define a "sequence of propositions" and proceed to label the axioms with $1, 2, \dots N$, however, if we are in the realm of logic and have not yet defined the notion of a set then how can we talk about the natural numbers? In fact, it does not matter how we label the axioms and we could instead use other lists of unique symbols, for example $|, ||, |||, \dots$ or $\clubsuit, \spadesuit, \heartsuit, \dots$. These are sometimes referred to as "pre-mathematical" numbers and allow us to define a sequence of axioms without depending on the definition of the natural numbers.

## Proofs
A proof of a proposition $p$ within an axiomatic system is a finite sequence of propositions $q_1, \dots, q_m$ such that $q_m \iff p$ and such that for $1 \le j \le m$ one and only one of the following is true:

1. $q_j$ is a proposition from the list of axioms.
2. $q_j$ is a tautology.
3. "Modus ponens": $\exists k, n : 1 \le k,n \lt j : (q_k \land q_n \implies q_j)$ 

If a proposition $p$ can be proven from an axiomatic system $a_1, \dots, a_n$ then we write 

$$
    a_1, \dots, a_n \vdash p
$$

### Modus Ponens
TODO

## Consistency
An axiomatic system is consistent if there exists a proposition $q$ that cannot be proven from the axioms:

$$
    \neg (a_1, \dots, a_n \vdash q)
$$

Consider an axiomatic system that contains contradictory axioms $s,\neg s$.  Then by modus ponens the following is a tautology:

$$
    s \land \neg s \implies q
$$

The left side is a contradiction, i.e. always false, and by the definition of implication this always evaluates to true. We can arrive at the truth of _any proposition_ $q$ ("ex falso quodlibet"). Therefore, it is a sign of consistency of an axiomatic system if there exists a proposition that cannot be proven from the axioms.

### Theorem: Consistency of Propositional Logic