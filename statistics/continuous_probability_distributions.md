## Statistics of Continuous Probability Distributions
The theory of statistics of discrete probability distributions can be readily extended to that of _continuous_ probability distributions. Probabilities are now provided using a probability _density_ function. The normalization condition is expressed as:
$$ \int\limits_{-\infty}^\infty P(x) dx = 1 $$

### Probability Density
The probability of any single value of $x$ is zero. This may seem counter-intuitive, however, consider that since the random variable is continuous then there are an infinite number of possible values it can take. Since the total probability is spread out over an infinite number of values, each value must have an infinitely small probability.

For continuous random variables, we do not ask what is the probability of one specific value of $x$ occurring, but rather what is the probability of $x$ occuring in some interval:

$$ P(\alpha \le x \le \beta) = \int\limits_\alpha^\beta P(x) dx $$

Since the probability of any specific value occurring is zero, the following are equivalent:

$$ P(\alpha \le x \le \beta) = P(\alpha \lt x \lt \beta) = P(\alpha \le x \lt \beta) = P(\alpha \lt x \le \beta)  $$

#### Proof

$$
\begin{align}
P(X \le c) &= P((X \lt c) \cup P(X = c)) \\
           &= P(X \lt c) + P(X = c) - P((X \lt c) \cap P(X = c)) \\
           &= P(X \lt c) + 0 - 0 \\
           &= P(X \lt c) \\
\end{align}
$$