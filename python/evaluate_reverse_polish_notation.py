def evalRPN(self, tokens: List[str]) -> int:
    def do_operation(first, second, operand):
        if operand == "+":
            return first+second
        elif operand == "-":
            return first-second
        elif operand == "*":
            return first*second
        else:
            return int(first/second)
        
    stack = []  
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            result = do_operation(first_operand, second_operand, token)
            stack.append(result)
            
    return stack.pop()

# Pattern:
# Use a stack to store the numbers and when an operand is encountered then 
# pop twice from the stack and compute the expression.
