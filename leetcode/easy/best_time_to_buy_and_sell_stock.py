class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0

        buy_price = prices[0]
        buy_date = 0
        profit = 0

        for idx, price in enumerate(prices):
            if price < buy_price:
                buy_price = price
                buy_date = idx
            if price > buy_price and buy_date < idx:
                sell_price = price
                profit = max(profit, sell_price-buy_price)
        return profit




sol = Solution()
prices = [1]
# prices = [7,9, 5, 1, 8, 9]
# prices = [2,4,1]

result = sol.maxProfit(prices)
print(result)
#Output: 5



# Input: prices = [7,6,4,3,1]
# Output: 0
