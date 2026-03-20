class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If 1 row or string is shorter than the number of rows
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of empty strings for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        
        for char in s:
            rows[cur_row] += char
            
            # Change direction if we hit the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down
            cur_row += 1 if going_down else -1
            
        # Join all the rows together
        return ''.join(rows)