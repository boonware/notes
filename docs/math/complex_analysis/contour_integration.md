## Contour Integration
For integrals that cannot be evaulated along the real line, for example due to the presence of a zero denominator, the method of contour integration in the complex plane may be used. Consider the integral below:

$$
    \int_{-\infty}^{\infty} \frac{dx}{x^2 - 1} \quad x \in \mathbb{R} 
$$

This integral has poles at $x = \pm 1$, i.e. it cannot be computed at these points as the denominator is zero. Let us perform a procedure called **analytic continuation** whereby we extend the integrand to be a function over the complex numbers:

$$
    x \rightarrow x + i \eta = z
$$

$$
    \int_{-\infty}^{\infty} \frac{dz}{z^2 - 1} \quad z \in \mathbb{C} 
$$

TODO

### Cauchy's Integral Theorem

If $C$ is a simple closed curve on the complex plane $z$ and $f(z)$ is a function holomorphic on and in $C$ then

$$
    \oint_C f(z) dz = 0
$$

#### Proof
TODO



#### Existence of Poles
If $f(z)$ contains singular points (poles) within $C$ then the integral does not necessarily vanish. This agrees with the definition as the function is no longer holomorphic within $C$, i.e. the derivative is not defined at the pole. Consider the following example where $C$ is a circle of radius $r$ centered on $z_0$. A pole exists at $z = z_0$ where the denominator becomes zero:

$$
    \oint_C \frac{dz}{(z-z_0)^n}
$$

Given the definition of $C$ we can express $z$ in polar form:

$$  
    \begin{align*}
        z = z_0 + re^{i\theta} \\
        dz = ire^{i\theta} d\theta
    \end{align*}
$$

$$
    \oint_C \frac{dz}{(z-z_0)^n} =  \oint_0^{2\pi} \frac{ire^{i\theta} d\theta}{(re^{i\theta})^n} = i r^{1-n} \oint_0^{2\pi} e^{i(1-n)\theta} d\theta
$$

$$
    i r^{1-n} \oint_0^{2\pi} e^{i(1-n)\theta} d\theta = \frac{r^{1-n}}{1-n} e^{i(1-n)\theta} \big|_0^{2\pi} = \frac{r^{1-n}}{1-n} e^{i(1-n)\theta} \big|_0^{2\pi}
$$