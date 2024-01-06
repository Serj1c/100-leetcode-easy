def license_key_formatting(s: str, k: int) -> str:
    s = s.replace('-')
    s.upper()

    ans = ''

    for i in range(len(s)-1, -1, -1):
        if not len(ans) % (k+1):
            ans += '-'
        ans += s[i]

    return ans[::-1][:-1]