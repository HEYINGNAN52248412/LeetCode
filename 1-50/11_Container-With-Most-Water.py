#brute-force(O(n²)): traverse throught all the possible area with nested for-loop
#better idea(O(n)): always move the pointer with the smaller height inward 
#Since the area is depended on the shorter bar, the best result of moving the longer bar is to keep the height but shorten the width(reduce the area).
#We only explore those possibilities that could bring a larger area, so we only move the shorter bar.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right =0, len(height)-1

        while left<right:
            max_water = max(max_water, min(height[left], height[right])*(right-left))

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_water
        