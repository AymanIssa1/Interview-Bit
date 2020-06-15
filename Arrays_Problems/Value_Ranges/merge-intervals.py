# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self) -> str:
        return "[" + str(self.start) + ", " + str(self.end) + "]"

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


# @param intervals, a list of Intervals
# @param new_interval, a Interval
# @return a list of Interval
def insert(intervals, new_interval):
    if new_interval.start > new_interval.end:
        new_interval.start, new_interval.end = new_interval.end, new_interval.start

    if len(intervals) == 0:
        return [Interval(new_interval.start, new_interval.end)]

    result = []

    current_start = intervals[0].start
    current_end = intervals[0].end
    i = 0

    while new_interval.start >= current_start and new_interval.start >= current_end:
        result.append(intervals[i])
        i += 1
        if i >= len(intervals):
            result.append(new_interval)
            return result

        current_start = intervals[i].start
        current_end = intervals[i].end

    overlapping_start = current_start
    if current_start > new_interval.start:
        overlapping_start = new_interval.start

    while new_interval.end >= current_start and new_interval.end >= current_end:
        i += 1
        if i >= len(intervals):
            result.append(Interval(overlapping_start, new_interval.end))
            return result

        current_start = intervals[i].start
        current_end = intervals[i].end

    overlapping_end = current_end
    if current_start > new_interval.end:
        overlapping_end = new_interval.end
        i -= 1

    result.append(Interval(overlapping_start, overlapping_end))

    for j in range(i + 1, len(intervals)):
        result.append(intervals[j])

    return result
