class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        for string in strs:
            c = [0]*26
            for l in string:
                c[ord(l) - ord('a')] += 1
            c = tuple(c)
            if c in t:
                t[c].append(string)
            else:
                t[c] = [string]
        return list(t.values())
