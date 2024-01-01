def remove_adjacent_dupls(s: str) -> str:
    stack = []

    for c in s:
        
        if stack and stack[-1] == c:
            stack.pop()
            continue
        
        stack.append(c)
        
    return ''.join(stack)

print(remove_adjacent_dupls('abbaca'))