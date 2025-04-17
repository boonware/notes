
## Pearson's Chi-Squared Test

Pearson's chi-squared test, also written $\chi^2$, is one of a number of statistical tests that use the $\chi^2$ distribution. This test is applied to sets of _categorical data_, i.e. variables which can take only a limited and fixed number of values. The test evaluates how likely it is that any observed difference between the sets of data arose due to chance.

There are three kinds of comparison in Pearson's $\chi^2$ test, each of which is explained below.

### Type 1 - Goodness of Fit

 Work in progress

In this test the aim is to determine if the observed _frequency_ of the  values of the categorical variable differ from the expected frequency in a statistically significant manner, or if the difference is down to chance. The $\chi^2$ statistic is defined as follows, where $O_i$ and $E_i$ are the $i$-th observed and expected values of the categorical variable, respectively:

$$
    \chi^2 = \sum^n_{i=1} \frac{(O_i - E_i)^2}{E_i}
$$

#### Example
Suppose that the national average percentages of commuters that use each mode of transport to commute was collected by a census and is known. We want to determine if a particular city follows this national average. We perform a random sample of commuters in the city.

| Category | Observed | Expected |
| - | - | - |
| Car | 0 | 0.76 |
| Motorcycle | | 0.10 | 
| Bicycle | | 0.05 |
| Walking | | 0.03 | 
| Bus | | 0.02 |
| Tram |  | 0.04 |

* $H_0$ - the city follows the national average, i.e. the values in the "expected" column.
 * $H_A$ - the city does not follow the national average.




### Type 2 - Independence
TODO

### Type 3 - Homogeneity
TODO