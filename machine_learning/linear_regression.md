## Linear Regression of a Single Variable
Linear regression is an example of supervised learning. In a regression problem, we aim to predict a real-valued output. By comparison, when the output is discrete-valued we use a classification algorithm. In linear regression, we establish a hypothesis function $h_\theta(x)$ which maps input $x$ to output $y$. This is of course the equation of a straight line:

$$
    h_\theta(x) = \theta_0 + \theta_1 x \quad \text{where} \quad x, h(x), \theta_0, \theta_1 \in \real
$$

### Cost Function
The hypothese function $h(x)$ depends on constants $\theta_0$ and $\theta_1$, but how do we choose the values for these constants? A good choice is that where the difference between $h_\theta(x)$ and the actual $y$ value is minimized for all $n$ training data points $(x, y)$. We can define a cost function which expresses this difference:

$$
    J(\theta_0, \theta_1) = \frac{1}{n} \sum^n_{i=1} \left( h_\theta(x_i) - y_i  \right)^2
$$

This cost function is the mean squared error. The square ensures only positive values for the cost. Note: some definitions include a factor of $1/2$ to simplify calculations with the derivative.

### Gradient Descent
The cost function can be minimized using the gradient descent algorithm.

1. Start with some initial $(\theta_0, \theta_1)$, for example $(\theta_0 = 0, \theta_1 = 1)$.
2. Change $(\theta_0, \theta_1)$ to reduce the cost function $J(\theta_0, \theta_1)$. This is achieved by subtracting a step in the direction of the gradient of the cost function. The gradient represents the direction of most rapid change in the function. A step size $\alpha$ must be selected.

$$
    \vec{J}(\theta_0, \theta_1) := \vec{J}(\theta_0, \theta_1) - \alpha \nabla \vec{J}(\theta_0, \theta_1) \quad \text{where} \quad \alpha \in \real^+
$$


3. Repeat step 2 until a minimum is reached. If $\alpha$ is too large the algorithm may overshoot the minimum and oscillate forever. Likewise, if $\alpha$ is too small the algorithm may take far too long to converge. In general, convergence to a global minimum is not guaranteed unless the cost function is convex; the definition of $J(\theta_0, \theta_1)$ given above is convex.

### Stochastic Gradient Descent
A variation of the gradient descent algorithm uses a random sample of the training data to estimate the gradient. This can be useful when training on vast data sets such as with neural networks, where the regular gradient descent algorithm may perform too slowly.
