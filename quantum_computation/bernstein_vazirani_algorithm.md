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
