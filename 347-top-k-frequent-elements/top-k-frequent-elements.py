class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter = {}

        for num in nums:
            if num in frequency_counter:
                frequency_counter[num]+=1
            else:
                frequency_counter[num]=1

        return sorted(frequency_counter, key=frequency_counter.get, reverse=True)[0:k]