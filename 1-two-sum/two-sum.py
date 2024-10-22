class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        result = []

        for index in range(len(nums)):
            if nums[index] in num_index:
                num_index[nums[index]].append(index)
            else:
                num_index[nums[index]] = [index]

        if len(num_index.get(target // 2, [])) > 1:
            result = num_index[target // 2]
            return result

        for num in nums:
            search = target - num
            if search in num_index and search != num:
                result = [ num_index[num][0], num_index[search][0]]
                break

        return result
        