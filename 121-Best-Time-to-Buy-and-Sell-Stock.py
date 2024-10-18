class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for i in range(1, len(prices)):
            if prices[l] > prices[i]:
                l = i
                continue
            profit = max(profit, prices[i] - prices[l])

        return profit 
        