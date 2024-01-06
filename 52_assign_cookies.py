def find_content_children(g, s) -> int:
    ans = 0

    g.sort()
    s.sort()

    i = 0
    for c in s:
        if i == len(g):
            break

        if c >= g[i]:
            ans += 1
            i += 1

    return ans
        