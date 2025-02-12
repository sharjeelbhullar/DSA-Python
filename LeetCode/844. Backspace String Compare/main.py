class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string: str) -> str:
            skip = 0
            result = []
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    result.append(c)
            return result
        
        return process_string(s) == process_string(t)
