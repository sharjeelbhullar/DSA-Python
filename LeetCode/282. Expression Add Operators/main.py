from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
    
        # Helper function to perform backtracking
        def backtrack(index, prev_operand, current_operand, value):
            if index == len(num):
                if value == target:
                    result.append(current_operand)
                return
            
            for i in range(index + 1, len(num) + 1):
                temp_str = num[index:i]
                
                # Skip numbers with leading zeros (except '0')
                if len(temp_str) > 1 and temp_str[0] == '0':
                    continue
                
                # Convert the current substring to an integer
                current_num = int(temp_str)
                
                if index == 0:
                    # No operator before the first number
                    backtrack(i, current_num, temp_str, current_num)
                else:
                    # Addition
                    backtrack(i, current_num, current_operand + "+" + temp_str, value + current_num)
                    # Subtraction
                    backtrack(i, -current_num, current_operand + "-" + temp_str, value - current_num)
                    # Multiplication
                    backtrack(i, prev_operand * current_num, current_operand + "*" + temp_str, value - prev_operand + (prev_operand * current_num))
        
        backtrack(0, 0, "", 0)
        return result