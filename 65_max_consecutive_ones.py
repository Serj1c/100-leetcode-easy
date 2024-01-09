def find_max_consecutive_ones(nums) -> int:
    res = 0
    cur = 0

    if len(nums) == 1:
        return nums[0]

    for r in range(len(nums)):
        if nums[r] == 1:
            cur += 1
        else:
            res = max(cur, res)
            cur = 0
        if r == len(nums)-1 and r != 0:
            res = max(cur, res)

    return res


print(find_max_consecutive_ones([1,1,0,1,1,1]))
print(find_max_consecutive_ones([1,0,1,1,0,1]))
print(find_max_consecutive_ones([1]))