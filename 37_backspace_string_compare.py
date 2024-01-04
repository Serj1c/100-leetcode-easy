def backspace_compare(s: str, t: str) -> bool:
    stack_s = []
    for c in s:
        if c == '#':
            if stack_s:
                stack_s.pop()
        else:
            stack_s.append(c)

        stack_t = []
    for c in t:
        if c == '#':
            if stack_t:
                stack_t.pop()
        else:
            stack_t.append(c)

    return ''.join(stack_s) == ''.join(stack_t)


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))