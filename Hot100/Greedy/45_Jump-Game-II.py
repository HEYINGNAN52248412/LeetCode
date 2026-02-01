#better solution: pay(move the step) first, then choose the landing point. We do this because we need to move at least once.
class Solution:
    def jump(self, nums: List[int]) -> int:
        # current_jump_end: The boundary of our current "paid" landing zone. 
        # We've already committed a step to reach anywhere within this range.
        current_jump_end = 0
        
        # farthest_scouted_reach: The best possible future reach found by our scout 'i' 
        # while traversing the current paid zone.
        #we need to pay at least once, so they are all 0 at the very beginning
        farest_two_jump_sum = 0
        step = 0

        #the index is not the current position of the jumper
        for i in range(len(nums)-1):
            #after every payment, the farest_two_jump search the scope of the current nums to get the farest next two jump it can make.
            farest_two_jump_sum = max(nums[i] + i, farest_two_jump_sum)

            #we have already travesed all the possible landing point
            if i == current_jump_end:
                #made the current jump. and now the farest_two_jump_sum it became the new end.
                current_jump_end = farest_two_jump_sum

                #pay for the new jump
                step += 1 

                #if the final is in the scope of the current "paid" area, just finish it.
                if current_jump_end >= len(nums)-1:
                    break

        return step

            

#dumb solution: travese every possible jumping point and solve the problem with nested loop
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        n = 0
        while n <len(nums)-1:
            max_step = 0
            for i in range (1, nums[n]+1):
                if  n+i <= len(nums)-1 and  i + nums[n+i] >= max_step + nums[n + max_step]:
                    max_step = i
            n += max_step
            step += 1

        return step
"""