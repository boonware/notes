## Fundamentals

### What is Statistics?
The German word _Statistik_, itself derived from Latin, had a now obsolete meaning "description of a state". In statistics, we are concerned with _populations_, and we wish to make _summary_ statements about the state of these populations by _sampling_ when it is simply impractical, or perhaps impossible, to learn about all members of a population. In this sense, we wish to determine the value of some state of the population. For example, it is at least impractical to determine the average height of every adult human on Earth by measuring billions of people, but by taking well-chosen samples we can determine a good approximation.

### Descriptive vs. Inferential Statistics
Statistical techniques fall into two broad categories. Descriptive statistics describe or summarize data, for example mean or standard deviation. With descriptive statistics there is no uncertainty as the reported statistics simply describe the data as measured. Descriptive statistics are used for creating graphs and charts such as histograms and pie charts. With inferential statistics the goal is to infer or estimate properties of a population based on sampling. Inferential techniques include hypothesis testing.

### Expected Value

For a discrete probability distribution $X$ with $n$ possible values, where $x_i$ is the i-th possible value and $p_i$ is the probability of that value, the expected value (or expectation) is given by

$$ \mu_X = E[X] = \sum_{i=1}^{n} x_i p_i $$

Where the distribution X is clear the symbol $\mu$ may also be used. The expectated value is a weighted average. Note the usage of square brackets here to denote that this is a _functional_, i.e. a function of other functions (probability distributions); this notation is not consistent. The notation $\overline{X}$ is also used, and $\braket{X}$ is common in physics.

#### Properties
The expected value is linear, no matter if the distributions are dependent or independent:

$$ E[X + Y] = E[X] + E[Y] $$

It is also trivial to show that it is idempotent:

$$ E[E[X]] = E[X] $$

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
Care must be taken when referring to statistics about an entire population (often unknown) versus samples taken from that population. More correctly, the values that refer to the entire population are  _parameters_ of the distribution. The expected value $E[X]$, a parameter as it is a property of the population, is often refered to as the mean $\mu_X$ or $\mu$ where the distribution $X$ is obvious. We cannot calculate this value for a sample

### Sample Mean

$$

\overline{x} = \frac{1}{n}\sum_{i=1}^{n} x_i

$$


The expected value of the sample mean is the population mean. In other words, if multiple independent samples are drawn from the population, the mean of the sample means will tend towards the mean of the population.

### Sample Variance

$$

s^2 =  \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \overline{x})^2

$$

The expected value of the sample variance is the population variance.


### Statistical Bias
A sample statistic is unbiased if the expectation value equals the population parameter. This is true for both the sample mean and sample variance given above:

$$

E[\overline{x}] = \mu 

$$

$$

E[s^2] = \sigma^2 

$$


### Bessel's Correction
The factor of $\frac{1}{1-n}$ above is known as _Bessel's Correction_. Intuitively it may seem like $\frac{1}{n}$ should be used, however, this produces an underestimation, i.e. a biased statistic. 

#### Proof

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

TODO to finish

