class Solution:
    def __sum_nums(nums: List[int]) -> float:
        num_sum = 0
        for num in muns:
            num_sum+= num

        return num_sum/2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged_list=[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1

        if i < len(nums1):
            merged_list += nums1[i:]

        if j < len(nums2):
            merged_list += nums2[j:]

        index = len(merged_list)//2

        if len(merged_list) % 2 ==0:
            return (merged_list[index] + merged_list[index-1])/2
        else:
            return merged_list[index]
        
            

            



            

    