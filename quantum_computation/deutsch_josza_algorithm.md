# Deutsch-Josza Algorithm

## Problem Statement
We are tasked with determining whether or not a function $f: \{0, 1\}^n  \rightarrow \{0, 1\}$ is constant or balanced with respect to its input, that is, it takes as input a binary number and returns either 0 or 1 for all possible inputs, or returns 0 for half of the input numbers and 1 for the other half, where $f$ is guaranteed to be one or the other. Such a function is called a black-box or _oracle_, where we cannot see how it works but can only _invoke_ it for some input and receive the corresponding output. The problem here described is known as _Deutsch's Problem_.

## Classical Solution
For a chosen input domain of binary numbers with maximum length $n$ digits, there are $2^{n}$ possible numbers. In the worst case scenario, once we have checked half of the input domain _plus one_ we will know if the oracle is balanced or constant, that is, the oracle must be called at least $2^{n-1} + 1$ times. Therefore the classical solution has running time $O(2^n)$.

## Quantum Solution
The Deutsch-Jozsa algorithm is a more general case of Deutsch's algorithm, where the input is generalized from 1 to $n$ bits. We begin by preparing $n$ qubits in the $\ket{0}$ state and one qubit in the $\ket{1}$ state:

$$
    \ket{\Psi_0} = \ket{0}^{\otimes n} \otimes \ket{1}
$$

The Hadamard transform is applied to all qubits, resulting in the state:

$$
    \ket{\Psi_1} = \sum_x \frac{ \ket{x} }{ \sqrt{2^n} } \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{where} \quad x \in \{0, 1\}^n
$$

TODO complete
