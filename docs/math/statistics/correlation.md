## Correlation

### Pearson Covariance

We can measure how strongly two variables "co-vary" together in both magnitude and direction. The covariance of two variables $X$ and $Y$, where $E(z)$ is the expected value of a variable $z$, is defined as follows:

$$
    cov(X, Y) = E[(X - E(X))(Y - E(Y))] = E(XY) - E(X)E(Y)
$$

A normalized version that makes use of the standard deviations $\sigma(X)$ and $\sigma(Y)$ can be defined, the **correlation coefficient**:

$$
    \rho(X, Y) = \frac{cov(X, Y)}{\sigma(X)\sigma(Y)}
$$

Whereas the covariance ranges from $-\infty$ to $+\infty$ and as such can be difficult to interpret, the correlation coefficient ranges between $-1$ and $+1$.