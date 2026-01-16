## Euler-Lagrange Equation

Let $J: C^\infty(\mathbb{R{}}) \to \mathbb{R{}}$ be a functional of $q(t)$, $q^{\prime}(t)$ and $t$ of the form:

$$
    J[q(t)] = \int_{t_1}^{t_2} L[q(t), q^{\prime}(t), t] dt \quad t \in \mathbb{R{}}
$$

Note that $L: C^\infty(\mathbb{R}) \times C^\infty(\mathbb{R}) \times \mathbb{R} \to \mathbb{R{}}$ is obviously also a functional. Functionals in this integral form arise in many important contexts, for example, in the study of the motion of objects in classical mechanics, where we wish to find the particular function $q(t)$ that minimizes $J$. We will study the case where the functional depends only on $q(t)$ and its first derivative $q^{\prime}(t)$; in general, the functional may also depend explicitly on $t$. We will see that the method developed below will generalize easily to functionals that depend on higher derivaties also.

### Variation
Suppose we _vary_ $q(t)$ by making a small change, where $0 < \epsilon \ll1$:

$$
    q(t) \to q(t) + \delta q(t) = q(t) + \epsilon\eta(t) 
$$

The corresponding change in $J$ is given by:

$$
    \Delta J = \int_{t_1}^{t_2} \left(L[q(t) + \epsilon \eta(t), q^{\prime}(t) + \epsilon \eta ^{\prime}(t), t] - L[q(t), q^{\prime}(t), t] \right) dt
$$


Let us expand $L$ as a Taylor series, where $O(\epsilon^2)$ represents the terms of order $\epsilon^2$ and higher.

$$
   L[q(t) + \epsilon \eta(t), q^{\prime}(t) + \epsilon \eta ^{\prime}(t), t] = L[q(t), q^{\prime}(t), t] + \epsilon \eta(t) \frac{\partial L}{\partial q(t)} + \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} + O(\epsilon^2)
$$

The integral can then be expressed as follows:

$$
    \begin{align*}
    \Delta J &= \int_{t_1}^{t_2} \left(\epsilon \eta(t) \frac{\partial L}{\partial q(t)} + \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} + O(\epsilon^2) \right) dt \\
   &= \int_{t_1}^{t_2} \epsilon \eta(t) \frac{\partial L}{\partial q(t)} dt + \int_{t_1}^{t_2} \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} dt +  O(\epsilon^2) \\
    \end{align*}
$$

Using integration by parts on the second integral:

$$  
    \begin{align*}
        u = \frac{\partial L}{\partial q^{\prime}(t)}, \quad du = \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt \\
        dv = \epsilon \frac{d\eta(t)}{dt}dt = \epsilon d\eta(t), \quad v = \epsilon \eta(t)
    \end{align*}
$$

$$
    \int_{t_1}^{t_2} \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} dt = \left[ \epsilon \eta(t) \frac{\partial L}{\partial q^{\prime}(t)} \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \epsilon \eta(t) \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt
$$

Combining both results, we have for $\Delta J$:

$$
    \begin{align*}
    \Delta J = \int_{t_1}^{t_2} \epsilon \eta(t) \frac{\partial L}{\partial q(t)} dt + \left[ \epsilon \eta(t) \frac{\partial L}{\partial q^{\prime}(t)} \right]_{t_1}^{t_2} - \int_{t_1}^{t_2} \epsilon \eta(t) \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt + O(\epsilon^2)\\
    \end{align*}
$$

### Functional Derivative
Suppose the variation $\eta(t)$ is zero at the points $t_1$ and $t_2$ but non-zero inbetween: we say the variation has _fixed endpoints_. In this case, the expression for $\Delta J$ simplifies:

$$
    \begin{align*}
        \Delta J = \epsilon \int_{t_1}^{t_2} \eta(t) \left( \frac{\partial L}{\partial q(t)} - \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) \right) dt + O(\epsilon^2)\\
    \end{align*}
$$

We define the variation $\delta J$ to be the first-order component of this equation, and from this we define functional derivative:

$$
    \frac{\delta J}{\delta q(t)} = \frac{\partial L}{\partial q(t)} - \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right)
$$

This is a natural definition of the functional derivative as can be seen in the expression for $\delta J$:

$$
    \delta J = \int_{t_1}^{t_2} \delta q(t) \frac{\delta J}{\delta q(t)} dt
$$

### Euler-Lagrange Equation
Which particular function $q(t)$ produces a stationary point for $J$? At a stationary point the variation $\delta J = 0$ for small changes $\delta q(t)$, by definition. In this case the functional derivative must be zero, giving us the Euler-Lagrange equation for stationary points:

$$
    \frac{\partial L}{\partial q(t)} = \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) \quad \text{where} \quad t_1 < t < t_2
$$

We see from this why the variation $\delta J$ is defined as the $O(\epsilon)$ component of $\Delta J$; as we are often interested in finding the stationary points we only need to consider where there first-order derivative is zero in order to find them.
