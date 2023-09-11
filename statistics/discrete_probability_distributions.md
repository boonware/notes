## Introduction

### What is Statistics?
The German word _Statistik_, itself derived from Latin, had a now obsolete meaning "description of a state". In statistics, we are concerned with _populations_, and we wish to make _summary_ statements about the state of these populations by _sampling_ when it is simply impractical, or perhaps impossible, to learn about all members of a population. In this sense, we wish to determine the value of some state of the population. For example, it is at least impractical to determine the average height of every adult human on Earth by measuring billions of people, but by taking well-chosen samples we can determine a good approximation.

### Descriptive vs. Inferential Statistics
Statistical techniques fall into two broad categories. Descriptive statistics describe or summarize data, for example mean or standard deviation. With descriptive statistics there is no uncertainty as the reported statistics simply describe the data as measured. Descriptive statistics are used for creating graphs and charts such as histograms and pie charts. With inferential statistics the goal is to infer or estimate properties of a population based on sampling. Inferential techniques include hypothesis testing.

## Statistics of Discrete Probability Distributions
We begin our study of statistics with the theory of _discrete random variables_. We denote the set of all possible values that the random variable can take as $X$. Specific values of the random variable are denoted in lower case $x$. A random variable obeys some probability distribution $P(X): \mathbb{R} \mapsto \mathbb{R}$ such that we can obtain the probability of a specific value of $X$ occurring. The probability distribution obeys the _normalization condition_:

$$ \sum_{i=1}^{n} P(x_i) = 1 $$

### Expected Value

For a discrete probability distribution $X$ with $n$ possible values, where $x_i$ is the i-th possible value and $p_i$ is the probability of that value, the expected value (or expectation) is given by

$$ \mu_X = E[X] = \sum_{i=1}^{n} x_i P(x_i) $$

Where the distribution X is clear the symbol $\mu$ may also be used. The expectated value is a weighted average. Note the usage of square brackets here to denote that this is a _functional_, i.e. a function of other functions (probability distributions); this notation is not consistent. The notation $\overline{X}$ is also used, and $\braket{X}$ is common in physics.

#### Linearity
The expected value is linear, no matter if the distributions are dependent or independent:

$$ E[X + Y] = E[X] + E[Y] $$

### Law of Large Numbers
When $n$ samples are taken from a probability distribution $X$ their average value approaches the expected value as the number of samples increases. This is an intuitive result.

$$ \lim_{n \to \infty } \sum_{i=1}^{n} \frac{X_i}{n} = E[X] $$

### Variance
The variance of a discrete random variable, written $Var[X]$ or often simply $\sigma^2$, is the expected value of the square of the difference between the variable and its expected value:

$$ \sigma^2 = Var[X] = E[(X - E[X])^2] $$


The variance quantifies the dispersion of samples from a probability distribution, that is, the weighted average (squared) spread of samples from the expected value. It can also be expressed as 

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
The square root of the variance is called the **standard deviation**:

$$
 \sigma = SD[X] = \sqrt{Var[X]}
$$

The standard deviation is expressed in the same units as the underlying variable, whereas the variance is expressed in squared units. Which is used depends on the context, however, sometimes one is mathematically more useful. For example, the expression above for $Var[X_1 + ... + X_n]$ does not apply to the standard deviation:

$$
 SD[X_1 + ... X_n] \neq SD[X_1] + ... + SD[X_n]
$$

### Population vs. Sample Values
Care must be taken when referring to statistics about an entire population (often unknown) versus samples taken from that population. More correctly, the values that refer to the entire population are  _parameters_ of the distribution. We can estimate the values of population parameters using sampling. A sample statistic is _unbiased_ if the expectation value equals the population parameter, otherwise it is known as a _biased_ statistic.

### Sample Mean
The sample mean provides an estimate of the population mean, and is an arithmetic average over the sample values:

$$
\overline{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

The expected value of the sample mean is the population mean:

$$
E[\overline{x}] = \mu 
$$

The variance of the sample mean approaches zero as the sample sizes increases, since the sample mean itself approaches the population mean:

$$
Var[\overline{x}] = \frac{\sigma^2}{n}
$$

#### Proof

$$
\begin{align*}
Var[\overline{x}] &= Var \left[ \frac{1}{n} \sum_{i=1}^{n} x_i \right] \text{xc} \\
                  &= \frac{1}{n^2} \sum_{i=1}^{n} Var[x_i]   \\
\end{align*}
$$

TODO - complete

### Sample Variance

$$
s^2 =  \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \overline{x})^2
$$

The expected value of the sample variance is the population variance:

$$
E[s^2] = \sigma^2 
$$


#### Bessel's Correction
The factor of $\frac{1}{n-1}$ in the sample variance is known as _Bessel's Correction_. Intuitively it may appear that an arithmetic average over the values should be taken, similar to the sample mean, however, this produces an underestimation, i.e. a biased statistic. 

##### Proof

First, let us show that the following produces a biased statistic:

$$
s_{b}^2 =  \frac{1}{n}\sum_{i=1}^{n} (x_i - \overline{x})^2
$$

Manipulate the expected value:

$$
\begin{align*}
    E[s_{b}^2] &= E \left[ \frac{1}{n}\sum_{i=1}^{n} (x_i^2 - 2x_i\overline{x} + \overline{x}^2) \right] \\
            &= E \left[ \frac{1}{n}\sum_{i=1}^{n} x_i^2 - 2\overline{x} \frac{1}{n}\sum_{i=1}^{n} x_i + \frac{1}{n}\sum_{i=1}^{n}\overline{x}^2 \right] \\
            &= E \left[ \frac{1}{n}\sum_{i=1}^{n} x_i^2 - 2\overline{x}^2 + \overline{x}^2 \right] \\
            &= E \left[ \frac{1}{n}\sum_{i=1}^{n} x_i^2 \right] - E[\overline{x}^2] \\
            &= \frac{1}{n}\sum_{i=1}^{n} E[x_i^2] - E[\overline{x}^2] \\
            &= \frac{1}{n} (n E[x_i^2] ) - E[\overline{x}^2] \\
            &= E[x_i^2] - E[\overline{x}^2] \\
\end{align*}
$$

The second last line holds since $x_i$ represents an observation, and all observations (it is assumed) are i.i.d. Therefore the expected value of any obversation is the same, i.e. $E[x_i] = \mu$.

From the definition of variance:

$$
\begin{align*}
    E[x_i^2] &= Var[x_i] + E[x_i]^2 \\
            &= \sigma^2 + \mu^2
\end{align*}
$$

We also know that $Var[\overline{x}] = \frac{\sigma^2}{n}$, therefore:

$$
\begin{align*}
    E[\overline{x}^2] &= Var[\overline{x}] + E[\overline{x}]^2 \\
                      &= \frac{\sigma^2}{n} + \mu^2
\end{align*}
$$

Bringing the above together:

$$
\begin{align*}
    E[s_{b}^2] &= \sigma^2 + \mu^2 - \frac{\sigma^2}{n} - \mu^2 \\
                &= \left( 1 - \frac{1}{n} \right) \sigma^2
\end{align*}
$$

The expected value of the sample variance $s_b^2$ is biased, that is, it is not equal to the population variance and must be corrected by the inverse factor on the right-hand side to obtain a non-biased result:

$$
\begin{align*}
    \sigma^2 &= \frac{n}{n-1}E[s_{b}^2]\\
             &= \left( \frac{n}{n-1} \right) \frac{1}{n}\sum_{i=1}^{n} (x_i - \overline{x})^2 \\
             &= \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline{x})^2
\end{align*}
$$