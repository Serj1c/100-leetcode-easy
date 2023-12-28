def two_sum(nums, target: int):
    res = []
    d = {}
    for i in range(len(nums)):
        d[nums[i]] = i
    print(d)

    for j in range(len(nums)):
        if target - nums[j] in d:
            print(target - nums[j])
            res.append(d[target - nums[j]])
            res.append(j)
            res.sort()
            return res


print(two_sum([2, 7, 11, 15], 9))
