class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = [0] * 2
        first = 0
        second = 0
        for i in range(len(numbers)):
            j = i + 1
            while ((i < j) and (i != j) and (j in range(len(numbers)))):
                if (numbers[i] + numbers[j]) == target:
                    out[0] = i + 1
                    out[1] = j + 1
                    return out
                j += 1