class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
        ]
        group_anagram = defaultdict(list)

        for word in strs:
            key = math.prod(primes[ord(c) - ord('a')] for c in word)
            group_anagram[key].append(word)
            
        return list(group_anagram.values())