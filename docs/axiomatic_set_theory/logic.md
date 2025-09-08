# Logic

## Propositional Logic

A propostion $p$ is a variable that can be either true or false. It is not the goal of propositional logic to determine if a given proposition is true or false, but rather only to determine the consequences from given propositions using logical operators.

We use logical operators to create new propositions from existing ones. In the sections below some of these operators are shown. Note that symbol used for an operator may vary.

### Unary Operators

| $p$ | $id. \ p$ (identity) | $\neg p$ (not) | $\top p$ (tautology)  | $\bot p$ (contradiction) |
| - | - | - | - | - |
| $t$ | $t$ | $f$ | $t$ | $f$ |
| $f$ | $f$ | $t$ | $t$ | $f$ |

### Binary Operators

In total there are $2^4$ binary logical operators, the most important of which are shown below. The predicate $p$ is known as the "antecendent" and $q$ as the "consequent".

| $p$ | $q$ | $p \land q$ (and) | $p \lor q$ (or)  | $p \veebar q$ (xor) | $p \implies q$ (implication) | $p \iff q$ (equivalence) |
| - | - | - | - | - | - | -|
| $t$ | $t$ | $t$ | $t$ | $f$ | $t$ | $t$ | 
| $t$ | $f$ | $f$ | $t$ | $t$ | $f$ | $f$ | 
| $f$ | $t$ | $f$ | $t$ | $t$ | $t$ | $f$ | 
| $f$ | $f$ | $f$ | $f$ | $f$ | $t$ | $t$ | 

### Material Implication

The implication operator $p \implies q$ is also known as "material implication". The usage of "material" here was used historically to highlight that the relationship between $p$ and $q$ is not causal, in contrast with  "formal implication" where _"... the presence of a certain formal connection between antecedent and consequent is an indispensable condition of the meaningfulness and truth of the implication"_ (Tarski).

In everyday language "implies" often comes with the notion of causality. The material implication $p \implies q$ is not about causality; one must remember that it is simply an operator between two predicates and says nothing about whether they are causally connected. The usefulness of the operator is that we can use it to _communicate_ an assertion, but of course we must still separately _show_ or _prove_ the assertion. For example, if I wish to prove some mathematical theorem $b$ and I believe that proving some predicate $a$ will _show_ that $b$ is true then I can write $a \implies b$ to communicate this assertion but I still need to write the proof for $a$ and show _why_ it also proves $b$.

We may also consider why the material implication takes the values that is does. In the following, we consider a "logically possible universe" as any universe that could exist without contradictions, for example, a universe where a circle has four corners is not logically possible.

* $t \implies t$ - In all logically possible universes a truth can only imply or cause another truth. As the antecedent is true it is restricted by reality and can only imply other truths, so this implication evaluates to true.
* $t \implies f$ - In no logically possible universe could a truth imply a falsehood for the same reason above, so this implication evaluates to false.
* $f \implies t$ - In all logically possible universes a falsehood can imply a truth. Since the antecedent is false it is not rooted in or restricted by reality so it can imply anything you want it to! This implication evaluates to true.
* $f \implies f$ - In all logically possible universes a falsehood can imply a falsehood for the same reason that it can imply a truth. This implication evaluates to true.

### Theorem: Proof by Contradiction

Any assertion can be proven by way of contradiction:

$$
    (p \implies q) \iff (\neg q \implies \neg p)
$$

#### Proof

| $p$ | $q$ | $\neg p$ | $\neg q$  | $p \implies q$ | $\neg q \implies \neg p$ |
| - | - | - | - | - | - |
| $t$ | $t$ | $f$ | $f$ | $t$ | $t$ |
| $t$ | $f$ | $f$ | $t$ | $f$ | $f$ |
| $f$ | $t$ | $t$ | $f$ | $f$ | $f$ |
| $f$ | $f$ | $t$ | $t$ | $t$ | $t$ |

The columns for $(p \implies q)$ and $(\neg q \implies \neg p)$  are identical.

## Predicate Logic

A predicate is a proposition-valued function of some variable(s).

New predicates can be constructed from others, for example:

$$
    Q(x, y, z): \iff P(x) \land R(y, z)
$$

### Quantifiers
New predicates can also be constructed using what are called quantifiers.

"For all $x$, $P(x)$" is written as:

$$
\forall x : P(x)
$$

"There exists an $x$ such that $P(x)$" is defined as:

$$
\exists x : P(x) \iff \neg (\forall x : \neg P(x))
$$

"There exists a unique $x$ such that $P(x)$" is defined as:

$$
\exists! x : P(x) \iff (\exists x : P(x)) \land (\neg \exists y : P(y) \land y \neq x)
$$ 