class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start, end = 0, len(nums) - 1
        first, last = -1, -1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                last = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [first, last]