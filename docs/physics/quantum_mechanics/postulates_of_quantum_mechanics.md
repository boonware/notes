# Postulates of Quantum Mechanics

## Postulate 1 - The Wave Function
The state of a system is completely given by a wave function. This wave function is a complex vector of unit length in a particular kind of vector space called a Hilbert space.

### Probability
_How_ does the wave function describe the state of a system? The wave function is interpreted as telling us the _probability_ of a system being in a particular state. Specifically, for a wave function that has continuous values, the _absolute value squared_ of the wave function is a _probability density function_ (PDF), whereas for a wave function that has discrete values it is a _probability mass function_ (PMF).

Let $\psi(x)$ be a wave function. If $\psi(x)$ takes continuous values then it must be a square-integrable function and the following must be true:

$$
  \int_{-\infty}^{\infty} \psi(x)^\star \psi(x) dx = \int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
$$

If the variable $x$ can only take discrete values then:

$$
  \sum_{i=1}^\infty \psi(x_i)^\star\psi(x_i) = \sum_{i=1}^\infty |\psi(x_i)|^2 = 1
$$

### Particle Position

Let $x$ be the position of a particle and $\psi(x)$ the wave function, where $|\psi(x)|^2$ is a probability density function. We can define the mean and standard deviation for the particle position as shown below. Notice how the variables are "sandwiched" inbetween the wave function and its complex conjugate. While this does not matter in the case of particle position and is written like this for the sake of convention, we will see later that this _does_ matter for other properties such as momentum that are represented by an _operator_ that _act_ on the wave function.

$$
  \langle x \rangle = \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx \tag{Mean}
$$

$$
  (\Delta x)^2 = \int_{-\infty}^{\infty} \psi(x)^\star (x -  \langle x \rangle)^2 \psi(x) dx \tag{Variance}
$$

The variance can also be written as follows:

$$
  \begin{align*}
     (\Delta x)^2 &= \int_{-\infty}^{\infty} \psi(x)^\star (x^2 + \langle x \rangle^2 - 2x \langle x \rangle) \psi(x) dx \\
     &= \int_{-\infty}^{\infty} \psi(x)^\star x^2 \psi(x) dx + \int_{-\infty}^{\infty} \psi(x)^\star \langle x \rangle^2 \psi(x) dx - 2\langle x \rangle \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx \\
     &= \langle x^2 \rangle - \langle x \rangle^2
  \end{align*}
$$

### Uncertainty
We can quantify the uncertainty in the particle's position by using the standard deviation $\Delta x$. Using the standard deviation in this way is a standard approach in mathematics to quantify the spread of a probability distribution.

$$
  \Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} \tag{Uncertainty in Position}
$$

### Particle Momentum

Following the same formalism, the expectation value of the momentum is given by

$$
  \langle p \rangle = \int_{-\infty}^{\infty} \psi(x, t)^\star p \psi(x, t) dx
$$

In this case we assume that the wave function is also a function of time $t$. If the wave function was only a function of position $x$ then the position could not change in time and hence the particle could not have momentum, which is associated with movement.

How can we find an expression for $p$ in terms of $x$ to compute the integral? Let's start with a wave that describes the motion of a free particle:

$$
  \psi(x, t) = Ae^{i(kx - \omega t)}
$$

$$
  \frac{\partial \psi(x, t)}{\partial x} = i k \psi(x, t)
$$

Noting that the momentum is given by $p = \hbar k$ from the De Broglie equation, where $k = \frac{2 \pi}{\lambda}$ is the wave number, we can write

$$
  p \psi(x, t) = -i \hbar \frac{\partial \psi(x, t)}{\partial x}
$$

We can thus define an _operator_ for momentum:

$$
  \hat{p} = -i \hbar \frac{\partial }{\partial x}
$$

## Postulate 2 - Observables

All measurable properties of a system, so called "observables", are represented by linear operators on the Hilbert space.

The momentum operator:


