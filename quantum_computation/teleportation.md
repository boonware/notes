

The total state of the three-qubit system is given by

$$
    \begin{align*}
        \ket \Psi_{total} &= (\alpha \ket{0}  + \beta \ket{1}) \otimes \frac{1}{\sqrt{2}} (\ket{00} + \ket{11}) \\
        &= \frac{1}{\sqrt{2}} \left( \alpha \ket{000} + \alpha \ket{011} + \beta \ket{100} + \beta \ket{111} \right)

    \end{align*}
$$

The state vector $\ket \Psi_{total}$ is 8-dimensional as there are  3 qubits giving $2^3$ possible combinations for basis states:

$$
    \ket{000}, \ket{001}, \ket{010}, \ket{011}, \ket{100}, \ket{101}, \ket{110}, \ket{111}
$$

Writing the vector in matrix notation, where the order matches the basis states' order above:

$$
    \Psi_{total}^\intercal = \begin{bmatrix} \alpha & 0 & 0 & \alpha & \beta & 0 & 0 & \beta \end{bmatrix}
$$