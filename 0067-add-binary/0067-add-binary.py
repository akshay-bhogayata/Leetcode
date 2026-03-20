class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result = str(total % 2) + result
            carry = total // 2
        
        if carry:
            result = str(carry) + result
        
        return result