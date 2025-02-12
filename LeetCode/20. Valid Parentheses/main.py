class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]
        
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            else:
            # Check if stack is empty or if the top element doesn't match
                if not stack or c != stack.pop():
                    return False

    # Check if the stack is empty at the end
        return not stack