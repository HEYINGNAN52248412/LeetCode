class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10 == 0 and x!=0):
            return False

        reverse_half = 0
        while x>reverse_half:
            reverse_half = x%10 + reverse_half*10
            x=x//10

        return x == reverse_half or x == reverse_half//10
        