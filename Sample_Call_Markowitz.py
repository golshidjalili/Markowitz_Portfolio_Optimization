import numpy as np
from Markowitz import optimize_portfolio

prices = np.array(
 [[126.60, 128.23, 131.88, 130.96,
 131.97, 136.69, 134.87, 133.72,
 132.69, 133.41, 133.01, 129.60,
 132.92, 132.05, 130.98, 134.80,
 134.89, 134.91, 134.14],
 [72.92, 73.06, 72.73, 73.40,
 72.99, 72.85, 71.50, 72.50,
 73.29, 72.49, 73.46, 74.07,
 76.34, 77.22, 75.63, 76.75,
 71.23, 73.25, 74.26]]
)

stock_names = ['AAPL', 'DELL']
risk_free_interest_rate = 0.05

# Call 1
# output: {'AAPL': 65.373, 'DELL': 34.627}
optimize_portfolio(prices, stock_names, risk_free_interest_rate)

# Call 2
# {'AAPL': 9805950.0, 'DELL': 5194050.0}
optimize_portfolio(prices, stock_names, risk_free_interest_rate, total_asset=150000)
