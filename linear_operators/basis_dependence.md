## Linear Operators

## Basis Dependence
Some operations performed on a linear operator depend on the basis chosen to represent the operator, while others do not. For a basis dependent operation we must specify in which basis we are performing the operation in order to fully describe that operation, however, for basis independent operations we do not need to specify the basis.

### Conjugate Transpose
For operators over the complex numbers, the conjugate transpose (Hermitian conjugate) is basis independent. Let $[A]_\alpha$ be an operator $A$ represented on the basis $\alpha$, and define a new operator $B$ equal to its conjugate transpose:

$$
    [B]_\alpha = [A]_\alpha^{\dagger}
$$

Translating the linear operator $A$ to a new basis is given by a _similarity transformation_ with a unitary operator $P$:

$$
    \begin{align*}
        & [A]_\beta = P^{-1} [A]_\alpha P \\
        & [A]_\beta^{\dagger} = (P^{-1} [A]_\alpha P)^{\dagger} = P^{-1} [A]_\alpha^{\dagger} P \\
    \end{align*}
$$
