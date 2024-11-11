class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n= len(nums)
        current_sum = 0
        current_len = 0
        sum_dict= {0 : -1}

        target = sum(nums) - x
        if target == 0:
            return n

        for i in range(n):
            current_sum += nums[i]
            diff = current_sum - target
            j = sum_dict.get(diff, i)

            current_len = max(current_len, i - j)

            sum_dict[current_sum] = i

        return n - current_len if current_len > 0 else -1