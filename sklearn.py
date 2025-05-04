import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data for house sizes (square feet) and house prices (thousands of dollars)
X = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]).reshape(-1, 1)
y = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])

# Creatung a Linear Regression model
model = LinearRegression().fit(X, y)

# TODO: Obtain slope (m) and intercept (c) from model
m = model.coef_[0]
c = model.intercept_

# Plotting the data
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price (in $1000)')
plt.title('House Size vs Price')
plt.show()
