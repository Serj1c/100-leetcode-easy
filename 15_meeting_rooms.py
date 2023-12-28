def can_attend_meetings(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


print(can_attend_meetings([[0, 10], [5, 10]]))
print(can_attend_meetings([[15, 20], [25, 30]]))
print(can_attend_meetings([[35, 40], [25, 30]]))
