def is_subsequence(s: str, t: str) -> bool:
    stack = []
    for i in range(len(s) - 1, -1, -1):
        stack.append(s[i])

    for c in t:
        if len(stack) >= 1 and c == stack[-1]:
            stack.pop()

    return len(stack) == 0


print(is_subsequence('abc', 'ahbgdc'))
