class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i, val in enumerate(prices):
            j = i - 1
            while j > -1:
                maxi = max(maxi, val - prices[j])
                j -= 1
                print(maxi)
        return maxi

