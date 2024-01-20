def sorted_squares(nums):
    l, r = 0, len(nums)-1
    ans = []

    while l <= r:
        if abs(nums[r]) > abs(nums[l]):
            ans.append(nums[r]*nums[r])
            r -= 1
        else:
            ans.append(nums[l]*nums[l])
            l += 1
    return ans[::-1]


print(sorted_squares([-4,-1,0,3,10]))