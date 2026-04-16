class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        mini = nums[low]
        while low <= high:
            mid = (low + high) // 2
            mini = min(nums[mid], mini)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        return mini