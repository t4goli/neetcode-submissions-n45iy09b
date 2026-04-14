from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tkeys = {}
        for i, val in enumerate(t):
            if val in tkeys:
                tkeys[val] += 1
            else:
                tkeys[val] = 1
        one = 0
        two = 0
        need = len(tkeys)
        have = 0
        win = defaultdict(int)
        best = float("inf")
        bestr = 0
        bestl = 0
        while two < len(s):
            if s[two] in tkeys:
                win[s[two]] += 1
                if win[s[two]] == tkeys[s[two]]: have += 1
            while have == need:
                if best > (two - one + 1):
                    bestr = two
                    bestl = one
                    best = two - one + 1
                win[s[one]] -= 1
                if s[one] in tkeys and win[s[one]] < tkeys[s[one]]:
                    have -= 1
                one += 1
            two += 1
        if best == float("inf"):
            return ""
        return s[bestl:bestr +1]


        