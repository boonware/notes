
## Student's T-Test

### One-Sample Test
When performing a z-test the population standard deviation must be known. The point of a z-test is to test if the population's hypothesized mean is correct. It is unlikely that one would know the population standard deviation $\sigma$ but not know the population mean. To solve this problem we can use a **t-test**, where we instead use the _sample standard deviation_ $s$ as an estimate of $\sigma$:

$$
   t = \frac {\overline{x} - \mu_0} { s / \sqrt n  }
$$

The t-test is in a sense the "best we can do" without knowing the population standard deviation.

### Degrees of Freedom
Consider choosing three numbers such that their mean is 9. If you choose 3 and 3, then the third number must also be 3. Similarly, if you choose 1 and 6 then the third number must be 2. We see that for $n$ numbers we can only freely choose $n-1$; once these are chosen the final number is fixed. The number of freely varying parameters is called the _degrees of freedom_.

### T-Distribution
The t-statistic follows the t-distribution whose probability density function is given by the following, where $\Gamma$ is the gamma function:

$$
   f(t|\nu) = \frac{ \Gamma( \frac{\nu + 1}{2}) }{ \sqrt{\nu \pi} \Gamma( \frac{\nu}{2} ) } \left(1 + \frac{t^2}{\nu} \right)^{-( \frac{ \nu + 1}{2} ) }
$$

The probability density function converges to the standard normal distribution as the degrees of freedom $\nu$ increases:

![Left-Tailed Test](/statistics/img/t-distribution.png)