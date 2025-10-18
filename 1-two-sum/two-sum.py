class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums={}

        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff in dict_nums:
                return [i, dict_nums[diff]]
            else:
                dict_nums[nums[i]] = i

        return []