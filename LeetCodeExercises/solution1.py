class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1= len(word1)
        len2 = len(word2)
        diff= len1 - len2
        if (diff > 0 ):
            word2 += diff*' '
        elif (diff < 0):
            diff*=-1
            word1 += diff*' '

        word3= zip(list(word1), list(word2))

        answ=""

        for comb in word3:
            answ += ''.join(comb).replace(" ", "")
        return answ