class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        #according to the execution of the intepreter, the if will only be executed once.
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        #extract the number
        res = 0
        for char in s:
            if char.isdigit():
                #put them into calculation directly instead of storing them in a list
                res = res * 10 + int(char)
            else:
                break
        
        res *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(res, INT_MAX))

#state machine:
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        leading_space=True
        sign = False
        negative = False
        leading_zero=True
        digits = False
        num_list = []

        for char in s:
            match char:
                case " " if leading_space:
                    continue

                case "+" if not sign and not digits:
                    leading_space=False
                    sign = True
                    leading_zero=True

                case "-" if not sign and not digits:
                    leading_space=False
                    sign = True
                    negative = True
                    leading_zero=True

                case n if '1'<=n<='9':
                    leading_space=False
                    leading_zero = False
                    digits=True
                    num_list.append(n)

                case "0":
                    leading_space=False
                    digits=True
                    if not leading_zero:
                        num_list.append("0")
                
                case _:
                    break

        if num_list:
            num_str = "".join(num_list)
        else: 
            return 0
        

        if negative:
            num = -int(num_str)
            if num < -2**31:
                num = -2**31
        else:
            num = int(num_str)
            if num > 2**31-1:
                num = 2**31-1
        
        return num
"""
                    


