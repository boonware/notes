## Time-Series Forecasting

### Random Noise
TODO
autocorrelation
mean and var of models

### Autoregressive Model (AR)
If we model a value $y_t$, that is, the value $y$ of a time series at some time $t$, as a linear combination of values at previous times, we have the autoregressive model. The name refers to the fact that $y_t$ is a regression on previous values of the series, i.e. on previous values of itself. We use the notation $y_t$ as this represents the value at a specific time $t$, whereas $y(t)$ refers to a function that represents the entire series. The AR model of order $n$ is given by:

$$
    AR(n): \quad y_t = c + \epsilon_t + \sum^n_{i=1} \phi_i y_{t-i}
$$

where $c$ is a constant, $\epsilon_t$ is the random noise present at time $t$, and $\phi_i$ are the model parameters, i.e. how much each previous value $y_{t-i}$ contributes to $y_t$. The values $y_{t-i}$ are known as **lags**.
 
### Moving Average Model (MA)

$$
    MA(n): \quad y_t = \mu + \epsilon_t + \sum^n_{i=1} \theta_i \epsilon_{t-i}
$$

### ARMA Model
TODO - where did the constant and mean go?

$$
    ARMA(p,q): \quad y_t = \epsilon_t + \sum^p_{i=1} \phi_i y_{t-i} + \sum^q_{i=1} \theta_i \epsilon_{t-i}
$$
