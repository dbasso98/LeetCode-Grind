def isValid(self, s: str) -> bool:
    opened = {"(":0,"[":1,"{":2}
    closed = {")":0,"]":1,"}":2}
    find_open = []
    for par in s:
        if par in opened:
            find_open.append(par)
        elif par in closed:
            if find_open and closed[par]==opened[find_open[-1]]:
                find_open.pop()
            else:
                return False
    
    return len(find_open) == 0 

# O(n) time complexity, O(n) space complexity with n number of parentheses in the string.

# Pattern:
# Use a stack to store open parentheses, when a closing parentheses occurs then check if this one is of the same type of the one on the top.
