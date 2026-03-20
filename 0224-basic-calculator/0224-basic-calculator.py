class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1   # +1 for '+', -1 for '-'
        
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            
            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1
            
            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1
            
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()   # sign before '('
                result += stack.pop()  # result before '('
        
        return result + sign * number