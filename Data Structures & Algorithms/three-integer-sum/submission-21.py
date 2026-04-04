class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []    
        nums.sort()
        rem = 0
        j = 0
        k = 0
        for i in range(len(nums)):
            if (nums[i] == nums[i-1] and i > 0):
                continue
            rem = 0 - nums[i]
            if (i + 1 < len(nums)):
                j = i + 1
            k = len(nums) - 1
            if nums[j] == nums[j - 1] and j != i + 1:
                continue
            while (j < k):
                if (nums[j] == nums[j -1] and j != i + 1):
                    j += 1
                    continue
                if (nums[j] + nums[k] == rem):
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    continue
                if (nums[j] + nums[k] < rem):
                    j += 1
                    continue
                if (nums[j] + nums[k] > rem):
                    k -= 1
                    continue
        return out