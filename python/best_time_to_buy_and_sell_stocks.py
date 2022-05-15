from typing import List

def maxProfit(prices : List[int]) -> int:
	best_profit = 0
	best_buy_price = prices[0]
	for price in prices:
		best_buy_price = min(best_buy_price, price)
		actual_profit = price - best_buy_price
		best_profit = max(actual_profit, best_profit)
	return best_profit

# O(n) time complexity and O(1) space complexity, pretty easy.

# Pattern:
# We are always looking in the future, so scan the array to get the minimum for the best price, 
# but we want to maximize the profit so keep track of the best profit and compare with the actual one 
# (difference btw best buying price and actual price). 
