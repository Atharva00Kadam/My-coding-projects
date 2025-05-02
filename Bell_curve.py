from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

lambda_param = 1

# Calculate PDF for a range of values
x = np.linspace(0, 10, 1000)
pdf = expon.pdf(x, scale=1/lambda_param)

# Calculate CDF for a range of values
cdf = expon.cdf(x, scale=1/lambda_param)

# Plot the PDF
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, pdf, 'b-', lw=2)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Probability Density Function (PDF) of Exponential Distribution')

# Plot the CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'r-', lw=2)
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function (CDF) of Exponential Distribution')

plt.show()
