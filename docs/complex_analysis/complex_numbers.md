## Complex Numbers

### Definition
$$
    i = \sqrt{-1}
$$

$$
    z = a  + ib \quad a,b \in \mathbb{R} \quad z \in \mathbb{C}
$$

The real and imaginary parts can be identified as follows:

$$
    Re(z) = a \quad Im(z) = b
$$

The complex conjugate ("z star") is defined as follows:

$$
    z^* = a - ib
$$

### Norm
A complex number can be pictured as representing a point in a plane, with the real and imaginary parts representing the orthogonal coordinates. The norm is then given by the length of the line from the origin to the point in the plane:

$$
    |z| = \sqrt{a^2 + b^2}
$$

$$
    zz^* = |z|^2
$$

### Multiplication
Multiplication of complex numbers proceeds like any other product of bracketed expressions:

$$
    (a+ib)(c+id) = ac + iad + ibc - bd
$$

### Division
Dividing complex numbers can be achieved by multiplying above and below by the complex conjugate of the denominator:

$$
    \frac{a+ib}{c+id} = \left( \frac{a+ib}{c+id} \right) \left( \frac{c-id}{c-id} \right)
$$


### Polar Form
Considering the complex number $z$ as a point in a two-dimensional plane, we can write $z$ in polar form using the angle $\theta$ between the line from the origin of length $|z|$ and the real axis:

$$
    z = |z| \left( \cos{\theta} + i\sin{\theta} \right)
$$

### Euler's Formula

$$
    e^{i\theta} = cos{\theta} + i\sin{\theta}
$$

### Cauchy-Riemann Equations
For a function of a complex variable, the Cauchy-Riemann equations establish a necessary and sufficient condition for the function to be differentiable. The function $f(z)$ can be split into two components, each acting on the real and imaginary parts:

$$
    f(z) = u(a, b) + v(a, b)
$$

Then the condition for differentiability is:

$$
    \frac{\partial{u}}{\partial{a}} = \frac{\partial{v}}{\partial{b}} \quad \quad \frac{\partial{u}}{\partial{b}} = - \frac{\partial{v}}{\partial{a}}
$$
