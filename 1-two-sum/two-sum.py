class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_digit = 0
        for index in range(len(nums)):
            first_digit= nums[index]
            for index2 in range((index+1), len(nums)):
                second_digit= nums[index2]
                if (first_digit+second_digit) == target:
                    return [index, index2]    
