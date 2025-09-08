## Schrödinger Equation

$$
    i \hbar \frac {\partial{\Psi(x,t)}}{\partial{t}} = \hat{H} \Psi(x,t)
$$

For a single, non-relativistic particle, the Hamiltonian operator $\hat{H}$ is given by the sum of the kinetic and potential energies:

$$
    \hat{H} = -\frac{\hbar^2}{2m} \nabla^2  + V(x,t)
$$

### Time-Independent Form

Consider a potential that only depends on position, $V(x)$. Perform _separation of variables_ on the Schrödinger equation to write the wave function as follows:

$$
    \Psi(x,t) = \phi(x)\omega(t)
$$

This is not always possible for an arbitrary function, as can be seen with the following counter example where the exponential cannot be split into a product of two other functions $g$ and $h$:

$$
    f(x,t) = e^{xt} \ne g(x) h(t) \tag{1}
$$

Let us make an _assumption_ that the wavefunction can be split as above, and see what happens. 

$$
    \begin{align*}
        & i \hbar \phi(x) \frac {\partial{\omega(t)}}{\partial{t}} = \left[ -\frac{\hbar^2}{2m} \nabla^2  + V(x) \right]\phi(x)\omega(t) \\
        & \frac{i \hbar}{\omega(t)} \frac {\partial{\omega(t)}}{\partial{t}} = \frac{1}{\phi(x)} \left[ -\frac{\hbar^2}{2m} \nabla^2 \phi(x) + V(x) \phi(x) \right] \\
    \end{align*}
$$

The LHS depends only on time and the RHS depends only on position. For both sides to be equal they must equal a constant. Let us call this constant $E$:

$$
    \frac{1}{\phi(x)} \left[ -\frac{\hbar^2}{2m} \nabla^2 \phi(x) + V(x) \phi(x) \right] = E
$$

We can now write the following time-independent form, which we can see is an eigenvalue equation for the Hamiltonian:

$$
    \hat{H} \phi(x) = E \phi(x)
$$

In what kind of physical situation is this relevant? The electrostatic field felt by an electron can be modeled by $V(x)$, with contributions from the electrostatic field of the atomic nucleus and other electrons. If we hypothesise that the electron's wave function takes the form of a stationary wave then we can indeed perform a separation of variables as above.
