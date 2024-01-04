def is_alien_sorted(words, order: str) -> bool:
    if len(words) < 2:
        return True
    
    d = {}
    for i in range(len(order)):
        d[order[i]] = i
    d['#'] = -1

    for i in range(1, len(words)):
        w1 = words[i-1]
        l1 = len(w1)
        w2 = words[i]
        l2 = len(w2)

        if len(w1) < len(w1):
            w1 += '#' * (l2-l1)
        else:
            w2 += '#' * (l1-l2)

        for j in range(len(w1)):
            if d[w1[j]] < d[w2[j]]:
                break
            if d[w1[j]] > d[w2[j]]:
                return False
    return True


print(is_alien_sorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_alien_sorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(is_alien_sorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
print(is_alien_sorted(["reb","inci"], "tcyklqfhoeapndgbimsujzvxwr"))