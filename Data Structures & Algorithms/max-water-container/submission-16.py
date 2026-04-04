class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        if len(heights) < 2:
            return 0
        greatest = 0
        second = 0
        third = 0
        greater = 0
        while (i < j):
            curr = (min(heights[i], heights[j])) * (j - i)
            if heights[i + 1] >= heights[i]:
                second = (min(heights[i + 1], heights[j])) * (j - i - 1)
            if heights[j - 1] >= heights[j]:
                third = (min(heights[i], heights[j - 1])) * (j - i - 1)
            if (heights[i] >= heights[j]):
                j -= 1
            if (heights[i] < heights[j]):
                i += 1
            greatest = max(curr, second, third, greatest)
        return greatest
            
            