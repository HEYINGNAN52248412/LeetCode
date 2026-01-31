#two pointer:
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0

        water_amount = 0
        left = 0
        right = len(height)-1

        left_max = 0
        right_max = 0

        #water_amount += min(left_max, right_max) - height[i]
        while left<right:
            # if height[left] < height[right], then left_max must be smaller than right_max. So min(left_max, right_max) = left_max
            # left_max > right_max >= right > left will never happen. 
            # because if (left_max > right_max), then the left should still be trapped at left_max.  
            # When (right_max < left_max) and the left is at left_max, left = left_max > right_max > right. So the pointer that should move is right.
            #so when height[left] < height[right], it implies two situation: 1. left_max < right 2. left_max > right but left_max < right_max

            if height[left] < height[right]:
                water_amount += left_max - height[left] if left_max - height[left]>=0 else 0
                left_max = max(left_max, height[left])
                left += 1
            else:
                water_amount += right_max - height[right] if right_max - height[right]>=0 else 0
                right_max = max(right_max, height[right])
                right -= 1

        return water_amount

#brute solution:
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0

        water_amount = 0

        # the maximum amount of water that each column can hold depends on the minimum value of the highest column on its right and the highest column on its right, minus the height of the current column
        for current_block in range (1, len(height)-1):
            left = current_block-1
            right = current_block+1
            max_left = 0
            max_right = 0

            while left >= 0:
                max_left = max(max_left, height[left])

            while right <= len(height)-1:
                max_right = max(max_right, height[right])
            
            water_amount += min(max_left, max_right) - height[current_block] if min(max_left, max_right) - height[current_block] >= 0 else 0

            current_block +=1

        return water_amount


"""