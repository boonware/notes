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

Let $x$ be the position of a particle and $\psi(x)$ the wave function, where $|\psi(x)|^2$ is a probability density function. We can define the expectation value (mean) and variance for the particle position as shown below. Notice how the variables are "sandwiched" inbetween the wave function and its complex conjugate. While this does not matter in the case of particle position and is written like this for the sake of convention, we will see later that this _does_ matter for other properties such as momentum that are represented by an _operator_ that _act_ on the wave function.

$$
  \langle x \rangle = \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx 
$$

$$
  (\Delta x)^2 = \int_{-\infty}^{\infty} \psi(x)^\star (x -  \langle x \rangle)^2 \psi(x) dx
$$

The variance can also be written as follows:

$$
  \begin{align*}
     (\Delta x)^2 &= \int_{-\infty}^{\infty} \psi(x)^\star (x^2 + \langle x \rangle^2 - 2x \langle x \rangle) \psi(x) dx \\
     &= \int_{-\infty}^{\infty} \psi(x)^\star x^2 \psi(x) dx + \langle x \rangle^2 \int_{-\infty}^{\infty} \psi(x)^\star \psi(x) dx - 2\langle x \rangle \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx \\
     &= \langle x^2 \rangle - \langle x \rangle^2
  \end{align*}
$$

### Uncertainty in Position
We can quantify the uncertainty in the particle's position by using the standard deviation $\Delta x$. Using the standard deviation in this way is a standard approach in mathematics to quantify the spread of a probability distribution.

$$
  \Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}
$$

### Particle Momentum

Following the same formalism, the expectation value of the momentum is given by

$$
  \langle p \rangle = \int_{-\infty}^{\infty} \psi(x, t)^\star p \psi(x, t) dx
$$

In this case we assume that the wave function is also a function of time $t$. If the wave function was only a function of position $x$ then it could not change in time and hence the particle could not be moving as momentum is a property of movement.

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
  \hat{P} = -i \hbar \frac{\partial }{\partial x}
$$

Following the approach above for particle position, we can define the expectation value and uncertainty for momentum as follows:

$$
  \langle p \rangle = -i \hbar\int_{-\infty}^{\infty} \psi(x, t)^\star \frac{\partial \psi(x, t)}{\partial x} dx
$$

$$
  \Delta p = \sqrt{\langle p^2 \rangle - \langle p \rangle^2} 
$$

Note that the expectation value of $p^2$ contains a second-order partial differential as the operator $\hat{P}$ is applied twice to the wave function:

$$
  \langle p^2 \rangle = -\hbar^2\int_{-\infty}^{\infty} \psi(x, t)^\star \frac{\partial^2 \psi(x, t)}{\partial x^2} dx
$$


## Postulate 2 - Observables

All measurable properties of a system, so called "observables", are represented by linear operators on the Hilbert space.

A linear operator representing an observable $o$ is typically written $\hat{O}$:

$$
  \langle o \rangle = \int_{-\infty}^{\infty} \psi(x, t)^\star \hat{O} \psi(x, t) dx
$$

Some common operators are:

$$
  \begin{align*}
    \hat{X} = x \tag {one-dimensional position} \\
    \hat{\vec{R}} = \vec{r} \tag{position vector} \\
    \hat{P} = -i \hbar \frac{ \partial }{ \partial x } \tag{one-dimensional momentum} \\
    \hat{\vec{P}} = -i \hbar \vec{\nabla} \tag{momentum vector} \\
  \end{align*}
$$

Many operators can be expressed in terms of the position and momentum operators, where the same functional dependence from classical mechanics applies, for example:

$$
  \begin{align*}
    \hat{T} = \frac{\hat{P}^2}{2m} \tag{kinetic energy} \\
    \hat{\vec{L}} = \hat{\vec{R}} \times \hat{\vec{P}} \tag{angular momentum} \\
  \end{align*}
$$

An example of an operator that _cannot_ be expressed in terms of the position and momentum operators is spin.

### Commutators

How does one know if it is possible to have complete simultaneous knowledge of two specific properties of a system, say $A$ and $B$? This can only be possible if the order of measurement does not matter, or in other words measuring one property does not affect the outcome of measuring the other: $AB\psi = BA\psi$. We define the commutator of two operators to quantify this fact:

$$
  [\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}
$$

Two operators commute if their commutator is zero. If the commutator is non-zero, the operators do not commute and it is impossible to have complete simultaneous knowledge of the two properties.


