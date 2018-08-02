import numpy as np

x = np.linspace(-2,2,100)
y = np.cos(x)

theta = np.random.random((3,1))
m = len(y)

for i in range(10000):
    #Calculate my y_hat
    y_hat = np.array([(theta[0]*(a**2) + theta[1]*a + theta[2]) for a in x])

    #Calculate my cost based off y_hat and y
    cost = np.sum((y_hat - y) ** 2) * (1/m)

    #Calculate my derivatives based off y_hat and x
    da = (2 / m) * np.sum((y_hat - y) * (x**2))
    db = (2 / m) * np.sum((y_hat - y) * (x))
    dc  = (2 / m) * np.sum((y_hat - y))

    #update step
    theta[0] = theta[0] - 0.0001*(da)
    theta[1] = theta[1] - 0.0001*(db)
    theta[2] = theta[2] - 0.0001*(dc)

    print("Epoch Num: {} Cost: {}".format(i, cost))

print(theta)
