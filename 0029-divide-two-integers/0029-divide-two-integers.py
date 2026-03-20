class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor
            
        quotient = 0
        
        while dividend <= divisor:
            temp_divisor = divisor
            power_of_two = -1
            
            while temp_divisor >= -1073741824 and dividend <= (temp_divisor << 1):
                temp_divisor <<= 1
                power_of_two <<= 1
                
            dividend -= temp_divisor
            quotient += power_of_two
            
        return -quotient if not is_negative else quotient