#better O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_length=0

        for num in numbers:
            #We only need smallest numbers in sequences. Skip if the num is not the smallest in any sequence.
            if num -1 in numbers:
                continue

            #This num is the smallest one in a sequence. Keep going up until we find the largest one in this sequence.
            current_num = num
            current_length = 1

            while current_num+1 in numbers:
                current_num += 1
                current_length+=1

            max_length = max(max_length, current_length)

#bad solution(O(n)but not that good because of too many hash finds):
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence_dict={}
        max_len=0
        for num in nums:
            if num in sequence_dict:
                continue

            #get endpoint length
            left_len = sequence_dict.get(num - 1, 0)
            right_len = sequence_dict.get(num + 1, 0)

            current_len = left_len + 1 + right_len

            max_len = max(max_len, current_len)

            sequence_dict[num] = current_len

            #update the value of the left/right terminal point, which is the length of the link
            sequence_dict[num - left_len] = current_len 
            sequence_dict[num + right_len] = current_len

        return max_len
"""