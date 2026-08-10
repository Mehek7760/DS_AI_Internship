# Shopping Cart Price Update

prices = [100, 250, 80, 150, 300]

# Using loop
for i in range(len(prices)):
    prices[i] = prices[i] + 20

print("Updated prices using loop:", prices)


# Using NumPy without loop
import numpy as np

prices = np.array([100, 250, 80, 150, 300])

updated_prices = prices + 20

print("Updated prices using NumPy:", updated_prices)