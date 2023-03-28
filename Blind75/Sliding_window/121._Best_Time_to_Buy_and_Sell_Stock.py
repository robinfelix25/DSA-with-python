

def maxProfit(prices):
    res = 0
    lowest = prices[0]
    for price in prices:
        lowest = min(lowest, price)
        res = max(res, price - lowest)
    return res

# using two pointer
def maxProfit_twopointer(prices):
    l, r = 0, 1
    max_profit = float("-inf")
    while r < len(prices):
        diff  = prices[r] - prices[l]
        if diff < 0:
            l += 1
        else:
            r += 1
        max_profit = max(max_profit, diff)

    return max_profit
prices = [7,1,5,3,6,4,100]
# print(maxProfit(prices))
print(maxProfit_twopointer(prices))