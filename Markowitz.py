import numpy as np


def optimize_portfolio(prices, stock_names, risk_free_interest_rate, stocks_on_rows=True, total_asset=False):
    """
    Calculate optimized ratios of given stocks.

    :param prices: a matrix (two-dimensional nparray) containing a history of previous stock prices
                for a number of stocks. Prices are organized in rows/columns,with each row/column containing
                prices of a single stock.
    :param stock_names: a list containing names of the stocks under study.
    :param risk_free_interest_rate: a positive float number
    :param stocks_on_rows: (True by default) a Boolean variable indicating whether prices for each stock are located
                        on a row (rather than a column).
    :param total_asset:(False by default) If assigned a value, your function must return the required amount of money
    to be invested in each stock (rather than the ratios).

    :return: a dictionary with stock names as keys and either optimized ratios or investment amounts
        (depending on total_asset variable) as values.
    """
    if not stocks_on_rows:
        prices = prices.T

    shifted_prices = np.zeros_like(prices)
    shifted_prices[:, 1:] = prices[:, :-1]
    returns = (prices - shifted_prices) / shifted_prices
    returns = np.delete(returns, 0, axis=1)

    risk_surplus_on_mean_returns = np.mean(returns, axis=1).reshape((-1, 1)) - risk_free_interest_rate
    coefficients_matrix = np.cov(returns)
    non_scaled_proportions = np.linalg.solve(coefficients_matrix, risk_surplus_on_mean_returns)
    optimized_portfolio = dict()
    for idx_stock, stock in enumerate(stock_names):
        optimized_portfolio[stock] = round(
            float(non_scaled_proportions[idx_stock] / np.sum(non_scaled_proportions)) * 100, 3
        )
        if total_asset:
            optimized_portfolio[stock] *= total_asset
    return optimized_portfolio
