def kids_with_candies(candies, extraCandies: int):
    cur_max = 0
    ans = []
    for kid in candies:
        if kid > cur_max:
            cur_max = kid
    for kid in candies:
        if kid + extraCandies >= cur_max:
            ans.append(True)
        else:
            ans.append(False)

    return ans


print(kids_with_candies([2,3,5,1,3], 3))