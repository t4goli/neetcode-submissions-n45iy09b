class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        index = int((len(nums) - 1) /2)
        high = len(nums) - 1
        low = 0
        if nums[index] == target:
            return index
        if nums[high] == target:
            return high
        if nums[low] == target:
            return low
        else:
            while low != index and high != index:
                print(index)
                print(high)
                print(low)
                if target > nums[index]:
                    low = index
                    index = int((high - low) /2) + low
                else:
                    high = index
                    index = int((high - low) /2) + low
                if nums[index] == target:
                    return index
        return -1

