## Laurent Series

$$
    f(z) = \sum_{n=-\infty}^\infty a_n(z-z_0)^n 
$$

The coefficients are given by the following integral:

$$
    a_n = \frac{1}{2 \pi i}\oint_C \frac{f(z)dz}{(z-z_0)^{n+1}} 
$$

### Comparison with Taylor Series
Taylor series are a special case of Laurent series where the coefficients of all negative-power terms are zero.