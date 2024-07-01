# Deutsch-Josza Algorithm

## Problem Statement
We are tasked with determining whether or not a function $f: \{0, 1\}^n  \rightarrow \{0, 1\}$ is constant or balanced with respect to its input, that is, it takes as input a binary number and returns either 0 or 1 for all possible inputs, or returns 0 for half of the input numbers and 1 for the other half, where $f$ is guaranteed to be one or the other. Such a function is called a black-box or _oracle_, where we cannot see how it works but can only _invoke_ it for some input and receive the corresponding output. The problem here described is known as _Deutsch's Problem_.

## Classical Solution
For a chosen input domain of binary numbers with maximum length $n$ digits, there are $2^{n}$ possible numbers. In the worst case scenario, once we have checked half of the input domain _plus one_ we will know if the oracle is balanced or constant, that is, the oracle must be called at least $2^{n-1} + 1$ times. Therefore the classical solution has running time $O(2^n)$.

## Quantum Solution
The Deutsch-Jozsa algorithm is a more general case of Deutsch's algorithm, where the input is generalized from 1 to $n$ bits. We begin by preparing $n$ qubits (known as the query register) in the $\ket{0}$ state and one qubit (known as the answer register) in the $\ket{1}$ state:

$$
    \ket{\Psi_0} = \ket{0}^{\otimes n} \otimes \ket{1}
$$

The Hadamard transform is applied to all qubits, resulting in the state

$$
    \ket{\Psi_1} = \sum_x \frac{ \ket{x} }{ \sqrt{2^n} } \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{where} \quad x \in \{0, 1\}^n
$$

As in Deutsch's algorithm $U_f$ is defined as

$$
    U_f: \ket{x,y} \rightarrow \ket{x, y 
    \oplus f(x)} \quad \text{where} \quad a \oplus b \coloneqq a + b \pmod 2
$$

In this case the input $x$ is the query register and the input $y$ is the answer register. The gate $U_f$ is applied to the state $\ket{\Psi_1}$ resulting in:

$$
        \ket{\Psi_2} = \sum_x \frac{ \ket{x} }{ \sqrt{2^{n+1}} } \otimes \left( \ket{0 \oplus f(x)} - \ket{1 \oplus f(x)} \right) 
$$

Depending on whether $f(x) = 0$ or $f(x) = 1$ the sign of each $\ket{x}$ is flipped, which can be expressed as:

$$
        \ket{\Psi_2} = \sum_x (-1)^{f(x)}\frac{ \ket{x} }{ \sqrt{2^{n+1}} } \otimes \left( \ket{0} - \ket{1} \right) 
$$

We see now that the results of evaluating $f(x)$ on all input $x \in \{0,1\}^n$ are stored in the amplitudes of the superposition state of the query register. We now interfere the terms in the superposition by applying a Hadamard transform to the query register. To understand how to calculate the result of this transform, consider the familiar result of applying a Hadamard gate to the state $\ket{x} =\ket{0}$ or $\ket{x} = \ket{1}$. Both results can be expressed in the following equation:

$$
    H \ket{x} = \sum_k \frac{(-1)^{xk}}{\sqrt{2}} \ket{k} \quad \text{where} \quad k \in \{0, 1\} 
$$

Therefore:

$$
   \ket{\Psi_3} = \sum_x \sum_z \frac{ (-1)^{f(x)} (-1)^{\vec{x} \cdot \vec{z}} }{2^n} \ket{z} \otimes \frac{ \left( \ket{0} - \ket{1} \right) }{\sqrt{2}}  \quad \text{where} \quad \vec{x} \cdot \vec{z} = \sum_{i=1}^n x_i z_i \quad x,z \in \{0, 1\}^n
$$

Notice that for the state where $\ket{z} = \ket{0}^{ \otimes n}$, the amplitude is given by:

$$
    \sum_x \frac{ (-1)^{f(x)} }{2^n}
$$

If $f(x)$ is constant this amplitude equals $+1$ or $-1$, depending on the value of $f(x)$. Because of the normalization condition of a quantum state vector it follows that all other amplitudes must be zero if $f(x)$ is constant. Therefore, if all qubits in the query register when measured are in the $\ket{0}$ state then $f(x)$ is constant. Conversely, if $f(x)$ is balanced then all the terms in the sum for the amplitude of state $\ket{0}^{ \otimes n}$ cancel out so that this amplitude is zero; measuring the query register will result is a state where at least one qubit is $\ket{1}$.