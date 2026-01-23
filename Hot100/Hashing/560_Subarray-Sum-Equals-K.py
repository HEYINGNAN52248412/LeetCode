#better solution, only one loop.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #This dict is to store the times that certain "sum" occured. cuz there might be negatives and zero in the list, so previous sum may be repeated.
        #if the first element equals to k, then it won't be count (pre_fix_sum_current-k, which is 0 in this situation, is not in the dict)
        #so we have to manually initialize it
        pre_fix_sum_times = {0: 1}

        #the number of the total subarray
        subarray=0

        #sum of all the previous elements
        pre_fix_sum_current = 0

        for num in nums:
            pre_fix_sum_current += num

            if pre_fix_sum_current not in pre_fix_sum_times:
                pre_fix_sum_times[pre_fix_sum_current] = 0

            # If pre_fix_sum_current - target = k, a valid subarray is found
            # We look for the frequency of the complement: (pre_fix_sum_current - k)
            subarray += pre_fix_sum_times[pre_fix_sum_current-k] if (pre_fix_sum_current-k in pre_fix_sum_times) else 0
            pre_fix_sum_times[pre_fix_sum_current] += 1

        return subarray


#ugly solution with syntax mistake
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_fix_sum={}
        subarray=0

        for index, num in enumerate(nums):
            pre_fix_sum[index] = pre_fix_sum[index-1] + num if index>0 else num

            for i in range(0,index):
                if pre_fix_sum[index]-pre_fix_sum[i] == k:
                    subarray+=1
        
        return subarray
"""
