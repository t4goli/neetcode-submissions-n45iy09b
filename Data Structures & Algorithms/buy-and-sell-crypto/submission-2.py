class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        for i, val in enumerate(prices):
            if val < mini:
                mini = val
            maxi = max(maxi, val - mini)
        return maxi

