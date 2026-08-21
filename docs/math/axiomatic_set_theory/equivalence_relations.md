# Equivalence Relations

Let $M$ be a set and $\sim$ a relation such that

1. Reflexivity - $\forall m \in M: m \sim m$
2. Symmetry - $\forall m,n \in M: m \sim n \ \iff \ n \sim m$
3. Transitivity - $\forall m,n,p \in M: m \sim n \ \land \ n \sim p \implies m \sim p$

The relation $\sim$ is called an equivalence relation on $M$.

### Examples

$p \sim q \iff \text{"p is of the same opinion as q"}$

Speaking of people, you must agree with your own opinions (reflexive), if you agree with someone then they agree with you (symmetric), and if that person agrees with a third person and you also agree with the third person (transitive). This is an equivalence relation.

$p \sim q \iff \text{"p is a sibling of q"}$

This is clearly not an equivalence relation as a person cannot be their own sibling (not reflexive).

### Equivalence Classes
Let $\sim$ be an equivalence relation on $M$. Define the set

$$
    [m] := \{ n \in M \ | \ m \sim n \}
$$

called the _equivalence class of_ $m$. There are two key properties of equivalence classes:

1. $a \in [m] \implies [a] = [m]$
2. Either $[a] = [m]$   or  $[a] \ \cap \ [m] = \emptyset $

#### Proof

$$
(a \in [m] \implies [a] = [m]) \implies (a \notin [m] \implies [a] \neq [m]) \\
(\forall n \in [m]: [n] = [m]) \land (a \notin [m] \implies [a] \neq [m]) \implies \forall n \in [m]: n \notin [a]
$$


### Quotient Set
Let $\sim$ be an equivalence relation on $M$. The quotient set $M/\sim$ is given by

$$
    M/\sim \ = \{ [m] \ | \ m \in M \}
$$

where the equivalence classes are members of the power set of $M$:

$$
    [m] \in P(M)
$$

The power set of $M$ is guaranteed to be a set by the Power Set Axiom, confirming that the quotient set is a valid set construction.

#### System of Representatives
By the Axiom of Choice, there exists a complete system of representatives $R$ (a set) for $\sim$ on $M$, that is

$$
    R \cong_{set} M/\sim
$$

Each member of the quotient set can be represented by exactly one of its elements, and these elements form $R$.

### Maps on Quotient Sets
Care must taken when defining maps whose domain is a quotient set when representatives of the equivalence classes are used to define the map. It must be proven that the map is well-defined. For example, consider the integers $\mathbb{Z}$ and the equivalence relation $m \sim n :\iff m - n \in 2\mathbb{Z}$, that is, the difference must be an even integer. The equivalence classes can be written as follows:

$$
    [0] = [2] = [4] = \ldots = [-2] = [-4] \ldots \\
    [1] = [3] = [5] = \ldots = [-1] = [-3] \ldots
$$

Now, how can we define addition on the equivalence classes? On $\mathbb{Z}$ addition is a map $+:\mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$, so let us define the following:

$$
    +:\mathbb{Z}/\sim \ \times \ \mathbb{Z}/\sim \ \to \mathbb{Z}/\sim
$$

where

$$
    [a] + [b] = [a + b]
$$

Is this well-defined? We can select different members of the equivalence classes and we should by definition have the same result:

$$
    [a^\prime] + [b^\prime] = [a^\prime + b^\prime] = [a] + [b] = [a + b]
$$

Is this true?

$$
    [a^\prime] = [a] = a^\prime - a = 2n \quad \text{where} \quad n \in \mathbb{Z} \\
    [b^\prime] = [b] = b^\prime - b = 2m \quad \text{where} \quad m \in \mathbb{Z} \\
    [a^\prime + b^\prime] = [2n - a + 2m - b] = [2(m+n) - (a+b)] \\
    [2(m+n) - (a+b)] \sim [a+b]
$$

The last line follows as clearly $2(m+n)$ is a multiple of 2, and therefore both sides are equivalent and the definition of addition is therefore well-defined.
