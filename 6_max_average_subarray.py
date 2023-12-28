from collections import deque


def findMaxAverageWithQueue(nums, k: int) -> float:
    q = deque([])
    ans = float('-inf')

    for num in nums:
        q.append(num)

        if len(q) == k:
            ans = max(ans, sum(q)/k)

        if len(q) > k:
            q.popleft()
            ans = max(ans, sum(q) / k)

    return ans


def findMaxAverage(nums, k: int) -> float:
    ans = float('-inf')

    count = 0
    curSum = 0

    for i in range(len(nums)):
        count += 1
        curSum += nums[i]

        if count == k:
            ans = max(ans, curSum/k)

        if count > k:
            curSum -= nums[i-k]
            ans = max(ans, curSum / k)

    return ans