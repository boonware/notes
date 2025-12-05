# Zermelo-Fraenkel Axioms

Set theory is built on the postulate that there is a fundamental _relation_, i.e. a predicate of two variables, called $\in$ (epsilon). A definition of $\in$ is not given, nor is the definition of a set, rather there are nine axioms which speak of $\in$ and sets. These axioms may be remembered with the mnemonic "EE PURP IC F".

* EE - Basic existence axioms.
* PURP - Construction axioms.
* IC - Further existence axioms.
* F - Non-existence axioms.

## 1. The $\epsilon$-Relation
$x \in y$ is a proposition iff $x$ and $y$ are sets:

$$
    \forall x : \forall y : (x \in y) \veebar \neg (x \in y)
$$

We define the negative epsilon relation as follows:

$$
    x \notin y : \iff \neg (x \in y)
$$

### Russel's Paradox
A counter-example is provided by the famous Russel's Paradox where the following proposition is constructed that contains the "sets" $u$ and $z$. One can think of $u$ as "the set of all sets that do not contain themselves".

$$
    \exists u : \forall z  : (z \in u \iff z \notin z )
$$

Is $u \in u$ true or false? According to the proposition above $u \in u \iff u \notin u$, which means $u \in u$ is not a proposition as it must _either_ be true or false, not both. The solution to this paradox is provided by the Axiom of the $\in$-Relation so that $u$ is not a set.

## 2. The Empty Set

$$
    \exists x : \forall y : y \notin x
$$

### Theorem: Uniqueness of the Empty Set

There exists only one empty set, $\emptyset$.

#### Proof: Formal
The following formal proof is given to demonstrate how proofs are constructed using statements in logic.

$$
    \begin{align*}
        \forall y : y \notin x \tag{a1} \\
        \forall y : y \notin x^{\prime} \tag{a2} \\
        \forall y : y \notin x \implies (\forall y : y \in x \implies y \in x^{\prime}) \tag{q1} \\
        (\forall y : y \notin x) \land (\forall y : y \notin x \implies (\forall y: y \in x \implies y \in x^{\prime})) \quad (a1 \land q1) \tag{q2} \\
        \text{Therefore} \quad \forall y: y \in x \implies y \in x^{\prime} \\
        \\
        \forall y : y \notin x^{\prime} \implies (\forall y : y \in x^{\prime} \implies y \in x) \tag{q3} \\
        (\forall y : y \notin x^{\prime}) \land (\forall y : y \notin x^{\prime} \implies (\forall y: y \in x^{\prime} \implies y \in x)) \quad (a2 \land q3) \tag{q4} \\
        \text{Therefore} \quad \forall y: y \in x^{\prime} \implies y \in x \\
        \\
        \text{Therefore} \quad (\forall y: y \in x \implies y \in x^{\prime}) \iff (\forall y: y \in x^{\prime} \implies y \in x) \tag{q5} \\
        \text{Therefore} \quad x = x^{\prime} \tag{q6} \\
    \end{align*}
$$

## 3. Pair Sets
Let $x$ and $y$ be sets. There exists another set that contains both $x$ and $y$.

$$
    \forall x : \forall y : \exists m : \forall u (u \in m \iff u = x \ \lor \ u = y )
$$

We denote $m$ by $\{x, y\}$ where $\{x, y\} = \{y, x\}$.

#### Proof

TODO

## 4. Union Sets
Let $x$ be a set. There exists another set $m$ whose elements are precisely the elements of the elements of $x$, denoted $m = \bigcup x$.

$$
    \forall x : \exists m : \forall a : \forall b : a \in m \iff (a \in b \implies b \in x)
$$

#### Example

$x = \{ \{u\}, \{v\} \} \quad \bigcup x = \{ u, v \}$

### Recursive Unions

Let $a_1, \dots, a_n$ be sets. The union is defined recursively for all $n \ge 3$:

$$
    \{a_1, \dots , a_n \} = \bigcup \{ \{ a_1, \dots, a_{n-1} \}, \{ a_n \} \}
$$
