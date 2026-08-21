# Classification of Sets
A recurring theme in mathematics is the study or classification of structure-preserving maps between spaces. By "space" is meant a set together with some structure on that set. A set is the simplest example of this as it has no additional structure beyond being a set.

## Maps
A map $\phi: A \to B$ is a relation such that for every $a \in A$ there exists exactly one $b \in B$ such that $\phi(a, b)$. Note that we read $\phi(a, b)$ as "$\phi(a, b)$ is true".

The notation $a \mapsto \phi(a)$ is typically used to show how a specific valued is mapped, but we should keep in my that this is an "abuse" of notation and really the map is a relation.

The map $\phi: A \to B$ may also be written $A \xrightarrow{\phi} B$.

### Terminology
* $A$ is the _domain_
* $B$ is the _codomain_ or _target_.
* Image of $A$: $\ \phi(A) \equiv Im_\phi(A) := \{ \phi(a)\ | \ a \in A \} $


### Surjective, Bijective, Injective
The map $\phi: A \to B$ is

* _surjective_ if $\ \phi(A) = B$
* _injective_ if $\ \phi(a_1) = \phi(a_2) \implies a_1 = a_2$
* _bijective_ if both _surjective_ and _injective_.


### Composition of Maps
Given two maps $\phi: A \to B$ and $\psi: B \to C$ we can define another map $\psi \circ \phi: A \to C$, read "psi after phi".

TODO - commuting diagram

Composition is obviously associative:

$$
    \xi \circ (\psi \circ \phi) = (\xi \circ \psi) \circ \phi
$$

### Inverse Map
Let $\phi: A \to B$ be a bijection. The inverse map $\phi^{-1}: B \to A$ is uniquely given by

$$
    \phi^{-1} \circ \phi = id_A \\
    \phi \circ \phi^{-1} = id_B
$$

The indentity map $id$ is defined as follows:

$$
    id_M: M \to M \\
    \forall m \in M: m \mapsto m
$$

### Pre-Image
Let $\phi: A \to B$ be any map. The preimage of $V \subseteq B$ is

$$
    preim_\phi(V) = \{ a \in A \ | \ \phi(a) \in V \}
$$

## Set Isomorphism
Two sets are (set-theoretically) _isomorphic_ if there exists a bijection between them:

$$
    A \cong_{set} B
$$

If there exists _any_ bijection between $A$ and $B$ then there exist many; as the bijection is a pairing of elements between the sets, one can always rearrange the pairings to make new bijections.

## Infinite Sets

A set $A$ is infinite if there is a proper subset $B \subset A$ that is isomorphic, $B \cong_{set} A$. 

As an example, consider $\mathbb{N} \cong_{set} \mathbb{Z}$.  The natural numbers are clearly a proper subset of the integers, and they can be placed in one-to-one correspondence, for example: $1 \mapsto 1$, $2 \mapsto -1$, $3 \mapsto 2$, $4 \mapsto -2$, and so on.

A set $A$ is finite if $A \cong_{set} \{ 1, 2, \ldots, \ n \}$ where $n \in \mathbb{N}$ and $|A| = n$.

### Countable & Uncountable
An infinite set $A$ is _countably infinite_ if $A \cong_{set} \mathbb{N}$, and _uncountably infinite_ otherwise.
