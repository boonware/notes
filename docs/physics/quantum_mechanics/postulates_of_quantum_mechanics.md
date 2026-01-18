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

### Position

Let $x$ be the position of a particle and $\psi(x)$ the wave function, where $|\psi(x)|^2$ is a probability density function. We can define the mean and standard deviation for the particle position as shown below. Notice how the variables are "sandwiched" inbetween the wave function and its complex conjugate. While this does not matter in the case of particle position and is written like this for the sake of convention, we will see later that this _does_ matter for other properties such as momentum that are represented by an _operator_ that _act_ on the wave function.

$$
  \langle x \rangle = \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx \tag{Mean}
$$

$$
  (\Delta x)^2 = \int_{-\infty}^{\infty} \psi(x)^\star (x -  \langle x \rangle)^2 \psi(x) dx \tag{Standard Deviation}
$$

The standard deviation can also be written as follows:

$$
  \begin{align*}
     (\Delta x)^2 &= \int_{-\infty}^{\infty} \psi(x)^\star (x^2 + \langle x \rangle^2 - 2x \langle x \rangle) \psi(x) dx \\
     &= \int_{-\infty}^{\infty} \psi(x)^\star x^2 \psi(x) dx + \int_{-\infty}^{\infty} \psi(x)^\star \langle x \rangle^2 \psi(x) dx - 2\langle x \rangle \int_{-\infty}^{\infty} \psi(x)^\star x \psi(x) dx \\
     &= \langle x^2 \rangle - \langle x \rangle^2
  \end{align*}
$$

## Postulate 2 - Observables

All measurable properties of a system, so called "observables", are represented by linear operators on the Hilbert space.

The momentum operator:

$$
  \hat{p} = -i \hbar \frac{\partial }{\partial x}
$$
