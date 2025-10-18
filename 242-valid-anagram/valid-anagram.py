class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2= {}

        if len(s) != len(t):
            return False

        for c, c2 in zip(s,t):
            d[c] = d.setdefault(c, 0) + 1
            d2[c2] = d2.setdefault(c2, 0) + 1

        if d == d2:
            return True

        return False