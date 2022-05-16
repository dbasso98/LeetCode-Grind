class MyQueue:

    def __init__(self):
        self.normal_stack = []
        self.reversing_stack = []   

    def push(self, x: int) -> None:
        self.normal_stack.append(x)

    def pop(self) -> int:
        while len(self.normal_stack) > 1:
            self.reversing_stack.append(self.normal_stack.pop())
        result = self.normal_stack.pop()
        while len(self.reversing_stack) > 0:
            self.normal_stack.append(self.reversing_stack.pop())
        return result

    def peek(self) -> int:
        while len(self.normal_stack) > 0:
            self.reversing_stack.append(self.normal_stack.pop())
        result = self.reversing_stack[-1]
        while len(self.reversing_stack) > 0:
            self.normal_stack.append(self.reversing_stack.pop())
        return result

    def empty(self) -> bool:
	    return len(self.normal_stack) == 0

# Space complexity is O(n) too. Push is O(1), Peek is O(n) and pop too. To get amortized O(1) for peek and pop we can do this:
class MyQueue:  

    def __init__(self):
        self.normal_stack = []
        self.reversing_stack = [] 
        self.front = None

    def push(self, x: int) -> None:
        if not self.normal_stack:
            self.front = x
        self.normal_stack.append(x)

    def pop(self) -> int:
        if not self.reversing_stack:
            while len(self.normal_stack) > 0:
                self.reversing_stack.append(self.normal_stack.pop())
        result = self.reversing_stack.pop()
        return result

    def peek(self) -> int:
        if self.reversing_stack:
            return self.reversing_stack[-1]
        return self.front

    def empty(self) -> bool:
	    return len(self.normal_stack) == 0 and len(self.reversing_stack) == 0

# Pattern:
# We can use lists in python as surrogate for the stack.
# 1 3 5 is the queue I wanna implement, in the stack this would be 5 on top of 3 on top of 
# 1 and 1 on top of 3 on top of 5 in the other stack. So, first I fill the first stack, 
# when a pop comes then I put all elements starting from the top into the other stack, 
# and do a pop from the other, then I put remaining elements back into the first stack (O(n) tc). 
# When pushing I push just on the first stack. Is empty is done also on the first stack.
