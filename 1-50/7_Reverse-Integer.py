#Convert the absolute value of x to a string and reverse it with [::-1]

class Solution:
    def reverse(self, x: int) -> int:
        string = str(x) if x>=0 else str(-x)
        string = string[::-1]
        res = int(string) if x >= 0 else -int(string)

        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res