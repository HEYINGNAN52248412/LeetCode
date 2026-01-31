from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we used deque cuz d.pop = d.leftpop = O(1)
        max_List = deque()
        maximum_sliding = []

        for i in range (len(nums)):
            #i is the lastest num
            #we put it in the deque
            #it will "eat" all the nums that are greater than/ equal to it.
            #then we put it in the end of the deque. 
            #See? it would be quite simple to sort if we only cared about the largest one.
            #the len(deque) will never be zero. cuz we always append the i at the end of it.
            while max_List and nums[i] >= nums[max_List[-1]]:
                max_List.pop()
            max_List.append(i)
            
            #if the max one is out of the sliding window, we pop it.
            if max_List[0] <= i - k:
                max_List.popleft()

            #the first one(largest one) in the deque is the max_num
            if i >= k-1:
                maximum_sliding.append(nums[max_List[0]])

        return maximum_sliding