## Green's Functions

### Definition

Consider the following equation where a **known** linear operator $L$ acts on an **unknown** function $\psi(x)$ to produce a **known** function $f(x)$:
$$
    L \psi(x) = f(x)
$$

How can we find $\psi(x)$? We introduce a function $G(x, x^{\prime})$ known as a **Green's function** defined as

$$
    LG(x, x^{\prime}) = \delta(x-x^{\prime})
$$

where $\delta(x-x^{\prime})$ is the Dirac delta function. Multiplying the above by $f(x^{\prime})$ and integrating over $x^{\prime}$, we have

$$
    \int LG(x, x^{\prime}) f(x^{\prime}) dx^{\prime} = \int \delta(x-x^{\prime}) f(x^{\prime}) dx^{\prime}
$$

By the definition of the Dirac delta function and since $L$ does not depend on $x^{\prime}$, we get

$$
    L \int G(x, x^{\prime}) f(x^{\prime}) dx^{\prime} = f(x)
$$

By comparison with the original equation:

$$
    \psi(x) = \int G(x, x^{\prime}) f(x^{\prime}) dx^{\prime}
$$
