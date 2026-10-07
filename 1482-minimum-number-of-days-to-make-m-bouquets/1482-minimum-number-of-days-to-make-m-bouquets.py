class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def isValid(day):
            total = 0
            count = 0
            for i in range(len(bloomDay)):
                if day >= bloomDay[i]:
                    count += 1
                    if count == k:
                        total += 1
                        count = 0
                    if total >= m:
                        return True
                else:
                    count = 0
                    
            return total >= m

        ans = -1
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = (left + right) // 2

            if isValid(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans