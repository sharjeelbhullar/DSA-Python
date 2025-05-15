class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, value: int) -> None:
        if not self.stack:
            self.mini = value
            self.stack.append(value)
        else:
            if value < self.mini:
                # Encode the previous min value
                encoded_val = 2 * value - self.mini
                self.stack.append(encoded_val)
                self.mini = value
            else:
                self.stack.append(value)

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.mini:
            # Recover previous min value
            self.mini = 2 * self.mini - top

    def top(self) -> int:
        if not self.stack:
            return -1
        top = self.stack[-1]
        if top < self.mini:
            return self.mini
        return top

    def getMin(self) -> int:
        return self.mini

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()