## Euler-Lagrange Equations

### The Lagrangian
Define the _Lagrangian_ $L: C^n \to \mathbb{R{}}$ as functional of $q(t)$, $q^{\prime}(t)$ and $t$:

$$
    L[q(t), q^{\prime}(t), t] \quad t \in \mathbb{R{}}
$$

Such a functional is said to be _local_ in $q$ as it depends on only finitely many derivatives of $q$. We will study the case where the functional depends only on $q(t)$ and its first derivative $q^{\prime}(t)$; in general, the functional may also depend explicitly on $t$. We will see that the method developed below will generalize easily to functionals that depend on higher derivaties also.

### Principle of Least Action
The _action_ $S$ is defined as the integral of the Lagrangian over time:

$$
    S = \int_{t_1}^{t_2} L[q(t), q^{\prime}(t), t] dt
$$

In the Calculus of Variations we aim to _minimize_ this integral, that is, _which_ function $q(t)$ will give the smallest integral between $t_1$ and $t_2$? For a function $f(x)$ we can find the minima by solving $f^{\prime}(x) = 0$ where $f^{\prime \prime}(x) > 0$, but in our case we are trying to minimize the action with respect to a functional so we need a new definition of the derivative, a _functional_ derivative.

Suppose we _vary_ $q(t)$ by making a small change, where $0 < \epsilon \ll1$:

$$
    q(t) \to q(t) + \epsilon\eta(t)
$$

The corresponding change in the action is given by:

$$
    \delta S = \int_{t_1}^{t_2} \left(L[q(t) + \epsilon \eta(t), q^{\prime}(t) + \epsilon \eta ^{\prime}(t), t] - L[q(t), q^{\prime}(t), t] \right) dt
$$

If $S$ is at a minimum then the variation in $q(t)$ should give $\delta S = 0$, consistent with what we know about differentiation in general, i.e. a minimum for a function $f(x)$ is where $\frac{df(x)}{dx} = 0$.

Let us expand $L$ as a Taylor series, where $O(\epsilon^2)$ represents the terms of order $\epsilon^2$ and higher.

$$
   L[q(t) + \epsilon \eta(t), q^{\prime}(t) + \epsilon \eta ^{\prime}(t), t] = L[q(t), q^{\prime}(t), t] + \epsilon \eta(t) \frac{\partial L}{\partial q(t)} + \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} + O(\epsilon^2)
$$

The integral can then be expressed as follows:

$$
    \begin{align*}
    \delta S &= \int_{t_1}^{t_2} \left(\epsilon \eta(t) \frac{\partial L}{\partial q(t)} + \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} + O(\epsilon^2) \right) dt \\
   &= \int_{t_1}^{t_2} \epsilon \eta(t) \frac{\partial L}{\partial q(t)} dt + \int_{t_1}^{t_2} \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} dt +  O(\epsilon^2) \\
    \end{align*}
$$

Using integration by parts on the second integral:

$$  
    \begin{align*}
        u = \frac{\partial L}{\partial q^{\prime}(t)}, \quad du = \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt \\
        dv = \epsilon \eta^{\prime}(t) dt, \quad v = \int_{t_1}^{t_2} \epsilon \frac{d\eta(t)}{dt} dt = \epsilon \eta(t) \Big|_{t_1}^{t_2}
    \end{align*}
$$

$$
    \int_{t_1}^{t_2} \epsilon \eta^{\prime}(t) \frac{\partial L}{\partial q^{\prime}(t)} dt = \epsilon \eta(t) \Big|_{t_1}^{t_2} \left( \frac{\partial L}{\partial q^{\prime}(t)} - \int_{t_1}^{t_2}  \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt \right)
$$

Combining both results, we have for $\delta S$:

$$
    \begin{align*}
    \delta S = \int_{t_1}^{t_2} \epsilon \eta(t) \frac{\partial L}{\partial q(t)} dt + \epsilon \eta(t) \Big|_{t_1}^{t_2} \left( \frac{\partial L}{\partial q^{\prime}(t)} - \int_{t_1}^{t_2}  \frac{d}{dt} \left( \frac{\partial L}{\partial q^{\prime}(t)} \right) dt \right) \\
   
    \end{align*}
$$
