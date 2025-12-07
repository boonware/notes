## Green Functions
The Britsh mathematical physicist George Green (1793 - 1841) introduced the concept known now as a Green function, an important tool for solving differential equations.

### Definition

Consider the following equation where a **known** linear operator $L$ acts on an **unknown** function $\psi(x)$ to produce a **known** function $f(x)$:
$$
    L \psi(x) = f(x)
$$

How can we find $\psi(x)$? We introduce a function $G(x, s)$ known as a **Green function** defined as

$$
    LG(x, s) = \delta(x-s)
$$

where $\delta(x-s)$ is the Dirac delta function. Multiplying the above by $f(s)$ and integrating over $s$, we have

$$
    \int LG(x, s) f(s) ds = \int \delta(x-s) f(s) ds
$$

By the definition of the Dirac delta function and since $L$ does not depend on $s$, we get

$$
    L \int G(x, s) f(s) ds = f(x)
$$

By comparison with the original equation:

$$
    \psi(x) = \int G(x, s) f(s) ds
$$

This is known as a Fredholm integral equation.

### Example

Consider the following differential equation:

$$
    y^{\prime \prime}(x) + y(x) = f(x)
$$

In this case the linear operator $L$ is given by:

$$
    L = \frac{d^2}{dx^2} + 1
$$

From above we know that $y(x)$ is given by the following:

$$
    y(x) = \int G(x, s) f(s) ds
$$

How can we find $G(x, s)$ ? Let's start with the definition of $G(x, s)$ and apply the operator:

$$
    \begin{align*}
        LG(x, s) = \delta(x-s) \\
        \frac{d^2 G(x, s)}{dx^2} + G(x, s) = \delta(x-s)
    \end{align*}
$$

Let us use the Fourier integral representation of the Dirac delta function:

$$
    \frac{d^2 G(x, s)}{dx^2} + G(x, s) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-ik(x-s)} dk
$$

SInce the right-hand side of the equality is a Fourier integral then the left-hand side must also be; the second derivative of such an integral is still a Fourier integral and so is the sum of this with another such integral. Therefore, there must be a Fourier representation of $G(x,s)$ in terms of the frequency $k$ that has the following form:

$$
    G(x, s) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-ik(x - s)} \hat{G}(k) dk
$$

$$
    \begin{align*}
         \\
        \frac{dG(x,s)}{dx} = \frac{-ik}{2\pi} \int_{-\infty}^{\infty} e^{-ik(x - s)} \hat{G}(k) dk \\
        \frac{d^2G(x,s)}{dx^2} = \frac{-k^2}{2\pi} \int_{-\infty}^{\infty} e^{-ik(x - s)} \hat{G}(k) dk
    \end{align*}
$$

Our equation finally reduces to the following when the integrals are cancelled out:

$$
    \begin{align*}
        -k^2\hat{G}(k) + \hat{G}(k) - 1 = 0 \\
        \hat{G}(k) = \frac{1}{1 - k^2}
    \end{align*}
$$

$$
     G(x, s) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} \frac{e^{-ik(x - s)}}{1 - k^2} dk
$$

This integral poses a problem: there are two poles at $k = \pm1$ where the denominator becomes zero. Contour integrals on the complex plan are ideal to treat these kinds of problems. We perform an analytic continuation of $G(x,s)$ into the complex numbers:

$$  
    \begin{align*}
        x \to z = x + i \eta \quad G(x,s) \to G(z) \\
         \lim_{\eta \to 0} G(z) = G(x) \\
    \end{align*}
$$

TODO