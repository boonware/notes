## Normal Distribution

<img alt="Graph of normal distribution" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/1920px-Standard_deviation_diagram.svg.png"/>

TODO big X and small x

### Definition
The _normal distribution_ for a continuous random variable $x$ is defined as

$$ P(x) = \frac{1}{\sigma\sqrt{2\pi}}  e^{-\frac{1}{2}{(\frac{x-\mu}{\sigma})^2}} $$

The center is given by the mean $\mu$, and the standard deviation $\sigma$ determines how "spread out" the graph is. It is also known as a Gaussian distribution, or bell curve due to its shape.

### Probability Density
This is a _probability density function_. The density of matter is defined as  mass per unit volume, for example the density of iron at room temperature is 7.874 grams per cubic centimeter. Similarly, a probability density function tells us the probability per unit $x$. This all becomes clearer when we consider how to use $P(x)$ to calculate probablities. For example, what is the probability of TODO

TODO - de morgans laws below??? 

TODO - why value of P(X) is zero for a single point

$$ P(\alpha \le x \le \beta) = \int\limits_\alpha^\beta P(x) dx $$

$$ P(\alpha \le x \le \beta) = P(\alpha \lt x \lt \beta) $$

$$
\begin{align}
P(X \le c) &= P((X \lt c) \cup P(X = c)) \\
           &= P(X \lt c) + P(X = c) - P((X \lt c) \cap P(X = c)) \\
           &= P(X \lt c) + 0 - 0 \\
           &= P(X \lt c) \\
\end{align}
$$

### Normalization
As the total probability over all possible values of $x$ must be 1, we have the following _normalization_:
$$ \int\limits_{-\infty}^\infty P(x) dx = 1 $$