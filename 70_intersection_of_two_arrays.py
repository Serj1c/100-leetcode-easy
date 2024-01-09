def intersection(nums1, nums2):
    d1 = {}
    d2 = {}
    
    for num in nums1:
        if num in d1:
            d1[num] += 1
        else:
            d1[num] = 1

    for num in nums2:
        if num in d2:
            d2[num] += 1
        else:
            d2[num] = 1

    res = []
    for num in d1:
        if num in d2:
            res.append(num)
    return res


print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))