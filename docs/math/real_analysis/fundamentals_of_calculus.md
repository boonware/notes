## Fundamentals of Calculus

### Riemann Integration

$$
    \begin{align*}
        \int_a^b f(x) = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^\star)\Delta x_k \\ \Delta x_k = x_k - x_{k-1}, \ x_k^\star \in \Delta x_k \\
        x_0 = a, x_n = b \\
    \end{align*}
$$

The integral of a function is also known as its anti-derivative. The definition above may be extended naturally to functions of multiple variables.

### Fundamental Theorem of Calculus, Part 1

Let $f(x)$ be a continuous function on $[a,b]$ and $F(x)$ be its anti-derivative, then
$$
    \int_a^b f(x)dx = F(b) - F(a)
$$

### Fundamental Theorem of Calculus, Part 2

$$
    F(x) = \int_a^x f(t)dt
$$

Then we see that differentiation and integration are inverse operations:

$$
    \frac{d}{dx} \left( \int_a^x f(t) dt \right) = f(x)
$$

### Mean Value Theorem

$$
    f'(c) = \frac{f(b) - f(a)}{b - a}
$$

### Integration by Parts

$$
    \int_a^b u(x)v^{\prime}(x)dx = \bigg[ u(x)v(x) \bigg]_a^b - \int_a^b v(x) u^{\prime}(x)dx
$$

#### Proof

Using the chain rule:
$$
    \begin{align*}
        & \frac{d}{dt} \bigg( u(x) v(x) \bigg) = \frac{d(u(x))}{dx}v(x) + \frac{d(v(x))}{dx}u(x) \\
       & \frac{d(v(x))}{dx}u(x) = \frac{d}{dx} \bigg( u(x) v(x) \bigg) - \frac{d(u(x))}{dx}v(x) \\
       & \int_a^b \frac{d(v(x))}{dx}u(x) dx = \int_a^b \frac{d}{dt} \bigg( u(x) v(x) \bigg) dx - \int_a^b \frac{d(u(x))}{dx}v(x) dx \\
        & \int_a^b d(v(x))u(x) = \int_a^b d\bigg( u(x) v(x) \bigg) - \int_a^b d(u(x))v(x) \\
    \end{align*}
$$