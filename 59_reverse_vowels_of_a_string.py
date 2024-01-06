def reverse_vowels(s: str) -> str:
    d = {'a', 'e', 'i', 'o','u'}
    l, r = 0, len(s)-1
    sl = list(s)
    while l <= r:
        if not sl[l].lower() in d:
            l += 1
            continue
        if not sl[r].lower() in d:
            r -= 1
            continue
        
        sl[l], sl[r] = sl[r], sl[l]
        l += 1
        r -= 1

    return ''.join(sl)


print(reverse_vowels('hello'))