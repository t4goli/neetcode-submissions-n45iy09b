class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i, val in enumerate(prices):
            j = i + 1
            while (j < len(prices)):
                if val < prices[j]:
                    maxi = max(maxi, prices[j] - val)
                j += 1
        return maxi

