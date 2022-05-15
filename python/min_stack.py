from math import inf

class MinStack:
    def __init__(self):
        self.stack = list()
        self.minimum = inf
	 
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val is not None:
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minimum:
            self.minimum = min(self.stack) if self.stack else inf
        return popped

    def top(self) -> int:
        return self.stack[-1] if self.stack else None 
        
    def getMin(self) -> int:
        return self.minimum if self.stack else inf

# Every operation takes O(1) rather than pop that takes O(n) in worst case scenario (when popping minimum).

# Pattern:
# Just keep track of the minimum every time an element is added to the stack.
