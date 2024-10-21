class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        def count_characters(s:str)-> dict:
            char_counter={}
            for char in s:
                if char in char_counter:
                    char_counter[char]+=1
                else:
                    char_counter[char]=1
            return char_counter

        
        return count_characters(s) == count_characters(t)

