class NumArray:
    def __init__(self, nums):
        sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            sums.append(cur_sum)
        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]