## Binomial Distribution

TODO - add diagram

### Definition
Consider a random experiment where each outcome can have one of two possible values: success with probability $p$ or failure with probability $1-p$. These events or trials are known as **Bernoulli Trials**. Each trial is independent of the others as the probability remains the same. An example of a Bernoulli Trial is tossing a coin to check for heads vs. tails.

The discrete probability distribution of obtaining exactly $k$ successes from $n$ Bernoulli Trials is given by the **binomial distribution**:

$$ P(k, n, p) = {n \choose k} p^k (1-p)^{n-k} $$

where the _binomial coefficient_ (often read as "$n$ choose $k$") is

$$ {n \choose k} = \frac{n!}{k!(n-k)!} $$

The binomial distribution is a _probability mass function_ as it gives the probability that a discrete random variable is exactly equal to some value.

For $n$ trials each with probability $p$ the mean is clearly given by

$$\mu = np$$

