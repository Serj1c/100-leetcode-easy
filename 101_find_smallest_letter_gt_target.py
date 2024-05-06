def nextGreatestLetter(letters, target: str) -> str:
    l, r = 0, len(letters)-1
    while l <= r:
        mid = (r + l) // 2
        if letters[mid] > target:
            r = r - 1
        else:
            l = l + 1
    print(l, len(letters), l % len(letters))
    return letters[l % len(letters)]

print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["c","f","j"], "c"))
print(nextGreatestLetter(["x","x","y","y"], "a"))