def summary_ranges(nums):
    ans = []
    if len(nums) == 0:
        return []
    s = nums[0]
    nums.append(float('inf'))

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            e = nums[i-1]
            if s != e:
                ans.append(f'{s}->{e}')
            else:
                ans.append(f'{e}')
            s = nums[i]
        
    return ans


print(summary_ranges([0,1,2,4,5,7]))
print(summary_ranges([0,2,3,4,6,8,9]))