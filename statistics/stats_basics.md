## Fundamentals

### What is Statistics?
The German word _Statistik_, itself derived from Latin, had a now obsolete meaning "description of a state". In statistics, we are concerned with _populations_, and we wish to make _summary_ statements about these populations by _sampling_ when it is simply impractical, or perhaps impossible, to learn about all members of a population. In this sense, we wish to determine the value of some state of the population. For example, it is at least impractical to determine the average height of every adult human on Earth by measuring billions of people, but by taking well-chosen samples we can determine a good approximation.

### Inferential vs. Descriptive Statistics
TODO

### Expected Value

For a discrete probability distribution $X$ with $n$ possible values, where $x_i$ is the i-th possible value and $p_i$ is the probability of that value, the expected value is given by

$$ E[X] = \sum_{i=1}^{n} x_i p_i $$

TODO weighted average similarity

Note the usage of square brackets here to denote that this is a _functional_, i.e. a function of other functions (probability distributions); this notation is not consistent. The notation $\overline{X}$ is also used, and $\braket{X}$ is common in physics.

### Law of Large Numbers

$$ \lim_{n \to \infty } \sum_{i=1}^{n} \frac{X_i}{n} = E[X] $$

### Variance
The variance of a discrete random variable is the expected value of the square of the difference between the variable and its expected value:

$$ Var[X] = E[(X - E[X])^2] $$


The variance quantifies the disperson of samples from a probability distribution, that is, the weighted average (squared) spread of samples from the expected value. It can also be expressed as 

$$ Var[X] = E[X^2] - E[X]^2 $$

##### Derivation
$$ 
\begin{align*}
E[(X - E[X])^2] &= \sum_{i=1}^{n} (x_i - \sum_{k=1}^{n} x_k p_k )^2 p_i \\
                &= \sum_{i=1}^{n} (x_i^2 - 2 x_i \sum_{k=1}^{n} x_k p_k + (\sum_{k=1}^{n} x_k p_k)^2) p_i \\
                &= \sum_{i=1}^{n} x_i^2 p_i- 2 \sum_{i=1}^{n} x_i p_i \sum_{k=1}^{n} x_k p_k + \sum_{i=1}^{n} p_i(\sum_{k=1}^{n} x_k p_k)^2 \\
                &= E[X^2]- 2 E[X]^2 + (1)E[X^2] \\
                &= E[X^2]- E[X]^2 \\
\end{align*}
$$


###

#### Why the Squared Difference?
The squared difference ensures that the value for all samples is always positive or zero, but the absolute value $ |X - E[X]| $ could also provide this property. There are a number of reasons why the squared difference is used:

* The squared difference is continuously differentiable (it exists and is itself continuous), whereas the absolute value's derivate is not continuous, it is undefined at $ x = 0 $ . This is useful when trying to optimize the variance.
* If $ X_n $ are independent discrete random variables then the following is true for the squared difference, unlike the absolute value:

$$
Var[X_1 + ... + X_n] = Var[X_1] + ... + Var[X_n]
$$



### Standard Deviation
The square root of the variance is called the **standard deviation**.
