class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_counter={}
        duplicate=False

        for num in nums:
            if num in dict_counter:
                duplicate=True
                break
            else:
                dict_counter[num]=1
                
        return duplicate