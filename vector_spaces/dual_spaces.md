# Dual Spaces

Every vector space $V$ over a field $\mathbb{F}$ has an associated _dual space_ $V^*$, also denoted $L(V, \mathbb{F})$. Elements of the dual space are sometimes called _covectors_.

## Linear Functionals
We define a _linear functional_ on $V$ as a map $\phi: V \to \mathbb{F} $:

$$
    \phi(a \vec u + b \vec v ) = a \phi(\vec u) + b \phi(\vec v) \quad \text{where} \quad \vec u, \vec v \in V \quad a,b \in \mathbb{F}
$$

By this definition the linear functionals are also vector space _homomorphisms_, where the field $\mathbb{F}$ is viewed as a one-dimensional vector space; the dual space is also denoted $Hom(V, \mathbb{F})$ for this reason. These linear functionals are themselves vectors and form the dual space; they can be added and multiplied by scalars from $\mathbb{F}$ to form new linear functionals:

$$
    \phi(\vec u) + \omega(\vec u) = (\phi + \omega)(\vec u)
$$

$$
    a \phi (\vec u) = (a \phi)(\vec u) 
$$

## Dual Basis
For a finite dimensional vector space $V$, let its basis vectors be $\{ e_1, \dots, e_n \}$ and define $n$ linear functionals $\{ \epsilon_1, \dots, \epsilon_n \}$ using the Kronecker delta by

$$
    \epsilon_i (e_k) = \delta_{ik} 
$$

These linear functionals form a basis for $V^*$ known as the _dual basis_, where $dim(V) = dim(V^*)$.

### Proof
To show that these vectors form a basis it is sufficient to show that they are linearly independent, that is, we must show

$$
    \sum_{i=1}^n a_i \epsilon_i = 0 \quad \implies \quad a_i = 0, \forall a_i \in \mathbb{F}
$$

As the basis vectors are linear functionals, we can apply the vector above to any basis vector $e_k \in V$:

$$
    \sum_{i=1}^n a_i \epsilon_i(e_k)  = 0
$$

By the definition of the dual basis vectors, all terms are zero except for when $i = k$

$$
    \begin{align*}
        a_k \epsilon_k(e_k) = 0 \\
        a_k .1  = 0 \\
        a_k = 0
    \end{align*}
$$

## Covectors as Row Vectors
In matrix notation, elements of the dual space $V^*$ can be regarded as row vectors, in contrast to the standard representation of finite dimensional vectors as column vectors. For a vector $\vec v \in V$ and linear functional (covector) $\vec g \in V^*$:

$$
    \begin{align*}
        & \vec w = \sum_{i=1}^n w_i e_i \quad w_i \in \mathbb{F} \\
        & \vec g = \sum_{i=1}^n g_i \epsilon_i \quad g_i \in \mathbb{F} \\
        & g(\vec w) = \sum_{i=1}^n w_i g(e_i) = \sum_{i=1}^n w_i g_i \\
    \end{align*}
$$

This can be represented as the product of a row and column matrix:

$$
    \begin{bmatrix} g_1 & \dots & g_n \end{bmatrix}
    \begin{bmatrix} w_1  \\\ \vdots \\\ w_n \end{bmatrix}
$$

## Visualization
Linear functionals are vectors in their own right in $V^*$ but we can also visualize them in $V$. Recall the equation for a plane in $\mathbb{R}^3$, where $(a,b,c)$ are the components in the $(\hat x, \hat y, \hat z)$ directions of the vector normal to the plane:

$$
    ax + by + cz = d 
$$

Now consider all vectors $\vec v \in \mathbb{R}^3$ for which the linear functional $g$ is equal to some constant $\alpha$. 
This equation is identical in form to the equation of a plane:

$$
    g(\vec v) = g_1 v_1 + g_2 v_2 + g_3 v_3 = \alpha
$$

Therefore, a linear functional can be visualized in $V$ as the set of planes perpendicular to the normal vector whose components are given by $g_i$. This can clearly be extended to hyperplanes in higher dimensions.

![Visualization of Covectors](/img/vector_spaces/covectors.png)

## Dual of the Dual
As $V^*$ is itself a vector space, we can consider the dual  $V^{**}$ of this dual space. TODO
