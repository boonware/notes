## Hypothesis Testing
Suppose we have a hypothesis about a population and we wish to determine if it is true or false using statistics. The scenario where it false is called the _null hypothesis_ $H_0$, and where it is true is called the _alternative hypothesis_ $H_A$. Using a hypothesis test we determine if we should accept $H_0$ or reject it, thereby accepting $H_A$. Hypothesis testing is also known as **significance testing**.

### Critical Value vs. P-Value
There are two equivalent approaches to performing a hypothesis test. In both cases, we essentially ask the same thing: "assuming $H_0$ is true, is the probability that I would observe my measured value less than or equal to $\alpha$?", where $\alpha$ is some chosen probability called the **significance level** such as 1%, 5% etc. If the answer from the test is yes, then we reject $H_0$ as it is _unlikely_ (under the chosen significance level) to obtain the measured value if $H_0$ is true.

#### Critical Value Approach
With the critical value approach it is determined whether or not the observed test statistic is more extreme than a defined critical value. We reject $H_0$ if the test statistic is more extreme than the critical value, otherwise we accept it. The critical value is selected based on two factors:
* A chosen probability $\alpha$ called the **significance level**, such as 1%, 5% etc.
* The probability distribution of the test statistic.

The critical value divides the area under the probability distribution curve into rejection region(s) and a non-rejection region.

##### Left-Tailed Test
Let $\phi(z)$ be a probability density function, $c$ the critical value and $\alpha$ the significance level:

$$
    \alpha = \int^{c}_{-\infty} \phi(z)dz
$$

For a test statistic $m$, when $m \le c$ we accept $H_A$ . In other words, with a left-tailed or left-sided test $H_0$ is rejected if the test statistic falls within the left rejection region:

![Left-Tailed Test](/statistics/img/critical-value-left.png)

##### Right-Tailed Test

$$
    \alpha = \int^{\infty}_{c} \phi(z)dz
$$

For a test statistic $m$, when $m \ge c$ we accept $H_A$ . In other words, with a right-tailed or right-sided test $H_0$ is rejected if the test statistic falls within the right rejection region:

![Right-Tailed Test](/statistics/img/critical-value-right.png)

##### Two-Tailed Test

In a two-tailed test, the total significance level is divided between two regions, i.e. the probability that the test statistic is less than or equal to a critical value $c_1$ _or_ that it's greater than or equal to a critical value $c_2$

$$
    \alpha = \int^{c_1}_{-\infty} \phi(z)dz \ + \ \int^{\infty}_{c_2} \phi(z)dz
$$

For a test statistic $m$, when $m \le c_1$ or $m \ge c_2$ we accept $H_A$ . When the probability density function is symmetric then $c_1 = - c_2$, but some distributions used in hypothesis testing are asymmetric, for example the chi-squared distribution. In other words, with a two-tailed or two-sided test $H_0$ is rejected if the test statistic falls within either of the two rejection regions, illustrated below for a symmetric distribution:

![Two-Tailed Test](/statistics/img/critical-value-two-sided.png)

#### P-Value Approach
In the p-value approach we evaluate the probability of observing a value _at least_ as extreme as the test statistic, assuming $H_0$ is true. In contrast to the critical value approach where we know the probability $\alpha$ but wish to determine the critical value in the integral limit, this time around we know the critical value and wish to determine the probability $p(z)$. The p-value is then compared against the significance level $\alpha$. For a test statistic $z$ we have:

$$
p(z) \le \alpha = \begin{cases} \text{true} \implies \text{reject $H_0$} \\
    \text{false} \implies \text{accept $H_0$} \end{cases}
$$

The smaller the p-value, the stronger the evidence against $H_0$. The p-value can be used to show the exact level of evidence for or against $H_0$ _without_ reference to a signficance level, unlike the critical value method.

#### Calculating Critical Values & P-Values
In practice, critical values and p-values are obtained using statistical software or standard tables. Calculating values under a distribution such as the normal distribution is difficult and typically solved using numerical methods.

#### Notes
Images taken from [here](https://www.geo.fu-berlin.de/en/v/soga-r/Basics-of-statistics/Hypothesis-Tests/Introduction-to-Hypothesis-Testing/Critical-Value-and-the-p-Value-Approach/index.html) under [Creative Commons Licence](https://creativecommons.org/licenses/by-sa/4.0/). No changes have been made.