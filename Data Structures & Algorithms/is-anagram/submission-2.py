class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string = {}
        for letter in s:
            if letter in string:
                string[letter] += 1
            else:
                string[letter] = 1
        for letter in t:
            if letter not in string:
                return False
            string[letter] -= 1
            if string[letter] < 0:
                return False
        for key in string:
            if string[key] != 0:
                return False
        return True
