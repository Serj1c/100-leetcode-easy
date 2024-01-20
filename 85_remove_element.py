def remove_element(nums, val: int) -> int:
    l, r = 0, len(nums)-1

    cnt = 0
    if len(nums) < 2 and nums[0] == val:
        return 0

    while l <= r:
        if nums[l] == val:
            while nums[r] == val:
                r -= 1
                if r == 0:
                    break
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                cnt += 1
                r -= 1

        l += 1
    return l if cnt > 0 else cnt


#print(remove_element([3,2,2,3], 3))
#print(remove_element([0,1,2,2,3,0,4,2], 2))
print(remove_element([2], 3))
#print(remove_element([1], 1))
#print(remove_element([1, 1], 1))