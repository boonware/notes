
### Z-Score
The z-score or standard score tells by how many standard deviations a value differs from the mean. This is useful when comparing values from different populations, each having their own parameters $\mu$ and $\sigma$, allowing the values to be compared in _standard units_.

$$
    z = \frac {{x} - \mu} {\sigma}
$$

Clearly, the standard score follows the same distribution as the measured values $x$ as it is simply rescaled via subtraction and division.

### Z-Test
When a hypothesis is about the _mean_ of a distribution we can use a z-test. The z-statistic is defined as follows, where $\mu_0$ is the population mean under the null hypothesis:
$$
    z = \frac {\overline{x} - \mu_0} { \frac {\sigma} { \sqrt n } }
$$

Fron the Central Limit Theorem we know that the sample mean $\overline{x}$ is approximately normally distributed, so the same distribution applies to the z-statistic. Note that the z-statistic in this case is essentially the same as above for the z-score; the difference between the measured value and the population mean is divided by the population standard deviation. For samples of size $n$, the standard deviation of the distribution of $\overline{x}$ is $\frac{\sigma}{\sqrt{n}}$.

#### Example
It is claimed that the mean grade for students in a university is 75. We ask, is this claim true? A random sample of grades of size 100 gives a sample mean of 73. It is known that the population standard deviation is 15.

* $H_0$ - the mean grade is 75.
* $H_A$ - the mean grade is not 75.

Calculate the z-statistic:

$$
z = \frac{73 - 75}{\frac{15}{\sqrt{100}}} = -1.33
$$

For our test we choose a significance level of 5%. Using the critical value approach:

TODO - finish
