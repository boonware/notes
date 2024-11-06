## Linear Operators

## Matrix Representation
A linear operator can be represented as a matrix. Consider a linear operator $A: V \rightarrow W$ where $dim(V) = n$ and $dim(W) = m$. The vector spaces $V$ and $W$ have basis vectors $v_i$ and $w_i$, respectively. The following holds by linearity

$$
    \begin{align*}
        & A(\sum^n_{i=1} b_i v_i) = \sum^m_{i=1} d_i w_i \\
        & \sum^n_{i=1} b_i A v_i = \sum^m_{i=1} d_i w_i \\
    \end{align*}
$$

Since the right-hand side is a vector in $W$ and the left-hand side is a sum, this sum must be a linear combination of vectors in $W$; a sum of entities which equals to a vector in some space only makes sense if it is a sum of other vectors in that same space. Therefore, we can express each element of the sum from the left-hand side as a vector in $W$, where the constants $b_i$ are omitted as these are the constants of the linear combination and are not part of the individual vectors.

$$
    \begin{align*}
        & A v_i = \sum_{k=1}^m a_{ki} w_k \\
    \end{align*}
$$

We see that $A$ must be a matrix to account for all three possibilities $n = m$, $n < m$ and $n > m$. For example, where $n = 2$ and $m = 3$:

$$
    \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32} \end{bmatrix}
    \begin{bmatrix} v_{1} \\ v_{2} \end{bmatrix} =
    \begin{bmatrix} w_{1} \\ w_{2} \\ w_{3} \end{bmatrix}
$$

Finally, we see that the matrix definition of the operator $A$ depends on both an input basis $v_i$ and an output basis $w_i$.
