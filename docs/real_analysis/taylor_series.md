## Taylor Series
If a function $f(x)$ is infinitely differentiable at a point $a$ then it can be represented as an infinite sum of derivatives at that point, known as a Taylor series or Taylor expansion:

$$
    f(x) = f(a) + \frac{f^{\prime}(a)(x-a)}{1!} + \frac{f^{\prime \prime}(a)(x-a)^2}{2!} + \frac{f^{\prime \prime \prime}(a)(x-a)^3}{3!} + \dots
$$

$$
    f(x) = \sum^\infty_{n=0} \frac{f^{(n)}(a)(x-a)^n}{n!}
$$

### Proof
Applying the Fundamental Theorem of Calculus, we can express a function $f(x)$ as, loosely, the value of the function at point $a$ _plus_ all of the changes in the function from $a$ to $x$. Concretely:

$$
    f(x) = f(a) + \int_a^x f^\prime(t_1)dt_1
$$

We can repeat the process for the integral above since the integral is itself a function. Although $a$ appears in the integration limits we can still choose to evaluate the function at $a$ also, there being no restriction on which point we choose:

$$
    \int_a^x f^\prime(t_1)dt_1 = \int_a^x f^\prime(a)dt_1 + \int_a^x \int_a^{t_1} f^{\prime \prime}(t_2)dt_2dt_1
$$

$$
    f(x) = f(a) + \int_a^x f^\prime(a)dt_1 + \int_a^x \int_a^{t_1} f^{\prime \prime}(t_2)dt_2dt_1
$$

We can repeat again for the double integral above:

$$
    \int_a^x \int_a^{t_1} f^{\prime \prime}(t_2)dt_2dt_1 = \int_a^x \int_a^{t_1} f^{\prime \prime}(a)dt_2dt_1 + \int_a^x \int_a^{t_1} \int_a^{t_2} f^{\prime \prime \prime}(t_3)dt_3 dt_2 dt_1
$$

$$
    f(x) = f(a) + \int_a^x f^\prime(a)dt_1 + \int_a^x \int_a^{t_1} f^{\prime \prime}(a)dt_2dt_1 + \int_a^x \int_a^{t_1} \int_a^{t_2} f^{\prime \prime \prime}(t_3)dt_3 dt_2 dt_1
$$

The integrals can be further simplified as follows:

$$
    \int_a^x f^{\prime}(a)dt_1 = f^{\prime}(a) \int_a^x dt_1 = f^{\prime}(a) (x-a)
$$

$$
    \int_a^x \int_a^{t_1} f^{\prime \prime}(a)dt_2dt_1 = f^{\prime \prime}(a) \int_a^x \int_a^{t_1} dt_2dt_1 = f^{\prime \prime}(a) \int_a^{x} (t_1 - a) dt_1 = f^{\prime \prime}(a) \frac{(x - a)^2}{2}
$$

$$
    \int_a^x \int_a^{t_1} \int_a^{t_2} f^{\prime \prime \prime}(t_3)dt_3 dt_2 dt_1 = \ldots = f^{\prime \prime \prime}(a) \frac{(x-a)^3}{3 \times 2}
$$

We see that in general we have:

$$
    \int_a^x \int_a^{t_1} \ldots \int_a^{t_{n-1}} f^{(n)}(t_n)dt_n \ldots dt_1 = f^{(n)}(a) \frac{(x-a)^n}{n!}
$$


## Maclaurin Series

A Taylor series with $a=0$ is known as a **Maclaurin series**. Some common Maclaurin series:

$$
    \cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^{n} x^{2n}}{2n!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots
$$

$$
    \sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots
$$