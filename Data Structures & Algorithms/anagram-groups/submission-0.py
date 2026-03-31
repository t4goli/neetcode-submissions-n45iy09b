class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        for string in strs:
            l = "".join(sorted(string))
            if l not in t:
                t[l] = []
                t[l].append(string)
            else:
                t[l].append(string)
        return list(t.values())
