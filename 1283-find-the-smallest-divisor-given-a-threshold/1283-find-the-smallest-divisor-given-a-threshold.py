class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def IsValid(arr, divisor):
            result = 0
            for n in arr:
                result += (n + divisor - 1) // divisor
            return result <= threshold

        ans = None
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2

            if IsValid(nums, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans