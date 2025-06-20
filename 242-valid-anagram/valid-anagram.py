class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return False if len(s) != len(t) else (True if (''.join(sorted(s)) == ''.join(sorted(t))) else False)