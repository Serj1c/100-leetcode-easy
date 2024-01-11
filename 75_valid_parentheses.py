def is_valid_parentheses(s: str) -> bool:
    stack = []
    dictt = {'(':')', '{':'}', '[':']'}
    for c in s:
        if c in dictt:
            stack.append(c)
        else:
            if stack:
                car = stack.pop()
                if dictt[car] != c:
                    return False
            else:
                return False
    return len(stack) == 0


print(is_valid_parentheses(')(){}'))
print(is_valid_parentheses('()[]{}'))
print(is_valid_parentheses('([]'))
print(is_valid_parentheses('([])'))