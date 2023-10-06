## Statistics of Continuous Probability Distributions
The theory of statistics of discrete probability distributions can be readily extended to that of _continuous_ probability distributions. Probabilities are now provided using a probability _density_ function $f(x)$. The normalization condition is expressed as:
$$ \int\limits_{-\infty}^\infty f(x) dx = 1 $$

### Probability Density
The probability of any single value of $X$ is zero. This may seem counter-intuitive, however, consider that since the random variable is continuous then there are an infinite number of possible values it can take. Since the total probability is spread out over an infinite number of values, each value must have an infinitely small probability.

For continuous random variables, we do not ask what is the probability of one specific value $x$ occurring, but rather what is the probability of $x$ occuring in some interval:

$$ P(\alpha \le X \le \beta) = \int\limits_\alpha^\beta f(x) dx $$

Since the probability of any specific value occurring is zero, the following are equivalent:

$$ P(\alpha \le X \le \beta) = P(\alpha \lt X \lt \beta) = P(\alpha \le X \lt \beta) = P(\alpha \lt X \le \beta)  $$

#### Proof

$$
\begin{align}
P(X \le c) &= P((X \lt c) \cup P(X = c)) \\
           &= P(X \lt c) + P(X = c) - P((X \lt c) \cap P(X = c)) \\
           &= P(X \lt c) + 0 - 0 \\
           &= P(X \lt c) \\
\end{align}
$$

### Expected Value


$$
    E[X] = \int\limits_{-\infty}^\infty x f(x)dx
$$

### Variance

$$
    Var[X] = \int\limits_{-\infty}^\infty (x-E[X])^2 f(x)dx
$$

### Sample Mean & Variance
Since a sample from any population contains a finite number of values, the equations for sample mean and variance for a discrete random variable also apply in the continuous case.

### Cumulative Distribution Function
The CDF is given by:

$$
    CDF(\alpha) = P(X \le \alpha )  \int\limits_{-\infty}^\alpha x f(x)dx
$$

### Normal Distribution

<img alt="Graph of normal distribution" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/1920px-Standard_deviation_diagram.svg.png"/>

The most important probability distribution is the normal distribution, also known as a Gaussian distribution or bell curve due to its shape. The center is given by the mean $\mu$, and the standard deviation $\sigma$ determines how "spread out" the graph is. It is defined as follows:

$$ P(x) = \frac{1}{\sigma\sqrt{2\pi}}  e^{-\frac{1}{2}{(\frac{x-\mu}{\sigma})^2}} $$

Many phenomena in nature can be _approximated_ quite well by a normal distribution, for example, people's heights, the size of snowflakes, and IQ scores.

### Central Limit Theorem
In its basic form, the Central Limit Theorem states that for a sample of size $n$ with sample mean $\overline{x}$ and sample standard deviation $s$, where all observations are i.i.d, then the following limit approaches a normal distribution:

$$
    \lim_{n\to\infty} \frac{ \overline{x} - \mu } { s }
$$

where the sample standard deviation is given by:

$$
    s = \frac{ \sigma } { \sqrt{n} }
$$

In other words, the Central Limit Theorem tells us that given many separate samples from a population, each with many observations, the sample means will tend towards a normal distribution, provided that the sample sizes were large enough. For example, imagine sampling the height's of thousands of adults in many countries around the world. The sample means of the heights for each country would be approximately normally distributed.
