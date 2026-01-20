#the best way to find a palindrome is to start from its center
#so we assume every character/gap are the center, and record the longest one.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_reserve = ""

        def expand(s, left, right, max_reserve):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            
            new_reserve = s[left+1: right]
            return new_reserve if len(new_reserve)>len(max_reserve) else max_reserve

        for i in range(len(s)):
            max_reserve = expand(s, i, i, max_reserve)
            max_reserve = expand(s, i, i+1, max_reserve)

        return max_reserve