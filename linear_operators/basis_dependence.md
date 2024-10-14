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

The same translation can be performed on $B$:

$$
    [B]_\beta = P^{-1} [B]_\alpha P = P^{-1} [A]_\alpha^{\dagger} P
$$

We see that the relationship between $A$ and $B$ still holds in the new basis

$$
    [B]_\beta = [A]_\beta^{\dagger}
$$

Having defined $B$ to be the conjugate transpose of $A$ in some basis, this relationship continues to hold on translating $A$ and $B$ to an arbitrary new basis. This is what is meant by _basis independence_.

### Transpose
Define a linear operator $B$ to be the transpose of $A$

$$
    [B]_\alpha = [A]_\alpha^{\intercal}
$$

Translate $A$ to a new basis $\beta$

$$
    \begin{align*}
        & [A]_\beta = P^{-1} [A]_\alpha P \\
        & [A]_\beta^{\intercal} = (P^{-1} [A]_\alpha P)^{\intercal} = P^{\intercal} [A]_\alpha^{\intercal} (P^{-1})^{\intercal} \\
    \end{align*}
$$

Translate $B$ to the same basis

$$
    [B]_\beta = P^{-1} [B]_\alpha P = P^{-1} [A]_\alpha^{\intercal} P
$$

For the complex numbers, we that see

$$
    [B]_\beta \neq [A]_\beta^{\intercal}
$$

However, for the real numbers the basis translation operator $P$ is orthogonal, so that

$$
    \begin{align*}
        & [A]_\beta^{\intercal} = P^{\intercal} [A]_\alpha^{\intercal} (P^{-1})^{\intercal} = P^{-1} [A]_\alpha^{\intercal} P \\
        & [B]_\beta = [A]_\beta^{\intercal} \\
    \end{align*}
$$

Therefore, the transpose operation is basis dependent for the complex numbers, but basis independent for the real numbers.

### Complex Conjugate
Define a linear operator $B$ to be the complex conjugate of $A$

$$
    [B]_\alpha = [A]_\alpha^*
$$

Translate $A$ to a new basis $\beta$

$$
    \begin{align*}
        & [A]_\beta = P^{-1} [A]_\alpha P \\
        & [A]_\beta^* = (P^{-1} [A]_\alpha P)^* = (P^{-1})^* [A]_\alpha^* P^* \\
    \end{align*}
$$

Translate $B$ to the same basis

$$
    [B]_\beta = P^{-1} [B]_\alpha P = P^{-1} [A]_\alpha^* P
$$

We see that the complex conjugate is basis dependent:

$$
    [B]_\beta \neq [A]_\beta^*
$$
