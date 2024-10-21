class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        Output=[]
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                if target == (nums[index]+ nums[index2]):
                    Output= [index, index2]
                    break



        return Output
                
