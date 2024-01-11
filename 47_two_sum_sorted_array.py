def two_sum_sorted_array(numbers, target: int):
    l, r = 0, len(numbers)-1
    while l < r:
        cur = numbers[l]+numbers[r]
        if cur == target:
            return [l+1,r+1]

        if cur > target:
            r -= 1
        if cur < target:
            l += 1


print(two_sum_sorted_array([2,7,11,15], 9))