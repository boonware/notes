### Residues
The Laurent series for a complex function $f: \mathbb{C} \to \mathbb{C}$ can be written in two parts:

$$
    f(z) = \sum_{n=1}^\infty \frac{b_n}{(z-z_0)^n} + \sum_{n=0}^\infty a_n(z-z_0)^n
$$

The coefficient $b_1$ is known as the residue of $f(z)$ at $z_0$:

$$
    Res(f, z_0) = b_1
$$

Integrate the Laurent series, choosing the contour $C$ as as a circle centered on $z_0$. We can express $z$ in polar coordinates:

$$  
    \begin{align*}
        z = z_0 + re^{i\theta} \\
        dz = ire^{i\theta} d\theta
    \end{align*}
$$

$$
    \begin{align*}
        & \oint_C \left( \sum_{n=1}^\infty \frac{b_n}{(z-z_0)^n} + \sum_{n=0}^\infty a_n(z-z_0)^n \right) dz= \\
        & \sum_{n=1}^\infty \oint_C \frac{b_n}{(z-z_0)^n} dz + \sum_{n=0}^\infty \oint_C a_n(z-z_0)^n dz = \\
        & \oint_C \frac{b_1}{(z-z_0)} dz + \sum_{n=2}^\infty \oint_C \frac{b_n}{(z-z_0)^n} dz + \sum_{n=0}^\infty \oint_C a_n(z-z_0)^n dz = \\
        & \oint_0^{2\pi} \frac{ib_1re^{i\theta}}{re^{i\theta}} d\theta + \sum_{n=2}^\infty \oint_0^{2\pi} \frac{ib_nre^{i\theta}}{r^ne^{in\theta}} d\theta + \sum_{n=0}^\infty \oint_0^{2\pi} ia_nr^{n+1}e^{i\theta(n+1)} d\theta  = \\
        & \oint_0^{2\pi} ib_1 d\theta + \sum_{n=2}^\infty \oint_0^{2\pi} ib_nr^{1-n}e^{i\theta(1-n)} d\theta + \sum_{n=0}^\infty \oint_0^{2\pi} ia_nr^{n+1}e^{i\theta(n+1)} d\theta = \\
        & ib_1\theta \Big|_0^{2\pi} + \sum_{n=2}^\infty \frac{b_nr^{1-n}e^{i\theta(1-n)}}{1-n} \Big|_0^{2\pi} + \sum_{n=0}^\infty \frac{a_nr^{n+1}e^{i\theta(n+1)}}{n+1} \Big|_0^{2\pi} = \\
        & 2\pi i b_1 + \sum_{n=2}^\infty \left(\frac{b_nr^{1-n} - b_nr^{1-n}}{1-n} \right) + \sum_{n=0}^\infty \left( \frac{a_nr^{n+1} - a_nr^{n+1}}{n+1} \right) = \\
        & 2\pi i b_1
    \end{align*}
$$