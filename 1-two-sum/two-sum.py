class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        twoSumIndex= []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                twoSumIndex = [i, prevMap[diff]]
                break
            else:
                prevMap[n] = i

        return twoSumIndex

