class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""    
        for i, val in enumerate(s):
            if val.isalnum():
                clean += val.lower()
        i = 0
        j = len(clean) - 1
        while (i < j):
            if clean[i] != clean[j]:
                return False
            else:
                i += 1
                j -= 1
        return True