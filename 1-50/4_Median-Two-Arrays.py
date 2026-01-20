"""
GENERAL IDEA:
The goal is to find the median of the combined sorted arrays. Conceptually, we can 
partition the merged array into two halves— Left and Right —where every element in the 
Left half is less than or equal to every element in the Right half.

Since the merged array is composed of sorted arrays A and B, such a partition must 
exist by splitting A and B individually into (A_left, A_right) and (B_left, B_right). 
Because A and B are already sorted, the critical values are at the partition lines:
- Max of Left half: max(A_left_max, B_left_max)
- Min of Right half: min(A_right_min, B_right_min)

The total number of elements in the combined Left half is fixed (half of the total size). 
Therefore, by determining the partition index in array A (i), the partition index in 
array B (j) is automatically derived as: j = half_size - i.

ALGORITHM DYNAMICS:
We utilize Binary Search on the partition index of array A to find the "perfect cut."

WHY START BINARY SEARCH ON THE SMALLER ARRAY?
1. Efficiency: Performing Binary Search on the shorter array ensures a time complexity 
   of $O(\log(\min(m, n)))$. This is crucial for handling cases where one array is 
   significantly larger than the other.
2. Index Safety: By ensuring len(A) <= len(B), we guarantee that cut_in_B always be non-negative (mid_point - cut_in_A > 0), preventing out-of-bounds 
   errors without needing complex conditional checks.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        mid_point=(len(A)+len(B))//2 #whole_left<=whole_right

        if len(A) > len(B):
            A,B = B,A #we cut the shorter array to save time&avoid out-of-bounds errors

        left_bound, right_bound = 0, len(A)
        while left_bound <= right_bound:
            #definition of "cut": cut_in_A is not an index. The value it holds represent the number of elements that stay on the left side of it.A
            #When the cut_in_A = 5, it means there are 5 integers smaller than it(index 0-4).
            cut_in_A = (left_bound+right_bound)//2 #A_left<=A_right
            cut_in_B = mid_point - cut_in_A

            #deal with out-of-bound problem. Use the infinity to remain mathematical validation even when one side of the partition is empty
            #for example, for [1,2] and [4,5]. 
            # First round cut_in_A=1, A_left_max=1, A_right_min=2. B_left_max > A_right_min, continue 
            # Second round cut_in_A=2, which is not in A. 
            #it means the whole A array should be in the overall left side. 
            #To keep the Mathematical Harmony, A_right_min must be infinity to validate "B_left_max < A_right_min"
            A_left_max = A[cut_in_A-1] if cut_in_A > 0 else float("-inf") 
            B_left_max = B[cut_in_B-1] if cut_in_B > 0 else float("-inf")
            A_right_min =A[cut_in_A] if cut_in_A < len(A) else float("inf")
            B_right_min =B[cut_in_B] if cut_in_B < len(B) else float("inf")
             
            
            if A_left_max <= B_right_min and  B_left_max <= A_right_min:  #and B_left_max <= B_right_min and A_left_max <= A_right_min
                if (len(A)+len(B))%2 == 1:
                    return min(A_right_min, B_right_min)
                else:
                    return ((max(A_left_max, B_left_max)) + (min(A_right_min, B_right_min)))/2
            
            #binary search
            if A_left_max > B_right_min:
                right_bound=cut_in_A-1
            else:
                left_bound=cut_in_A+1\
                