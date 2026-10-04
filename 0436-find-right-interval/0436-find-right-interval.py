class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)

        ans = [-1] * len(intervals)
        intervals.sort()
        for i in range(len(intervals)):
            start, end = i, len(intervals) - 1

            while start <= end:
                mid = (start + end) // 2
                
                if intervals[mid][0] >= intervals[i][1]:
                    ans[intervals[i][2]] = intervals[mid][2]
                    end = mid - 1
                else:
                    start = mid + 1
                
        return ans