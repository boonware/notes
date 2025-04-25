
## Pearson's Chi-Squared Test

Pearson's chi-squared test, also written $\chi^2$, is one of a number of statistical tests that use the $\chi^2$ distribution. This test is applied to sets of _categorical data_, i.e. variables which can take only a limited and fixed number of values. The test evaluates how likely it is that any observed difference between the sets of data arose due to chance.

The $\chi^2$ statistic is defined as follows, where $O_i$ and $E_i$ are the $i$-th observed and expected values of the categorical variable, respectively:

$$
    \chi^2 = \sum^n_{i=1} \frac{(O_i - E_i)^2}{E_i}
$$

There are three kinds of comparison in Pearson's $\chi^2$ test, each of which is explained below.

### Size Requirement

The expected frequency of each value of the categorical variable must be $\ge 5$. While not exact, this is a rule of thumb to help ensure the distribution of the test statistic adequately matches a $\chi^2$ distribution.

### Type 1 - Goodness of Fit



In this test the aim is to determine if the observed _frequency_ of the  values of the categorical variable differ from the expected frequency in a statistically significant manner, or if the difference is down to chance. 

The number of degrees of freedom is given below, where $k$ is the number of categories of the random variable:

$$
    df = k - 1
$$

#### Example
Suppose that the national average percentages of commuters that use each mode of transport to commute was collected by a census and is known. We want to determine if a particular city follows this national average. We perform a random sample of commuters in the city with sample size $n=1000.$ The data are shown in the table below.

| Category | Observed % | Expected % | Observed Count | Expected Count |
| - | - | - | -| - |
| Car | 0.75 | 0.76 | 750 | 760 |
| Motorcycle | 0.11 | 0.10 | 110 | 100 |
| Bicycle | 0.03 | 0.05 | 30 | 50 |
| Walking | 0.03 | 0.03 |  30 | 30 |
| Bus | 0.06 | 0.02 | 60 | 20 |
| Tram | 0.02 | 0.04 | 20 | 40 |

The hypotheses for our test are as follows:

* $H_0$ - the city follows the national average, i.e. the values in the "expected" column.
* $H_A$ - the city does not follow the national average.

Compute the test statistic:

$$
    \chi^2 = 0.13 + 1 + 8 + 0 + 80 + 10 = 99.13
$$

Using a standard table we finding the critical value by looking up the row that corresponds to the degrees of freedom $df = 5$ and the column for our chosen significance level $\alpha = 5$%. The critical value is 11.07. We reject $H_0$ because $99.13 > 11.07$. In other words, it is statistically unlikely that we would measure the observed values that we did _and_ that the population, i.e. the commuters of the city, would use modes of transport that follow the national average. We conclude that the city's commuters do _not_ follow the national average.


### Type 2 - Independence
In this test the aim is to determine if two categorical variables are related, that is, if the value of either one of the variables depends on the value of the other.

### Type 3 - Homogeneity
TODO