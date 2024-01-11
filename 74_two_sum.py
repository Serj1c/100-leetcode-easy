def two_sum(nums, target: int):
    res = []
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            res.append(seen[complement])
            res.append(i)
            return res
        seen[nums[i]] = i
    return res


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
