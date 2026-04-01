class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0
        length = 0
        for num in s:
            if num - 1 not in s:
                while num in s:
                    num += 1
                    length += 1
            if length > long:
                long = length
            length = 0
        return long

