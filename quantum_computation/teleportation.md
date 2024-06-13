# Quantum Teleportation

Consider a superposition qubit state that Alice wishes to send to Bob:

$$
    \ket{\Psi_A} = \alpha \ket{0}  + \beta \ket{1}
$$

Due to the No-Cloning Theorem this state cannot be copied, however, using quantum teleporation this state _can_ be transferred to Bob. In what follows, the linear algebra calculations are written out explicitly to demonstrate the full procedure.

Alice and Bob share an entangled pair given by

$$
    \ket{\Psi_{AB}} = \frac{1}{\sqrt{2}} (\ket{00} + \ket{11})
$$

The total state of the three-qubit system is given by the following, where by convention the first two qubits in the 3-qubit basis states are Alice's and the third is Bob's:

$$
    \begin{align*}
        \ket{\Psi_{total}} &= \ket{\Psi_A} \otimes \ket{\Psi_{AB}} \\
        &= (\alpha \ket{0}  + \beta \ket{1}) \otimes \frac{1}{\sqrt{2}} (\ket{00} + \ket{11}) \\
        &= \frac{1}{\sqrt{2}} \left( \alpha \ket{000} + \alpha \ket{011} + \beta \ket{100} + \beta \ket{111} \right)
    \end{align*}
$$

Using this convention saves us from using awkward notation such as $\ket{0_{Alice} 0_{Alice} 0_{Bob}}$. Going forward, the tensor product symbol may be dropped for brevity. The state vector $\ket{\Psi_{total}}$ is 8-dimensional as there are  3 qubits giving $2^3$ possible combinations for basis states:

$$
    \ket{000}, \ket{001}, \ket{010}, \ket{011}, \ket{100}, \ket{101}, \ket{110}, \ket{111}
$$

Writing the vector in matrix notation, where the order matches the basis states' order above:

$$
    \Psi_{total}^\intercal = \frac{1}{\sqrt{2}} \begin{bmatrix} & \alpha & 0 & 0 & \alpha & \beta & 0 & 0 & \beta & \end{bmatrix}
$$

Alice now applies a CNOT gate to her two qubits. As the CNOT gate operates on two qubits, i.e. the basis states $\ket{00}, \ket{01}, \ket{10}, \ket{11}$, it is typically presented as a $4 \times 4$ matrix:

$$
    CNOT_4 = \begin{bmatrix}
        & 1 & 0 & 0 & 0 & \\
        & 0 & 1 & 0 & 0 & \\
        & 0 & 0 & 0 & 1 & \\
        & 0 & 0 & 1 & 0 &
    \end{bmatrix}
$$

As the state $\Psi_{total}$ is 8-dimensional, we need to express the CNOT operator in 8 dimensions also:

$$
    CNOT_8 \Psi_{total} = \frac{1}{\sqrt{2}} \begin{bmatrix}
        & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \\
        & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & \\
        & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \\
        & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \\
        & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & \\
        & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & \\
        & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & \\
        & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & \\
    \end{bmatrix}  \begin{bmatrix} \alpha \\ 0 \\ 0 \\ \alpha \\ \beta \\ 0 \\ 0 \\ \beta \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \\ 0 \\ \alpha \\ 0 \\ \beta \\ \beta \\ 0 \end{bmatrix} 
$$

Now, the total state is given by

$$
    \ket{\Psi_{total}} = \frac{1}{\sqrt{2}} \left( \alpha \ket{000} + \alpha \ket{011} + \beta \ket{110} + \beta \ket{101} \right)
$$

Next, a Hadamard gate is applied to Alice's first qubit. The total state can be refactored, noting that $\ket{0} \otimes \ket{01} = \ket{001}$ etc.:

$$
    H = \frac{1}{\sqrt{2}} \begin{bmatrix}
        & 1 & 1 & \\
        & 1 & -1 & \\
    \end{bmatrix}
$$

$$
    \ket{\Psi_{total}} = \frac{1}{\sqrt{2}} \left[ \alpha \ket{0} \left( \ket{00} + \ket{11} \right) + \beta \ket{1} \left( \ket{10} + \ket{01} \right) \right]
$$

$$
    \begin{align*}
        H \Psi_{total} &= \frac{1}{2} \left[ \alpha H \ket{0} \left( \ket{00} + \ket{11} \right) + \beta H \ket{1} \left( \ket{10} + \ket{01} \right) \right] \\
        &= \frac{1}{2} \left[ \alpha \left( \ket{0} + \ket{1} \right) \left( \ket{00} + \ket{11} \right) + \beta \left(\ket{0} - \ket{1} \right) \left( \ket{10} + \ket{01} \right) \right] \\
    \end{align*}
$$


