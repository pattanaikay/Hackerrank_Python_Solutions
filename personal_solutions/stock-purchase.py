'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

'''

def stockprice(prices):
    if not prices:
        return 0
    
    min_prices = prices[0]
    max_profit = 0

    for i, price in enumerate(prices):
        if price <= min_prices:
            min_prices = price
        else:
            max_profit = max(max_profit, price-min_prices)

    return (max_profit, i)

price_array = [7, 1, 5, 3, 6, 4]

result, indexed = stockprice(price_array)
print(f"The max profit is {result} when stock is sold on {indexed}th day")