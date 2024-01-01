def find_numbers(nums) -> int:
    def d_num(num):
        ret = 0
        while num:
            num //= 10
            ret += 1

        return ret
    
    ans = 0

    for num in nums:
        ans += 0 if d_num(num) % 2 else 1

    return ans