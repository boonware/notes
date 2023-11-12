## Feature Scaling

### Motivation

#### Example: Linear Regression
Consider using a linear regression model for predicting the price of a house based on the number of floors and floor area in square feet. The features in the training data have ranges $0 \le x_{floors} \le 3$ and $0 \le x_{area} \le 3500$. Now consider what happens to the price for two houses with the same number of floors but areas 500 and 1500 $\text{ft}^2$, respectively. If $\theta_{floors} \sim \theta_{area}$ then the price of both houses differ by a factor of approximately 1000, the difference in area. In this model, if the first house costs \$500,000 then the second would cost \$500,000,000! This is clearly unrealistic. When determining the price, the feature with the larger scale has a disproportionate impact on the predicted value.

#### Example: Gradient Descent
In the example above the house prices in the training data will be actual (i.e. realistic) values, and consequently we could assume that a good hypothesis function will have $\theta_{floors} >> \theta_{area}$ so that the impact of $x_{area}$ is reduced. However, this in turn causes problems for gradient descent. When performing gradient descent the step size $\alpha$ must be chosen small enough for $\theta_i$ with the smallest scale so as to not overshoot the minimum, however, this small $\alpha$ may dramatically slow down the convergence in the directions of $\theta_i$ with much larger scales. Adjusting all features to have similar scale can improve the efficiency of convergence.

#### Example: Clustering
Consider a model which assigns a person to a t-shirt size of either small or large. The features used to predict the assignment are mass in kilograms and height in feet. This assignment can be achieved using a clustering algorithm, where some measure is calculated for each new person and compared to the mean of this measure for the small and large samples, respectively. For example, suppose we use the Euclidean distance as measure, where $m$ and $m_\mu$ are the mass and mean mass, $h$ and $h_\mu$ are the height and mean height:

$$
    d = \sqrt{(m - m_\mu)^2 + (h - h_\mu)^2}
$$

Let us calculate the distance for a new person whom we wish to assign a t-shirt size. The mean values from our model are as follows:

* Large: $m_\mu = 80$ , $h_\mu = 6.1$
* Small: $m_\mu = 55$ , $h_\mu = 5.2$

Calculate the distance from each mean for a new person with height 6 ft and mass 67 kg:

* $d_{large} = 13.00$
* $d_{small} = 12.03$

The person is assigned a small t-shirt size as $d_{small}$ is smaller, i.e. they are closer to the mean for the small t-shirt size data. I think you would agree that a person who is 6 ft tall would be better to wear a large size! Again, we see how the feature with the larger scale is dominating the outcome.

### Min-Max Normalization
Features can be scaled to the range $[0, 1]$ using min-max normalization:

$$
    x^\prime_i = \frac{x_i - \min(x_i)}{\max(x_i) - \min(x_i)}
$$

Min-max normalization is sensitive to outliers; extreme values will be very close to one and cause non-extreme values to be "squashed" into a small interval closer to zero due to the denominator being large.

### Mean Normalization
Another approach to normalization subtracts the feature's mean $\mu_i$ from each value, and divides by the range:

$$
    x^\prime_i = \frac{x_i - \mu_i}{\max(x_i) - \min(x_i)}
$$

### Z-score Normalization (Standardization)
Features that follow a Gaussian distribution can be scaled using standardization so that each feature $x_i$ has approximately zero mean $\mu_i$ and standard deviation of 1.

$$
    x^\prime_i = \frac{x_i - \mu_i}{\sigma_i}
$$

### Choosing a Method
The method of rescaling to choose depends on the particular task at hand and the data. Often, multiple methods may be compared to select the most appropriate for a given situation. In certain cases care must be taken when applying rescaling, for example in linear regression rescaling must not be applied to $x_0 = 1$.
