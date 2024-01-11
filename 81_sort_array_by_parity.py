def sort_array_by_parity(nums):
    if len(nums) < 2:
        return nums
    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l] % 2 == 1 and nums[r] % 2 == 1:
            r -= 1
            continue

        if nums[l] % 2 == 0:
            l += 1
            continue    

        if nums[l] % 2 != 0 and nums[r] % 2 == 0:
            nums[l], nums[r] = nums[r], nums[l]

        l += 1
        r -= 1
    return nums


print(sort_array_by_parity([0,1,2]))
print(sort_array_by_parity([3,1,2,4]))
print(sort_array_by_parity([0]))

def sort_array_by_parity2(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


print(sort_array_by_parity([0,1,2]))
print(sort_array_by_parity([3,1,2,4]))
print(sort_array_by_parity([0]))