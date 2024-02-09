## Maximum Likelihood Estimation
Suppose there is a random sample $X_1, ... , X_n$ whose probability distribution depends on some unknown parameter $\theta$. The method of Maximum Likelihood enables us to find a point estimator for the parameter. A point estimator is so-called because it estimates the value of the parameter by selecting a specific value out of the parameter space $\Theta$, that is, the space of all possible values for that parameter. As an example, if a random sample was taken from a distribution assumed to be normal then the goal would be to find a point estimator for the mean $\mu$. 

It seems reasonable that a good estimate of the parameter $\theta$ would be that value which maximizes the probability of observing those values which were observed. For a random sample, where the probability mass or density function is $f(x ; \theta)$, the joint probability is given by

$$
    L(\theta) = P(X_1 = x_1, ... , X_n = x_n) = \prod_{i=1}^{n} f(x_i ; \theta)
$$

The point estimate for $\theta$ from the set $\Theta$ of possible values is given by

$$
    \hat{\theta} = \underset{\theta \in \Theta}\argmax L(\theta)
$$

The point estimate can be found by differentiating the likelihood function $L(\theta)$ to find a maximum:

$$
    \frac{\partial L(\theta)}{\partial \theta} = 0 \quad \quad \frac{\partial^2 L(\theta)}{\partial \theta^2} < 0
$$
