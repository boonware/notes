# Dual Spaces

Every finite-dimensional vector space $V$ over a field $\mathbb{F}$ has an associated _dual space_ $V^\star$, also denoted $L(V, \mathbb{F})$. Elements of the dual space are sometimes called _covectors_. In what follows, for clarity, the "arrow" vector notation is used only for elements of the vector space $V$ unless where necessary to _emphasize_ the vector nature of elements of the dual space.

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

These linear functionals form a basis for $V^\star$ known as the _dual basis_, where $dim(V) = dim(V^\star)$.

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
In matrix notation, elements of the dual space $V^\star$ can be regarded as row vectors, in contrast to the standard representation of finite dimensional vectors as column vectors. For a vector $\vec v \in V$ and linear functional (covector) $\vec g \in V^\star$:

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
Linear functionals are vectors in their own right in $V^\star$ but we can also visualize them in $V$. Recall the equation for a plane in $\mathbb{R}^3$, where $(a,b,c)$ are the components in the $(\hat x, \hat y, \hat z)$ directions of the vector normal to the plane:

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
As $V^\star$ is itself a vector space, we can consider the dual $V^{**}$ of this dual space. For finite dimensional vector spaces, the dualing process stops at the first dual; the dual of the dual space is the original vector space $V$.

Similar to how the linear functionals were defined for $V$, consider a map $\bar\omega: V^\star \to \mathbb{F}$ that acts on the dual space. This maps takes a linear functional $g$ and maps it to an element of the field $\mathbb{F}$, however, there will be some vector $\vec v$ that the linear functional $g$ also maps to the same value in $\mathbb{F}$:

$$
    \bar\omega(g) = g(\vec v) \quad \forall g \in V^\star
$$

The map $\bar\omega$ is a linear functional in its own right. For $g,h \in V^\star$ and $\alpha,\beta \in \mathbb{F}$:

$$  
    \begin{align*}
        \bar\omega(\alpha g + \beta h) = (\alpha g + \beta h)(\vec v) \\
        = \alpha g(\vec v) + \beta h(\vec v) \\
        = \alpha \bar \omega(g) + \beta \bar \omega(h) \\
    \end{align*}
$$

As there is a way to associate every $v \in V$ with an $\bar{\omega} \in V^{**}$, this implies the existence of a map $\rho: V \to V^{**}$:

$$
    \bar\omega(g) = g(\vec v) \implies \rho(\vec v) = \bar \omega
$$

The map $\rho$ is linear:

$$  
    \begin{align*}
        \rho(a \vec{u} + b \vec{v})(g) = \bar{\sigma}(g) \\
        = g(a \vec{u} + b \vec{v}) \\
        = a g(\vec{u}) + b g(\vec{v}) \\
        = a \rho(\vec{u})(g) + b \rho(\vec{v})(g) \\
    \end{align*}
$$

Since this is true for arbitrary $g$ we have $\rho(a \vec{u} + b \vec{v}) = a \rho(\vec{u}) + b \rho(\vec{v})$, proving linearity.

###  Basis
The linear functionals $\rho(e_i)$ form a basis for $V^{**}$, where $e_i$ are the basis for $V$.

#### Proof
The proof proceeds as above where we must show the following:

$$
    \sum_{i=1}^n \bar{a}_i \rho(e_i) = 0 \quad \implies \quad \bar{a_i} = 0, \forall \bar{a_i} \in \mathbb{F}
$$

We can apply the linear functional above above to any basis vector $\epsilon_k \in V^*$:

$$
    \sum_{i=1}^n \bar{a}_i \rho(e_i)(\epsilon_k) = 0
$$

$$
    \begin{align*}
        \rho(e_i)(\epsilon_k) = \epsilon_k(e_i) = \delta_{ik} \\
        \bar{a}_k \rho(e_k)(\epsilon_k) = 0 \\
        
        a_k 1  = 0 \\
        a_k = 0
    \end{align*}
$$

## Natural Isomorphism

The map $\rho$ is onto as every $\bar{\omega} \in V^{**}$ is mapped to by some vector in $V$, as we can see by the linearity of $\rho$:

$$
    \bar{\omega} = \sum_{i=1}^n \bar{a}_i \rho(e_i) =  \sum_{i=1}^n \rho(\bar{a}_i e_i) = \rho(\sum_{i=1}^n \bar{a}_i e_i) \quad \bar{a}_i \in \mathbb{F}
$$

The map $\rho$ is also one-to-one because by the definition of a basis each vector $\sum_{i=1}^n \bar{a}_i e_i$ is unique. Therefore, the map $\rho$ is an isomorphism between $V$ and $V^{**}$. Note that the relation $\bar\omega(g) = g(\vec v)$ makes no reference to a basis so we call $V \cong V^{**}$ a _natural isomorphism_; there is no ambiguity in writing $\vec{v}(g) = g(\vec v)$.