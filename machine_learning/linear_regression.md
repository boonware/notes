## Linear Regression of a Single Variable
Linear regression is an example of supervised learning. In a regression problem, we aim to predict a real-valued output. By comparison, when the output is discrete-valued we use a classification algorithm. In linear regression, we establish a hypothesis function $h_\theta(x)$ which maps input $x$ to output $y$. This is of course the equation of a straight line:

$$
    h_\theta(x) = \theta_0 + \theta_1 x \quad \text{where} \quad x, h(x), \theta_0, \theta_1 \in \real
$$

### Cost Function
The hypothese function $h(x)$ depends on constants $\theta_0$ and $\theta_1$, but how do we choose the values for these constants? A good choice is that where the difference between $h_\theta(x)$ and the actual $y$ value is minimized for all $n$ training data points $(x, y)$. We can define a cost function which expresses this difference:

$$
    J(\theta_0, \theta_1) = \frac{1}{2n} \sum^n_{i=1} \left( h_\theta(x_i) - y_i  \right)^2
$$

This cost function is the mean squared error. The square ensures only positive values for the cost. The factor of $1/2$ simplifies calculates when taking the derivative to minimize the cost function.

### Gradient Descent
The cost function can be minimized using the gradient descent algorithm.

1. Start with some initial $(\theta_0, \theta_1)$, for example $(\theta_0 = 0, \theta_1 = 1)$.
2. Change $(\theta_0, \theta_1)$ to reduce the cost function $J(\theta_0, \theta_1)$.
3. Repeat step 2 until (hopefully) a minimum is reached.

$$
    \theta_j := \theta_j - \alpha \frac{\partial{J(\theta_0, \theta_1)}}{\partial{\theta_j}} \quad \text{where} \quad j \in \{0, 1\}
$$