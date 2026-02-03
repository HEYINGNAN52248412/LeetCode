class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #the farest that we can reach
        farest = 0
        #use a loop to traverse every elements in the list and store the farest place we can reach
        for i in range(len(nums)):
            #if there is an element that we can not reach at all, return false
            if i > farest:
                return False

            farest = max(farest, nums[i]+i)

            if farest >= len(nums)-1:
                return True
        #all other weird situation. Just in case.
        return False