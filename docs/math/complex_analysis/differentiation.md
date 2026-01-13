### The Complex Derivative

The derivative of a complex function $f: \mathbb{C} \to \mathbb{C}$ is defined similarly to the real derivative:

$$
    \frac{df(z)}{dz} = \lim_{h \to 0} \frac{f(z + h) - f(z)}{h} \quad h \in \mathbb{C}
$$

Note that for a complex derivative to exist, this limit must exist for all directions in which $z$ can be approached in the complex plane. This is a much stricter condition then a real derivative where the limit must only exist in two directions on the real line.

### Holomorphic & Meromorphic Functions

If $f(z)$ is complex differentiable at every $z \in U$ where $U \subseteq \mathbb{C}$ then $f(z)$ is said to be **holomorphic on U**. If $f(z)$ is holomorphic except at isolated points called poles then it is said to be **meromorphic**.

### Theorem: Holomorphic Implies Analytic

One of the most fundamental results in complex analysis is that _a complex function being holomorphic implies that is analytic_.

* A complex function having a derivative at a point implies it is infinitely differentiable at that point.
* This is entirely unlike real analysis where a function being differentiable at a point does _not_ imply it is infinitely differentiable at that point.
* Since a holomorphic function is differentiable at all points in its domain, and since this implies it is _infinitely_ differentiable at all points in its domain, then this is sufficient to have a Taylor series defined at every point in its domain, i.e. the function is analytic.

#### Proof
TODO

### Cauchy-Riemann Equations
Any complex function $f: \mathbb{C} \to \mathbb{C}$ can be interpreted as a function of two real numbers $f(a, b)$ where $z = a + ib$. In general, both the real and imaginary parts of the function's output can depend on both $a$ and $b$. We can write $f(z)$ using two real-valued functions $u$ and $v$:

$$
    f(z) = u(a, b) + iv(a, b)
$$

As a simple example, consider the following:

$$
    f(z) = (1 + i)z = a - b + i(a + b)
$$

We can rewrite the definition of the derivative using $u$ and $v$. Then, since the derivative must exist approaching $z$ in all directions we can chose the real line and the imaginary line as two directions and work out the derivative for each. First, with $h \in \mathbb{R}$, we compute the derivate along the real line: 

$$
    \begin{align*}
        \frac{df(z)}{dz} = \lim_{h \to 0} \frac{u(a + h, b) + iv(a + h, b) - u(a,b) - iv(a,b)}{h} \\
        \frac{df(z)}{dz} = \frac{\partial u}{\partial a} + i \frac{\partial v}{\partial a}
    \end{align*}
$$

Then, we take the derivative along the imaginary line:

$$
    \begin{align*}
        \frac{df(z)}{dz} = \lim_{h \to 0} \frac{u(a, b + h) + iv(a, b + h) - u(a,b) - iv(a,b)}{ih} \\
        \frac{df(z)}{dz} = -i\frac{\partial u}{\partial b} + \frac{\partial v}{\partial b}
    \end{align*}
$$

$$
    \frac{\partial{u}}{\partial{a}} = \frac{\partial{v}}{\partial{b}} \quad \quad \frac{\partial{u}}{\partial{b}} = - \frac{\partial{v}}{\partial{a}}
$$

These are the Cauchy-Riemann equations which establish a necessary and sufficient condition for the function to be complex differentiable. 