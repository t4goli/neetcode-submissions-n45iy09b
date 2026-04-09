class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        num = len(s1)
        for i in range(len(s1)):
            if s1[i] in seen:
                seen[s1[i]] += 1
            else:
                seen[s1[i]] = 1
        
        left = 0
        right = 0
        seentwo = {}
        while right in range(len(s2)):
            if s2[right] in seentwo:
                seentwo[s2[right]] += 1
            else:
                seentwo[s2[right]] = 1
            if right - left >= num:
                seentwo[s2[left]] -=1
                if seentwo[s2[left]] == 0:
                    del seentwo[s2[left]]
                left += 1
            if seentwo == seen:
                return True
            right += 1
        
        return False
