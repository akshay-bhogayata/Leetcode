class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_exp = False
        
        for i, ch in enumerate(s):
            
            if ch.isdigit():
                seen_digit = True
            
            elif ch in ['+', '-']:
                # sign only allowed at start OR just after e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            elif ch == '.':
                # dot only once and not after exponent
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            
            elif ch in ['e', 'E']:
                # exponent only once and must come after a number
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False  # reset for exponent part
            
            else:
                return False
        
        return seen_digit