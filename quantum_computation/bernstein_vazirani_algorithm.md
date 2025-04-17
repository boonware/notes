# Bernstein-Vazirani Algorithm

## Problem Statement
Consider a function $f(a, x)$ tha takes two binary numbers $a$ and $x$ of length $n$, computes their inner product and returns the value modulo 2:

$$
    f (a, x) = \langle a, x \rangle \bmod 2 \quad \text{where} \quad a, x \in \{0, 1\}^n
$$

The function is known as an _oracle_ as the number $x$ is hidden and known only to the function, whereas we get to choose $a$ and receive the output value. How can we determine $x$?

## Classical Solution
The value of $x$ can be determined by calling $f$ with $a$ set to each possible permutation of the binary number with 1 in the $i$th position and zeros everywhere else, i.e. $\{0_n \dots 1, ~ 0_n \dots 10, ~ \dots, ~ 1_n \dots 0\}$. The inner product acts as a logical AND operation for any digit pair in the two binary numbers, and by setting $a$ to a number with only a single position containing a 1, if the result of $f$ is 1 then it is known that $x$ contains a 1 in the $i$th position. For a binary number of length $n$, there are clearly $n$ numbers as those just described to pass to $f$, giving this classical algorithm $O(n)$ time complexity to determine all positions of $x$.

## Quantum Solution
TODO

$$
    \sum_{x \in S^n} (-1)^{x \cdot y} = \begin{cases}
      0 & \text{if}\ y \ne 0^n \\
      2^n & \text{if}\ y = 0^n
    \end{cases}
$$

---

### Proof

Case $y = 0^n$:

$$
    \left | S^n \right | = 2^n \implies \sum_{x \in S^n}(-1)^{x \cdot y} = \sum_{x \in S^n}(-1)^{x \cdot 0^{n}} = \sum_{x \in S^n}(-1)^0 = 2^n
$$

Case $y \ne 0^n$:

Let $x = (\ldots b_i \ldots)^n$ represent a string of $n$ bits, where $b_i$ is the bit at position $i$. For each $x \in S^n$ we can define a conjugate bit string $\bar{x}$:

$$
    \forall x, y \in S^n, k \in \N \ | \ y_k = 1 \ \exists! \ \bar{x} \in S^n \ | \ x \cdot y = c \implies \bar{x} \cdot y = c \oplus 1
$$

Let $k$ be some number such that $y_k = 1$, then by the definition of $x \cdot y$ it must be the case that

$$
    x = (\ldots b_k \ldots)^n \implies \bar{x} = (\ldots b_k \oplus 1 \ldots)^n
$$

That is, by flipping only one bit $b_k$ in $x$, which is at the same position as $y_k = 1$ in $y$, we are guaranteed that $x \cdot y$ will also flip:

$$
    (\ldots b_k \ldots)^n \cdot y = c \implies (\ldots b_k \oplus 1\ldots)^n \cdot y = c \oplus 1
$$

$$
    \bar{x} \cdot y = (x \cdot y) \oplus 1
$$

Note that choosing a different $k$ produces a different set of conjugates; the choice of $k$ does not matter as long as it is fixed for all $x \in S$ and $y_k = 1$. For each $x \in S$ its corresponding $\bar{x}$ is unique for the chosen $k$, that is, no two bit strings have the same conjugate; suppose there is another bit string $a$ such that $\bar{a} = \bar{x}$, then

$$
    (\ldots \bar{a}_k \ldots) = (\ldots \bar{x}_k \ldots) = (\ldots x_k \oplus 1 \ldots) \implies a = x
$$

Now, by the definition of $\bar{x}$

$$
    (-1)^{x \cdot y} = - (-1)^{ \bar{x} \cdot y}
$$

Therefore, writing the sum to include both each $x_i$ and its conjugate $\bar{x}_i$, and only summing to $2^n/2$ since each expansion of the sum contains two elements, we have

$$
    \sum_{x \in S^n} (-1)^{x \cdot y} = \sum_{i = 1}^{2^{n-1}} (-1)^{x_i \cdot y} + (-1)^{ \bar{x}_i \cdot y} = 0
$$

---