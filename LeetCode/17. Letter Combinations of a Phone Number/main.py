from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            for letter in digit_to_letters[current_digit]:
                # Add the letter to the current combination
                current_combination.append(letter)
                # Move to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack by removing the last letter
                current_combination.pop()
        
        backtrack(0, [])
        return result