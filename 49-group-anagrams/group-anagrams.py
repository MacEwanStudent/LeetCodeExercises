from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagramLists= defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            groupAnagramLists[sorted_word].append(word)
        #Converts the ouput into a List[List[str] as per instructions.
        return list(groupAnagramLists.values())