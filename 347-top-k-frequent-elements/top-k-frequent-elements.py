class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = {}
        sorted_list = []

        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1


        sorted_dict = dict(sorted(num_counter.items(), key=lambda item: item[1], reverse=True))

        solution= []

        counter = 1

        for item in sorted_dict:
            solution.append(item)
            if counter == k:
                break
            counter +=1

        return solution