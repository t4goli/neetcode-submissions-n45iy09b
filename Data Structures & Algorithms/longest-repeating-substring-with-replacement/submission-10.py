class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        left = 0
        right = 1
        seen = {s[0]: 1}
        maxi = 1
        curr = 1

        while right < len(s):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            maxi = max(maxi, seen[s[right]])
            if (right - left +1) - maxi <= k:
                curr += 1
            else:
                seen[s[left]] -= 1
                left += 1
            longest = max(longest, curr)
            right += 1

        # dont need curr; can do a while loop with the window size and maxi and keep 
        # moving left until valid; dont need to update maxi because window only gets
        # smaller and we already recorded a larger size, so longest will alawys
        # be accurate
            
        return longest
        