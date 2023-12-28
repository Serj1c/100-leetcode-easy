def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l <= r:
        if not s[l].isalnum():
            l = l + 1
            continue
        if not s[r].isalnum():
            r = r - 1
            continue

        if s[l].lower() != s[r].lower():
            print(s[l], s[r])
            return False

        l = l + 1
        r = r - 1

    return True


print(is_palindrome('A man, a plan, a canal: Panama'))
