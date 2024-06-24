# Quantum Parallelism

## Introduction
Consider the simple function $f: \{0,1\} \rightarrow \{0,1\}$, i.e. a one bit domain and range. The implementation of the function $f$ is not important, only that we can represent it as a unitary transformation $U_f$ in a quantum circuit. We might consider the following circuit with a single input qubit $q$ and a single output classical bit for evaluating the function:

![Naive Circuit](/img/quantum_computation/parallelism/naive_circuit.png)

If we measure the output of this circuit, however, it will behave just like a classical circuit, receiving the classical bits 0 or 1 for input qubit $q = \ket{0}$ or $q = \ket{1}$. There is nothing extraordinary about this circuit. What about leveraging superposition by first applying a Hadamard gate?

![Naive Circuit](/img/quantum_computation/parallelism/naive_circuit_2.png)

Until it is measured, the output state this time is a superposition, however, it is indistinguishable from the output of the Hadamard gate; we cannot tell for which input $x$ we have measured $f(x)$:

$$
    \frac{\ket{f(0)} + \ket{f(1)}}{\sqrt{2}} = \frac{\ket{0} + \ket{1}}{\sqrt{2}}
$$

Instead, consider the following circuit with _two_ input qubits and _two_ output classical bits, where the input qubits are both in the ground state:

$$
    q_0 = \ket{0} \quad q_1 = \ket{0}
$$

![Correct Circuit](/img/quantum_computation/parallelism/correct_circuit.png)

Whatever the implementation of $f$, we can implement the gate $U_f$ so that 

$$
    U_f: \ket{x,y} \rightarrow \ket{x, y \oplus f(x)} \quad \text{where} \quad a \oplus b \coloneqq a + b \pmod 2
$$

where $x$ is the first input of the gate ($q_0$), and $y$ the second input ($q_1$). In the circuit, both input qubits are prepared in the state $\ket{0}$ and then a Hadamard gate is applied to $q_0$ leaving the two states:

$$
    q_0 = \frac{ \ket{0} + \ket{1} }{\sqrt{2}} \quad q_1 = \ket{0}
$$

Since $q_1$ is prepared in the state $\ket{0}$, addition modulo 2 with this qubit is equivalent to evaluating the function on the gate's input $x$:

$$
    0 \oplus f(x) = f(x)
$$

The gate $U_f$ therefore results in the output state

$$
    \frac{ \ket{0, f(0)} + \ket{1, f(1)} }{\sqrt{2}}
$$

This is a remarkable state! In a _single_ application of the gate $U_f$ the output state contains both values $f(0)$ and $f(1)$, and unlike before, we know for which input we have received $f(x)$ due to the value of the first qubit. Of course, if we measure the output state we will get information on only one of the values of $f(x)$ and not both, since the superposition will collapse.

## Generalizing to N Qubits
Applying a Hadamard gate to $n$ qubits in parallel, each in the initial state $\ket{0}$, results in the state:

$$
    \frac{1}{\sqrt{2^n}} \sum_x \ket{x}
$$

where the sum is over all possible values of $x$. Thus, parallel evaluation of a function with n-bit input $x$ and 1-bit output, $f(x)$, can be achieved in the following way:

1. Prepare the initial $n+1$ qubit state $\ket{0}^{\otimes n}\ket{0}$.
2. Apply a Hadamard gate to the first $n$ qubits.
3. Apply the quantum circuit $U_f$ implementing the function $f$.

The outcome of the steps above is the state

$$
    \frac{1}{\sqrt{2^n}} \sum_x \ket{x} \ket{f(x)}
$$

Although the resulting state is a superposition of all possible outcomes of $f$, we can only measure _one_ value. Quantum computation requires something more than just quantum parallelism in order to extract information about more than one value of $f$. Deutsch's algorithm demonstrates one example.

## Deutsch's Algorithm
Suppose we do not know if the functiona $f$ is constant or balanced, that is, is $f(0) = f(1)$ or $f(0) \ne f(1)$? Let us start with the states

$$
    q_0 = \ket{0} \quad q_1 = \ket{1}
$$

Consider the circuit shown below where a Hadamard gate is applied to both input qubits:

![Deutsch](/img/quantum_computation/parallelism/deutsch.png)

The Hadamard gates produce the following total state:

$$
    \begin{align*}
        \ket{\Psi_1} &= \left( \frac{ \ket{0} + \ket{1} }{ \sqrt{2} } \right) \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \\
        &= \frac{ \ket{00} - \ket{01} + \ket{10} - \ket{11} }{2} \\
    \end{align*}
$$

Depending on the value of $f(x)$ for the qubit $q_0$, there are four possible output states:

$$
    \begin{align*}
        & f(0) = 0, f(1) = 1 \\
        & \ket{\Psi_2} = \frac{ \ket{00} - \ket{01} + \ket{11} - \ket{10} }{2} \\
    \end{align*}
$$

$$
    \begin{align*}
        & f(0) = 1, f(1) = 0 \\
        & \ket{\Psi_2} = \frac{ \ket{01} - \ket{00} + \ket{10} - \ket{11} }{2} \\
    \end{align*}
$$

$$
    \begin{align*}
        & f(0) = 0, f(1) = 0 \\
        & \ket{\Psi_2} = \frac{ \ket{00} - \ket{01} + \ket{10} - \ket{11} }{2} \\
    \end{align*}
$$

$$
    \begin{align*}
        & f(0) = 1, f(1) = 1 \\
        & \ket{\Psi_2} = \frac{ \ket{01} - \ket{00} + \ket{11} - \ket{10} }{2} \\
    \end{align*}
$$

The only difference between these output states is that the sign is flipped for each ket. We can group the output states by whether or not $f$ is balanced or constant:

$$
    \begin{align*}
        \pm \left( \frac{ \ket{0} + \ket{1} }{ \sqrt{2} } \right) \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{(constant)} \\
        \pm \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{(balanced)} \\
    \end{align*}
$$

Applying the final Hadamard gate to $q_0$ we have the possible states

$$
    \begin{align*}
        \pm \ket{0} \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{(constant)} \\
        \pm \ket{1} \otimes \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right) \quad \text{(balanced)} \\
    \end{align*}
$$

Since $f(0) \oplus f(1) = 0$ if $f$ is constant and 1 if $f$ is balanced, the state can be written concisely as

$$
    \pm \ket{f(0) \oplus f(1)} \left( \frac{ \ket{0} - \ket{1} }{ \sqrt{2} } \right)
$$

Therefore, by measuring the qubit $q_0$ we can determine if the function is balanced or constant, having applied the gate $U_f$ only once, i.e. having evaluated $f$ only once. Any classical solution must evaluate the function $f$ at least two times, thus showing how a quantum algorithm can outperform any possible classical algorithm for this problem.
