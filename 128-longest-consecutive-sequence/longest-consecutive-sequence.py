class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        curr_len = 1
        n = len(nums)
        start = nums[0]

        max_len = 0

        for i in range(1,n):
            diff = nums[i] - nums[i-1]

            if diff == 1 :
                curr_len +=1
            elif diff != 0 :
                max_len = max(max_len, curr_len)
                curr_len =1


        return max(max_len, curr_len)