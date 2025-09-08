## What is Machine Learning?
The term machine learning (ML) was coined in 1959 by Arthur Samuel, an IBM computer scientist and early pioneer in artificial intelligence. He defined machine learning as the _"field of study that gives computers the ability to learn without being explicitly programmed"_.

Computer scientist Tom Mitchell later gave a more formal definition of machine learning (1998): _"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E."_

For example, consider automated spam filtering of emails:
* T = automated filtering of spam emails. 
* E = the user manually marking an email as spam.
* P = fraction of spam emails filtered automatically.

## What is a Model?
In machine learning we often speak of models. When we chose an algorithm that is suitable for the ML task at hand, we run that algorithm on a dataset and the output is our model. This process is called _training the model_. The dataset passed to the algorithm is called _training data_ and is used by the algorithm to learn how to produce the desired output. The model is then used for predicting outcomes based on new input values.

## Machine Learning Algorithms
Algorithms for machine learning can be broadly classified into one of a number of high-level categories.

### Supervised Learning
In supervised learning the training data passed to the algorithm contains example input _and_ output values. The algorithm learns the relationship between the input and output based on these examples. This kind of training data, which contains both the input and desired output, is called _labelled data_.

### Unsupervised Learning
In contrast to supervised learning, unsupervised learning uses training data with only input values. The algorithm discovers patterns in the data by itself without any examples of desired output. This kind of training data is called _unlabelled data_.

### Reinforcement Learning
Unlike both supervised and unsupervised learning, reinforcement learning does not use either labelled or unlabelled data. An "agent" interacts with an environment via trial and error and is either rewarded or punished depending on the output of the model. In this way, the model is continuously trained or optimized as input data from the environment produces an output, and the model learns to produce output for which it will be rewarded.
