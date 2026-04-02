class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""    
        for i, val in enumerate(s):
            if val.isalnum():
                clean += val.lower()

        return clean == clean[::-1]