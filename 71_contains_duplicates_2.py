def contains_nearby_duplicate(nums, k: int) -> bool:
    d = {}

    for i, num in enumerate(nums):
        if num in d and i - d[num] <= k:
            return True
        d[num] = i

    return False


print(contains_nearby_duplicate([1,2,3,1], 3))
print(contains_nearby_duplicate([1,0,1,1], 1))
print(contains_nearby_duplicate([1,2,3,1,2,3], 2))
print(contains_nearby_duplicate([99, 99], 2))