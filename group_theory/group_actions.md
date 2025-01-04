
## Group Actions

For a group $G$, the _group action_ on a set $X$ is a map $\phi: G \times X \to X$ that takes an element $x \in X$ to a new element $gx \in X$ by the product with $g \in G$. A group action is associative: $g_1(g_2 x) = (g_1g_2)x$ for $g_1, g_2 \in G$.

As the group action maps each element of $X$ to a another element of $X$, i.e. taking the product of $g$ with each element of $X$ creates a permutation of the elements of $X$, the group action can also be seen as a homomorphism between $G$ and the symmetric group, $\gamma: G \to Sym(X)$.

### Orbits

The set of elements for which a given $x \in X$ is mapped to by $G$ is called the _orbit_ of $x$, denoted $Gx \coloneqq \{gx : g \in G \}$.

### Fixed Points

The set of elements of $X$ that are mapped to themselves are called the _fixed points_ of the group action: $\{ x : gx = x \enspace \forall g \in G \}$.

### Transitive Actions

 If for any $x, y \in X$ there is a $g \in G$ such that $gx = y$ the group action is called _transitive_; since every element of $X$ is mapped to every other element by some $g$, there is only _one_ orbit for a transitive group action, i.e. the entire set $X$. If _any_ $x \in X$ has the entire set $X$ as its orbit then the group is transitive as this implies every element is mapped to every other element, for example:

$$
  g_1 x = y, \enspace g_2 x = z \implies g_2 g_1^{-1} z = y
$$

### Faithful/Effective Actions
TODO

### Free Actions
TODO
