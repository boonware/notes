## Linear Regression of a Single Variable
Linear regression is an example of supervised learning. In a regression problem, we aim to predict a real-valued output. By comparison, when the output is discrete-valued we use a classification algorithm. In linear regression, we establish a hypothesis function $h_\theta(x)$ which maps input $x$ to output $y$:

$$
    h_\theta(x) = \theta_0 + \theta_1 x \quad \text{where} \quad x, h_\theta(x), \theta_0, \theta_1 \in \mathbb{R}
$$

The $x$ value is called a "feature". This hypothesis function is the equation of a straight line:

![Fitting a line to data points](/machine_learning/img/linear_regression.png)

### Cost Function
The hypothesis function $h(x)$ depends on constants $\theta_0$ and $\theta_1$, but how do we choose the values for these constants? A good choice is that where the difference between $h_\theta(x)$ and the actual $y$ value is minimized for all $n$ training data points $(x, y)$. We can define a cost function which expresses this difference:

$$
    J(\theta_0, \theta_1) = \frac{1}{n} \sum^n_{i=1} \left( h_\theta(x_i) - y_i  \right)^2
$$

This cost function is the mean squared error. The square ensures only positive values for the cost. Note: some definitions include a factor of $1/2$ to simplify calculations with the derivative.

### Normal Equation

$$
    X\theta = y
$$


$$
\begin{align*}
       \frac{\partial}{\partial \theta} \left( X \theta - y  \right)^T \left( X \theta - y  \right) &= 0 \\
        2X^T(X \theta - y) &= 0 \\
         \theta &= \left( X^TX \right)^{-1} X^T y
\end{align*}

$$

### Gradient Descent
The cost function can be minimized using the gradient descent algorithm. This is also known as "batch" gradient descent, where all training examples are used to calculate the gradient on each iteration.

1. Start with some initial $(\theta_0, \theta_1)$, for example $(\theta_0 = 0, \theta_1 = 1)$.
2. Change $(\theta_0, \theta_1)$ to reduce the cost function $J(\theta_0, \theta_1)$. By considering the cost function as a vector-valued function, this is achieved by subtracting a step in the direction of the gradient of the cost function. The gradient represents the direction of most rapid change in the function. A step size $\alpha$ must be selected.

$$
    \vec{J}(\theta_0, \theta_1) := \vec{J}(\theta_0, \theta_1) - \alpha \nabla \vec{J}(\theta_0, \theta_1) \quad \text{where} \quad \alpha \in \mathbb{R}^+
$$


3. Repeat step 2 until a minimum is reached. If $\alpha$ is too large the algorithm may overshoot the minimum and oscillate forever. Likewise, if $\alpha$ is too small the algorithm may take far too long to converge. In general, convergence to a global minimum is not guaranteed unless the cost function is convex; the definition of $J(\theta_0, \theta_1)$ given above is convex.

### Stochastic Gradient Descent
A variation of the gradient descent algorithm uses a random sample of the training data to estimate the gradient. This can be useful when training on vast data sets such as with neural networks, where batch descent algorithm may perform too slowly.

## Linear Regression of Multiple Variables
In the case where the output variable depends on multiple features, we can write the hypothesis function as follows:

$$
    h_\theta(x) = \theta_0 + \theta_1 x_1 + ... + \theta_n x_n\quad \text{where} \quad x_n, h_\theta(x), \theta_n \in \mathbb{R}
$$

Using matrix notation, we can write $\theta$ and $x$ as column vectors:
$$
    h_\theta(x) = \vec{\theta} \cdot \vec{x} = \theta^Tx
$$

The same cost function applies in the multi-variable case, where now the input is $\vec{\theta}$.

## Polynomial Regression

$$
    h_\theta(x) = \sum^n_{i=0} \theta_ix^i
$$

## Notes
* Linear regression image taken from [here](https://commons.wikimedia.org/wiki/File:Linear_least_squares_example2.svg) under [Creative Commons Licence](https://creativecommons.org/licenses/by-sa/3.0/). No changes have been made.