## Linear Operators

## Basis Dependence
Some operations performed on a linear operator depend on the basis chosen to represent the operator, while others do not. For a basis dependent operation we must specify in which basis we are performing the operation in order to fully describe that operation, however, for basis independent operations we do not need to specify the basis.

### Conjugate Transpose
For operators over the complex numbers, the conjugate transpose (Hermitian conjugate) is basis independent. Let $\left[  A \right] _\alpha$ be an operator $A$ represented on the basis $\alpha$, and define a new operator $B$ equal to its conjugate transpose:

$$
    \left[ B\right] _\alpha = \left[ A\right] _\alpha^{\dagger}
$$

Translating the linear operator $A$ to a new basis is given by a _similarity transformation_ with a unitary operator $P$:

$$
    \begin{align*}
        & \left[ A\right] _\beta = P^{-1} \left[ A\right] _\alpha P \\
        & \left[ A\right] _\beta^{\dagger} = (P^{-1} \left[ A\right] _\alpha P)^{\dagger} = P^{-1} \left[ A\right] _\alpha^{\dagger} P \\
    \end{align*}
$$

The same translation can be performed on $B$:

$$
    \left[ B\right] _\beta = P^{-1} \left[ B\right] _\alpha P = P^{-1} \left[ A\right] _\alpha^{\dagger} P
$$

We see that the relationship between $A$ and $B$ still holds in the new basis

$$
    \left[ B\right] _\beta = \left[ A\right] _\beta^{\dagger}
$$

Having defined $B$ to be the conjugate transpose of $A$ in some basis, this relationship continues to hold on translating $A$ and $B$ to an arbitrary new basis. This is what is meant by _basis independence_.

### Transpose
Define a linear operator $B$ to be the transpose of $A$

$$
    \left[ B\right] _\alpha = \left[ A\right] _\alpha^{\intercal}
$$

Translate $A$ to a new basis $\beta$

$$
    \begin{align*}
        & \left[ A\right] _\beta = P^{-1} \left[ A\right] _\alpha P \\
        & \left[ A\right] _\beta^{\intercal} = (P^{-1} \left[ A\right] _\alpha P)^{\intercal} = P^{\intercal} \left[ A\right] _\alpha^{\intercal} (P^{-1})^{\intercal} \\
    \end{align*}
$$

Translate $B$ to the same basis

$$
    \left[ B\right] _\beta = P^{-1} \left[ B\right] _\alpha P = P^{-1} \left[ A\right] _\alpha^{\intercal} P
$$

For the complex numbers, we that see

$$
    \left[ B\right] _\beta \neq \left[ A\right] _\beta^{\intercal}
$$

However, for the real numbers the basis translation operator $P$ is orthogonal, so that

$$
    \begin{align*}
        & \left[ A\right] _\beta^{\intercal} = P^{\intercal} \left[ A\right] _\alpha^{\intercal} (P^{-1})^{\intercal} = P^{-1} \left[ A\right] _\alpha^{\intercal} P \\
        & \left[ B\right] _\beta = \left[ A\right] _\beta^{\intercal} \\
    \end{align*}
$$

Therefore, the transpose operation is basis dependent for the complex numbers, but basis independent for the real numbers.

### Complex Conjugate
Define a linear operator $B$ to be the complex conjugate of $A$

$$
    \left[ B\right] _\alpha = \left[ A\right] _\alpha^\star
$$

Translate $A$ to a new basis $\beta$

$$
    \begin{align*}
        & \left[ A\right] _\beta = P^{-1} \left[ A\right] _\alpha P \\
        & \left[ A\right] _\beta^\star = (P^{-1} \left[ A\right] _\alpha P)^\star = (P^{-1})^\star \left[ A\right] _\alpha^\star P^\star \\
    \end{align*}
$$

Translate $B$ to the same basis

$$
    \left[ B\right] _\beta = P^{-1} \left[ B\right] _\alpha P = P^{-1} \left[ A\right] _\alpha^\star P
$$

We see that the complex conjugate is basis dependent:

$$
    \left[ B\right] _\beta \neq \left[ A\right] _\beta^\star
$$
