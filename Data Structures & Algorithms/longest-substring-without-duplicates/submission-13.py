class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        seen = {s[0]: 0}
        maxi = 1
        curr = 1
        while right < len(s):
            print(left)
            print(right)
            if s[right] in seen and left <= seen[s[right]]:
                left = seen[s[right]] + 1
                seen[s[right]] = right
            else:
                seen[s[right]] = right
            curr = right - left + 1
            right += 1
            print(curr)
            print(maxi)
            maxi = max(maxi, curr)

        return maxi


