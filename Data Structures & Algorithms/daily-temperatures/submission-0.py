class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        y = 0
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures), 1):
            if len(stack) == 0:
                stack.append(i)
            else:
                while temperatures[i] > temperatures[stack[-1]]:
                    y = stack.pop()
                    res[y] = i - y
                    if len(stack) == 0:
                        break
                stack.append(i)

        return res
        