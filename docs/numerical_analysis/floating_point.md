## Floating-Point Arithmetic

IEEE 754 is the technical standard for computer arithmetic. It defines two formats for representing real numbers $x$:

* single precision (32 bits): $10^{-38} \lt |x| \lt 10^{38}$
* double precision (64 bits): $10^{-308} \lt |x| \lt 10^{308}$

If a number is greater than what a computer can handle this results in **overflow**, an error. If a number is smaller than what a computer can handle then this is **underflow**, but this is not an error as the number is zero!

The relative error is defined as follows, where $fl(x)$ is the approximated value of the real number $x$ represented as a floating-point number:

$$
    u = \frac{|x - fl(x)|}{|x|}
$$

The maximum possible relative error is known as the **machine epsilon**:

* single precision: $u \le 5.96\times10^{-8}$
* double precision: $u \le 1.11\times10^{-16}$

