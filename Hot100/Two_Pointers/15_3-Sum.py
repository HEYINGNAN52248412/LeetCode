class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #a sorted list is the most important prerequisite of the solution
        nums.sort()
        result = []

        #i is fixed. And since we need 3 different pointers it's meaningless to make i to len(nums)-2 (only one element after it)
        for i in range (len(nums)-2):

            #if the smallest one is bigger than zero, the total sum can never be 0.Just break.
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element to ensure unique triplets.
            # If nums[i] == nums[i-1], we've already explored all possible combinations starting with this value.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            #use two pointers to find the solution
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    #skip duplicated j and k. Always check j<k in case the remaining elements are all the same.
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j+=1
                    while j < k and nums[k-1] == nums[k]:
                        k-=1

                    #starting to look for the next possible solution
                    j += 1 
                    k -= 1    

        return result