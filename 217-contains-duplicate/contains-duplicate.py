class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_counter={}
        duplicate=False

        for num in nums:
            if num in dict_counter:
                dict_counter[num]+=1
            else:
                dict_counter[num]=1

        for item in dict_counter.values():
            if item>1:
                duplicate=True
                break
                
        return duplicate