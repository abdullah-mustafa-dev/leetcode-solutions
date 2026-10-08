class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        def calStartEnd(index, radius):
            start = max(heaters[index] - radius, 1)
            end = heaters[index] + radius
            return start, end

        def isWarmed(radius):
            total, i, j = 0, 0, 0
            start, end = calStartEnd(j, radius)
            while i < len(houses):
                if start <= houses[i] <= end:
                    total += 1
                elif houses[i] > end:
                    j += 1

                    if j >= len(heaters):
                        return False

                    start, end = calStartEnd(j, radius)
                    continue
                elif houses[i] < start:
                    return False
                i += 1

            return total >= len(houses)

        ans = 0
        start = 0
        end = max(max(houses), max(heaters)) - min(min(houses), min(heaters))
        while start <= end:
            mid = (start + end) // 2

            if isWarmed(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans