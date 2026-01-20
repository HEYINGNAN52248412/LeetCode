#quite easy as long as you know what is a Hashmap and what is  Sliding Window Optimization
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map={}
        left=0
        max_length = 0

    #The right pointer keep sliding until it meets a repeated character.(Find that by checking the hashmap)
    #the right pointer keeps updating the hashmap all the time, make sure all the keys in the hashmap is the latest(rightest).
    #When a repeated character's found, move the left pointer, and get the current length(cuz the left pointer will only go further and never come back)
        for right, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char]+1)
            
            char_map[char] = right

            max_length = max (max_length, right - left + 1)

        return max_length