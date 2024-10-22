class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_anagrams = {}

        for word in strs:
            sorted_word= ''.join(sorted(word))
            if  sorted_word in dict_anagrams:
                dict_anagrams[sorted_word].append(word)
            else:
                dict_anagrams[sorted_word]=[word]

        return [value for value in dict_anagrams.values()]
