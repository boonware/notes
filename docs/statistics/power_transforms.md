## Power Transforms
Many statistical methods assume that the data on which they operate is normally distributed. Data that is non-normal, for example highly skewed data, may be difficult to analyse, and applying many standard methods will fail. By applying a transform to the data, the statistical methods that assume normality can now be used.

### Box-Cox Transform
By defining the variable $w = (y^{\lambda} - 1)/\lambda$ we obtain a useful transform of the variable $y$. When $\lambda = 1$ the transform is a simple linear transformation, meaning our data is already normally distributed. Other values of $\lambda$ can be chosen, depending on the distribution of the data. When $\lambda = 0$ the transform as defined above is indetermine, however we can find the transform for this case using L'Hôpital's Rule, taking the derivative with respect to $\lambda$:

$$
    \lim_{\lambda \to 0} w(\lambda) = \frac{ \lim_{\lambda \to 0} (y^{\lambda} - 1) }{ \lim_{\lambda \to 0} \lambda } = \frac{ \lim_{\lambda \to 0} (y^{\lambda} - 1)^\prime }{ \lim_{\lambda \to 0} \lambda^\prime } = \frac{ \lim_{\lambda \to 0} y^\lambda \ln(y) }{ \lim_{\lambda \to 0} 1 } = \ln(y)
$$

The general formulation for the Box-Cox transform is therefore given by:

$$
    w(\lambda) = \begin{cases} \ln(y) \quad \text{if} \quad \lambda = 0 \\
    (y^{\lambda} - 1)/\lambda \quad if \quad \lambda \ne 0 \end{cases}
$$

The parameter $\lambda$ is chosen so as to provide the best fit to a normal distribution. Typically, many values of $\lambda$ may be tested until the one that results in a best-fit to a normal distribution is found. Lambda is chosen using variety of methods including:

* Maximum Likehood
* Goodness of Fit tests

### Yeo-Johnson Transform
TODO
