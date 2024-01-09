def longest_palindrome(s: str) -> int:
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    cnt = 0
    for key in d:
        cur = d[key] - (d[key] % 2)
        cnt += cur
        d[key] -= cur

    if sum(d.values()):
        cnt += 1

    return cnt    


print(longest_palindrome('bananas'))
print(longest_palindrome('ccc'))
