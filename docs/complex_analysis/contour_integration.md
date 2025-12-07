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
    \int_{-\infty}^{\infty} \frac{dx}{z^2 - 1} \quad z \in \mathbb{C} 
$$
