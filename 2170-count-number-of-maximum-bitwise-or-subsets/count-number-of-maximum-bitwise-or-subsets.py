import itertools

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:  

        def calculate_or(subset):
            sub_or=0
            for num in subset:
                sub_or = sub_or | num
            
            return sub_or

        # Calculate the Max OR
        max_or = calculate_or(nums)
        count =0
        # Make increasing subsets starting with subsets of 1(single item subsets) and check their max_or
        # eg startrs with [[a],[b],[c],[d],...]
        # then [[a,b],[]...], [[a,b,c],[]...] and so on
        for i in range(1, len(nums)+1):
            #https://docs.python.org/3/library/itertools.html
            for subset in itertools.combinations(nums, i):
                if calculate_or(subset) == max_or:
                    count+=1
        

        return count